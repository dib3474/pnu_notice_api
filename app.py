from flask import Flask, request, json, jsonify
from cse_notice import get_notice
app = Flask(__name__)

@app.route("/notice", methods=['POST']) #get 으로 변경
def get_data():
    response = get_notice()
    return response
