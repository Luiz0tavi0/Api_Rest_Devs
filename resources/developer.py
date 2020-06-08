from flask import request, jsonify
from flask_restful import Resource

from models.model_developer import Model_Developer
from models.model_habilidade import Model_Habilidade
from resources.bd import lista_devs, lista_habilidades


class Developer(Resource):
    def get(self, id=None):
        if id is None:
            result= [dev.to_json() for dev in lista_devs]
            return jsonify(result)
        result = [dev for dev in lista_devs if dev.id == id]

        return result[0].to_json() if len(result) != 0 else {"result": "Not Found"}


    def post(self):
        data = request.get_json()
        hab_recebidas = {Model_Habilidade(hab) for hab in data['habilidades']}

        novas_hab = hab_recebidas.difference(lista_habilidades)

        #Adiciona na lista/banco de habilidades as habilidades que não estão cadastradas.
        for hab in novas_hab:
            lista_habilidades.append(hab)

        #Garante que todas habilidades de desenvolvedores tenham referência única na lista/banco de habilidades.
        data['habilidades'] = [hab for hab in lista_habilidades if hab in hab_recebidas]

        new_dev = Model_Developer(**data)

        lista_devs.append(new_dev)
        return {"dev_created": new_dev.id}, 201

    def put(self, id = None):
        for ind in range(len(lista_devs)):
            if lista_devs[ind].id == id:
                data = request.get_json()
                dev = Model_Developer(**data)

                hab_recebidas = {Model_Habilidade(hab) for hab in data['habilidades']}
                novas_hab = hab_recebidas.difference(lista_habilidades)

                #Adiciona na lista/banco de habilidades as habilidades que não estão cadastradas.
                for hab in novas_hab: lista_habilidades.append(hab)

                dev.id = lista_devs[ind].id
                dev.habilidades = [hab for hab in lista_habilidades if hab in hab_recebidas]
                lista_devs[ind] = dev
                return dev.to_json()

        return {"result": "Not Found"}

    def delete(self, id=None):
        for ind in range(len(lista_devs)):
            if lista_devs[ind].id == id:
                lista_devs.pop(ind)
                return {"result": "Deleted"}
        return {"result": "Not Found"}
