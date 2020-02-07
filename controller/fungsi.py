from flask_restful import Resource
from flask import Flask, jsonify, request
from controller.scraping import getContent
import sys
sys.path.append("..")
from configapi.dbconfig import configdb
from datetime import datetime

mongo = configdb()
temp={}
class Masterdata(Resource):
  def get(self):
    value = mongo.db.stackoverflow
    output = {}
    for s in value.find():
      s.pop('_id')
      output.update(s)
    return jsonify(output)

  def post(self):
    value = mongo.db.stackoverflow
    data ={}
    reqTime = datetime.now()
    data.update({"reqTime":reqTime, "stackOverFlowData":getContent()})
    #print(data)
    value.insert(data)
    return jsonify({"result":"Insert"})
    

class Anotherfile(Resource):
  def get(self,id):
    value = mongo.db.stackoverflow
    data = []
    unit = value.find({'userId':int(id)})
    for x in unit:
      if x:
        x.pop('_id')
        data.append(x)        
      else:
        data.append('notfound')
    
    return jsonify({"result":data})

class CariMahasiswa(Resource):
  def get(self,id):
    value = mongo.db.inputmhs
    data = []
    unit = value.find({'NIM':int(id)})
    for x in unit:
      if x:
        x.pop('_id')
        data.append(x)
      else:
        data.append('notfound')
    
    return jsonify({"result":data})