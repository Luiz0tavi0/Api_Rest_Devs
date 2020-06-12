from flask import request
from flask_restful import Resource
from services.hab_services import HabilidadeServices


class Habilidade(Resource):
    def get(self, id=None):
        return HabilidadeServices().selectAll() if id is None else HabilidadeServices().select(id=id)

    def delete(self, id=None):
        resp = HabilidadeServices().delete(id=id)
        return ({"success": "delete"}, 200) if resp else ({"failed": "not found"}, 404)

    def post(self):
        data = request.get_json()
        return HabilidadeServices().create(data)

    def put(self, id=None):
        return HabilidadeServices().update(id, **request.get_json())
