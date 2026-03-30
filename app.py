from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import os

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)
db = client.get_database("films")
films = db.get_collection("films")
app = Flask(__name__)



app.run()
