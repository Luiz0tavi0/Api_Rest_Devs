from abc import ABCMeta
from flask import request
from models.modeldeveloper import ModelDeveloper
from models.modelhabilidade import ModelHabilidade
from repository.bd import lista_devs
from services.abstract_service import Abstract_Service
from services.hab_services import HabilidadeServices


class DeveloperServices(Abstract_Service, metaclass=ABCMeta):
    def __init__(self):
        super(DeveloperServices, self).__init__(lista_devs)

    def create(self, **kwargs):
        dev = ModelDeveloper(**kwargs)

        HabilidadeServices().create(dev.habilidades)
        dev.habilidades = HabilidadeServices().findByNames(dev.habilidades)

        lista_devs.append(dev)
        return dev.id

    def update(self, id: str = None, **kwargs):
        for ind in range(len(lista_devs)):
            if lista_devs[ind].id == id:
                data = request.get_json()
                dev = ModelDeveloper(**data)

                HabilidadeServices().create(dev.habilidades)
                dev.habilidades = HabilidadeServices().findByNames(dev.habilidades)

                dev.id = lista_devs[ind].id

                lista_devs[ind] = dev
                return dev.to_json()

        return None
