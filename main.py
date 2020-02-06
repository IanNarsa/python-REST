from controller.fungsi import File, Anotherfile
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

api.add_resource(File, '/', '/update')
api.add_resource(Anotherfile,'/name/<id>')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)