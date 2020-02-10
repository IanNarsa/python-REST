from controller.fungsi import Masterdata,CariMahasiswa,Grafik
from controller.prediksiV1 import Mahasiswa
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()

api.add_resource(CariMahasiswa, '/nim/<id>')
api.add_resource(Mahasiswa, '/prediksi')
api.add_resource(Masterdata, '/getcontent/stackoverflow')
api.add_resource(Grafik, '/grafik')


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=4000)