from flask import Flask
from flask_restful import Api
from resources.developer import Developer

app = Flask(__name__)
api = Api(app)




api.add_resource(Developer, '/dev/', '/dev/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
