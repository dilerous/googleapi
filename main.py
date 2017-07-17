import logging

from flask import Flask, jsonify, redirect, render_template, request, session, abort
import json

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

@app.route('/todo/api/v1.0/json', methods=['GET', 'POST'])
def renderblog():
    finaldata=[]
    with open('resume.json') as f:
        data = json.load(f)
        finaldata.append(data)
    return jsonify(finaldata)

@app.route('/')
def hello():
	return "Hello World"

@app.route('/brad')
def brad():
	return "Pull Resume here"

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
