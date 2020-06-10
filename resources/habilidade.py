from flask import request
from flask_restful import Resource
from resources.bd import TblHabilidades


class Habilidade(Resource):
    def get(self, id=None):
        return TblHabilidades().selectAll() if id is None else TblHabilidades().select(id=id)

    def delete(self, id=None):
        resp = TblHabilidades().delete(id=id)
        return ({"success": "delete"}, 200) if resp else ({"failed": "not found"}, 404)

    def post(self):
        return TblHabilidades().create(**request.get_json())

    def put(self, id=None):
        return TblHabilidades().update(id, **request.get_json())
