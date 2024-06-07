# pip install flask
from flask import Flask, jsonify, request

import gpt
import recorder
import stt

app = Flask(__name__)

@app.route("/record/start", methods=['POST'])
def start():
    recorder.start()

    response = {
        "result": "ok",
    }
    return jsonify(response)

@app.route("/record/stop", methods=['POST'])
def stop():
    recorder.stop()
    speach = stt.stt()
    result = gpt.chatGpt(speach)

    response = {
        "result": "ok",
        "speach": speach,
        "message": result
    }
    return jsonify(response)


@app.route("/chat", methods=['POST'])
def chat():
    req_data = request.get_json()
    try:
        query = req_data["query"]
    except KeyError:
        query = ""

    result = gpt.chatGpt(query)

    response = {
        "result": "ok",
        "message": result
    }

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8085)