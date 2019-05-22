
from all_import import *
from load_write import *
from flask import jsonify, abort, request
import requests

@app.route('/tasks', methods=['POST'])

def create_task():
    tasks=load_file()
    if not request.json or not 'date' in request.json:
        abort(400)

    task = list(filter(lambda t: t['date'] == request.json['date'], tasks))

    if len(task) > 0:
        abort(404)
    if not request.json:
        abort(400)

    task = {
        'id': tasks[-1]['id'] + 1,
        'date': request.json['date'],
        'temperature': request.json.get('temperature', ""),
        'precipitation': request.json['precipitation']
    }
    tasks.append(task)

    write_file(tasks)

    return jsonify({'task': task}), 201

def test_post():

    data = {
        "date": "20-12-2019",
        "temperature": -2,
        "precipitation": 19
    }
    headers = {'content-type': 'application/json'}
    print("\nrequsts.post")
    response = requests.post("http://127.0.0.1:5000/tasks", data=json.dumps(data), headers=headers)
    #data = r.json()
    assert response.status_code == 404
