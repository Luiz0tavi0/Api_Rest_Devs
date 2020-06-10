from flask import Flask, request
from flask_restful import Api, Resource
from resources.developer import Developer
from resources.habilidade import Habilidade

app = Flask(__name__)
api = Api(app)

api.add_resource(Developer, '/dev/', '/dev/<string:id>')
api.add_resource(Habilidade, '/hab/', '/hab/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)

