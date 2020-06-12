from abc import ABCMeta
from models.modelhabilidade import ModelHabilidade
from repository.bd import lista_devs, lista_habilidades
from services.abstract_service import Abstract_Service


class HabilidadeServices(Abstract_Service, metaclass=ABCMeta):
    def __init__(self):
        super(HabilidadeServices, self).__init__(lista_habilidades)

    def create(self, listaHab):
        habs = {ModelHabilidade(hab) for hab in listaHab}
        
        novasHabs = habs.difference(lista_habilidades)
        for hab in novasHabs:
            lista_habilidades.append(hab)
        return [hab.id for hab in novasHabs]

    def update(self, id=None, **kwargs):
        for hab in range(len(lista_habilidades)):
            if lista_habilidades[hab].id == id:
                lista_habilidades[hab].descricao = kwargs.get('descricao')
                return True
        return False
    def findByNames(self, listNames):
        result = [hab for hab in lista_habilidades if hab.descricao in listNames]
        return result
