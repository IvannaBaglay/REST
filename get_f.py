from all_import import *
from load_write import *
from flask import jsonify, abort, request, make_response
import requests

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks=load_file()
    return jsonify({'tasks': tasks})


@app.route('/tasks/<string:task_id>', methods=['GET'])
def get_task(task_id):
    tasks=load_file()
    task = list(filter(lambda t: t['date'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})




def test_get():

    response = requests.get("http://127.0.0.1:5000/tasks")
    #data = r.json()
    assert response.status_code == 200

    print("\nrequsts.get")
    s = "20-12-2019"
    response = requests.get("http://127.0.0.1:5000/tasks/" + s)
    #data = r.json()
    assert response.status_code == 200

    s = "20-12-2019"
    response = requests.get("http://127.0.0.1:5000/tasks/" + s)
    #data = r.json()
    assert response.status_code == 200
