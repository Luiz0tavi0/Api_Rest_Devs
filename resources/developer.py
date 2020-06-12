from flask import request, jsonify
from flask_restful import Resource
from services.dev_services import DeveloperServices
from models.modeldeveloper import ModelDeveloper
from models.modelhabilidade import ModelHabilidade
from repository.bd import lista_devs, lista_habilidades


class Developer(Resource):
    def get(self, id=None):
        return DeveloperServices().selectAll() if id is None else DeveloperServices().select(id=id)

    def post(self):
        response = DeveloperServices().create(**request.get_json())
        return ({"failed": "not created"}, 200) if response is None else({"dev_created": response}, 201)

    def put(self, id=None):
        response = DeveloperServices().update(id, **request.get_json())
        return ({"failed": "not found"}, 404) if response is None else response

    def delete(self, id=None):
        response = DeveloperServices().delete(id)

        return ({"success": "deleted"}, 200) if response else ({"failed": "not found"}, 404)
