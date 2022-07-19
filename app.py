from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
api = Api(app)

class Base(Resource):
    def get(self):
        return {'Message':'Working'}

class addition(Resource):
    def post(self):
        reqData = request.get_json()
        num1 = reqData['num1']
        num2 = reqData['num2']
        return num1+num2

class multiply(Resource):
    def post(self):
        reqData = request.get_json()
        num1 = reqData['num1']
        num2 = reqData['num2']
        return num1*num2

api.add_resource(Base, '/')
api.add_resource(addition, '/add')
api.add_resource(multiply, '/multiply')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)