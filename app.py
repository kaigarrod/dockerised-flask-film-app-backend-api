from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import os

uri = "mongodb://localhost:27017/"
client = MongoClient(uri)
db = client.get_database("films")
films = db.get_collection("films")
app = Flask(__name__)


def serialize_film(film):
    return {
        "id": str(film["_id"]),
        "title": film["title"]
    }


@app.route("/api/films", methods=["GET"])
def get_films():
    result = [serialize_film(film) for film in films.find({})]
    return jsonify({"data": result}), 200


@app.route("/api/films", methods=["POST"])
def post_films():
    if not request.json or not "title" in request.json or not request.json["title"].strip():
        return jsonify({"error": "invalid title"}), 400

    result = films.insert_one(
        {
            "title": request.json["title"]
        }
    )

    inserted_film = films.find({"_id": ObjectId(result.inserted_id)})
    return jsonify({"data": serialize_film(film) for film in inserted_film})


app.run()
