import sys
# sys.path.append("/usr/local/lib/python3.9/dist-packages/")
# sys.path.append("/usr/lib/python3/dist-packages/")
# sys.path.append("/home/vish182/.local/lib/python3.9/site-packages")
from flask import Flask
from flask import jsonify, request
import json
from flask_cors import CORS

from handlers.transcribe import getTranscribedNotes


app = Flask(__name__)
CORS(app)


@app.route('/addUser', methods=["POST"])
def addUser():
    res = jsonify("success?")

    return res

@app.route('/getUser', methods=["POST"])
def getUser():
    _json = request.json
    print(_json)
    # print("please sigIN" )

    # user = mongo.db.users.find_one({"email": _json["email"]})

    # print(user)
    # res = jsonify("failed")
    # if _json["password"] == user["password"]:
    #     res = jsonify("success")
    
    res = jsonify("success")
    return res



@app.route('/getreq', methods=["POST"])
def getPrediction():
    _json = request.json
    print(_json)
    print("please")

    res = jsonify("pls")
    return res

@app.route('/all', methods=["GET"])
def getAlldocs():
    
    return jsonify("all")

@app.route('/getnotes', methods=["GET"])
def getNotes():
    res = getTranscribedNotes()
    return jsonify(res)

if __name__ == "__main__":
    print("hello world")
    app.run(debug=True)
    

