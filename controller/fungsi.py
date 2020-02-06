from flask_restful import Resource
from flask import Flask, jsonify, request
import sys
sys.path.append("..")
from configapi.dbconfig import configdb
from datetime import datetime

mongo = configdb()
class File(Resource):
  def get(self):
    value = mongo.db.formnames
    output = []
    for s in value.find():
      s.pop('_id')
      output.append(s)
    return jsonify({"result":output})

  def post(self):
    value = mongo.db.formnames
    data = request.json
    reqTime = datetime.now()
    reqTime = {'reqTime':reqTime}
    print(reqTime)
    data.update(reqTime)
    value.insert(data)
    return jsonify({'result' : "inserted"})

class Anotherfile(Resource):
  def get(self,id):
    value = mongo.db.formnames
    data = []
    unit = value.find({'userId':int(id)})
    for x in unit:
      if x:
        x.pop('_id')
        data.append(x)
        
        print(data)
      else:
        data.append('notfound')
    
    return jsonify({"result":data})