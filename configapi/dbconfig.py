from flask import Flask
from flask_pymongo import PyMongo
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'mongopy'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/mongopy'

def configdb():
    mongo = PyMongo(app)
    return mongo