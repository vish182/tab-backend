import sys
# sys.path.append("/usr/local/lib/python3.9/dist-packages/")
# sys.path.append("/usr/lib/python3/dist-packages/")
# sys.path.append("/home/vish182/.local/lib/python3.9/site-packages")
from flask import Flask
from flask import jsonify, request
import json
from flask_cors import CORS
from utils.download import download_audio

from handlers.transcribe import getTranscribedNotes
from handlers.autochord import getChords
from handlers.createTabs import tabgen_api
from handlers.seperate import seperate


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

@app.route('/all', methods=["POST"])
def getAlldocs():
    _json = request.json
    print("POST body: ",_json)
    return jsonify("all")

@app.route('/getnotes', methods=["POST"])
def getNotes():
    _json = request.json
    print("POST body: ",_json)
    download_audio(_json['download'])

    dur = int(seperate(int(_json['startTime']), int(_json['endTime'])))

    print("duration of clip: ", dur)

    if int(_json['chords']) == 0:
        print("tabs")
        res = getTranscribedNotes()
        print("before tab gen: ", res)
        res = tabgen_api(res)
        print("after tabgen: ", res)
        res = [(str(x)).replace("'", "\"") for x in res]
        return json.dumps(res)
    elif int(_json['chords']) == 1:
        print("chords")
        res = getChords('temp.wav')
        return res

# @app.route('/get_Chords', methods=["POST"])
# def getNotes():
#     _json = request.json
#     print("POST body: ",_json)
#     download_audio(_json['download'])
#     res = getTranscribedNotes()
#     return jsonify(res)

if __name__ == "__main__":
    print("hello world")
    app.run(debug=True)
    

