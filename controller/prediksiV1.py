import urllib.request
from flask import request, jsonify
import json
from flask_restful import Resource
from configapi.dbconfig import configdb


mongo = configdb()
class Mahasiswa(Resource):
    def post(self):
        value = mongo.db.datamhs
        valueInput = mongo.db.inputmhs
        trasnkrip = request.json
        data = {
                "Inputs": {
                        "input1":
                        [
                            {
                                    'Jenis_Kelamin': trasnkrip['Jenis_Kelamin'],   
                                    'Jenis_Seleksi': trasnkrip['Jenis_Seleksi'],   
                                    'Pendapatan_Wali': trasnkrip['Pendapatan_Wali'],   
                                    'Pendidikan_Ibu': trasnkrip['Pendidikan_Ibu'],   
                                    'IP_SMT1': trasnkrip['IP_SMT1'],   
                                    'IP_SMT2': trasnkrip['IP_SMT2'],   
                                    'IP_SMT3': trasnkrip['IP_SMT2'],   
                                    'IP_SMT4': trasnkrip['IP_SMT3'],   
                                    'sks1': trasnkrip['sks1'],   
                                    'sks2': trasnkrip['sks2'],   
                                    'sks3': trasnkrip['sks2'],   
                                    'sks4': trasnkrip['sks4'],   
                            }
                        ],
                },
            "GlobalParameters":  {
            }
        }

        body = str.encode(json.dumps(data))

        url = 'https://ussouthcentral.services.azureml.net/workspaces/df99cc1a15274b63901dad3330973fce/services/3679d6df526a42569fd6e59edd5e953c/execute?api-version=2.0&format=swagger'
        api_key = '3l0QKh1YGi8ESxnITI1c4sF9zDzGVpsfl4ZE3S9RegIvqup5o9XBjzLAHTop2sg83Ny9f7St8CXYkjClEes2EQ==' # Replace this with the API key for the web service
        headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

        req = urllib.request.Request(url, body, headers)

        valueInput.insert(trasnkrip)

        try:
            response = urllib.request.urlopen(req)

            result = response.read()
            my_json = result.decode('utf8').replace("'", '"')
            print(type(my_json))
            data = json.loads(my_json)
            paket = {}
            for i in data["Results"]["output1"]:
                value.insert_one(i)
                paket.update(i)
            print(paket)
            #'Scored Labels': 'TT', 'Scored Probabilities': '0.625845388416492'
            return jsonify({"Result":[{'Scored Labels': paket['Scored Labels'], 'Scored Probabilities': paket['Scored Probabilities']}]})

        except urllib.error.HTTPError as error:
            print("The request failed with status code: " + str(error.code))
            print(error.info())
            print(json.loads(error.read().decode("utf8", 'ignore')))
            return jsonify({'404'})