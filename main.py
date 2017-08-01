import logging

from flask import Flask, jsonify, redirect, render_template, request, session, abort
import json

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/api/v1.0/json', methods=['GET', 'POST'])
def renderblog():
    finaldata=[]
    with open('resume.json') as f:
        data = json.load(f)
        finaldata.append(data)
    return jsonify(finaldata)


@app.route('/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/api/v1.0/tasks', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/')
def hello():
	return "Hello World"

@app.route('/brad')
def brad():
	return "Pull Resume here"

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8080, debug=True)
