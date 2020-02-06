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
    data = getContent()
    temp = []
    for i in data:
      print(i)
      temp.append(i)
    value.insert({"stackOverFlow":temp})
    
    return jsonify(temp)  

  def post(self):
    value = mongo.db.stackoverflow
    data ={}
    temp = []
    temp.append(getContent())
    data.update(temp)
    reqTime = datetime.now()
    data.update(reqTime)
    value.insert(data)
    return jsonify({"result":data})
    


class File(Resource):
  def get(self):
    value = mongo.db.stackoverflow
    output = {}
    for s in value.find():
      s.pop('_id')
      output.update(s)
    return jsonify(output)

  def post(self):
    value = mongo.db.stackoverflow
    data = request.json
    reqTime = datetime.now()
    reqTime = {'reqTime':reqTime}
    print(reqTime)
    data.update(reqTime)
    value.insert(data)
    return jsonify({'result' : "inserted"})

class Anotherfile(Resource):
  def get(self,id):
    value = mongo.db.stackoverflow
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