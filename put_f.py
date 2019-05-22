
from all_import import *
from load_write import *
from error_f import *
from flask import jsonify, abort, request, make_response
import requests

@app.route('/tasks/<string:task_id>', methods=['PUT'])
def update_task(task_id):
    tasks=load_file()

    task = list(filter(lambda t: t['date'] == task_id, tasks))

    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    task[0]['date'] = request.json.get('date', task[0]['date'])
    task[0]['temperature'] = request.json.get('temperature', task[0]['temperature'])
    task[0]['precipitation'] = request.json.get('precipitation', task[0]['precipitation'])

    write_file(tasks)

    return jsonify({'task': task[0]})

def test_put():

    headers = {'content-type': 'application/json'}
    data = {

        "temperature": 2,
        "precipitation": 19
    }
    print("\nrequsts.put")
    s = "20-12-2019"
    response = requests.put("http://127.0.0.1:5000/tasks/" + s, data=json.dumps(data), headers=headers)
    #data = r.json()
    assert response.status_code == 200
