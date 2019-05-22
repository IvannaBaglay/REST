from all_import import *
from load_write import *
from flask import jsonify, abort, make_response
import requests

@app.route('/tasks/<string:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks=load_file()
    task = list(filter(lambda t: t['date'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    write_file(tasks)
    return jsonify({'result': True})


def test_delete():

    print("\nrequsts.delete")
    s = "20-12-2019"
    response = requests.delete("http://127.0.0.1:5000/tasks/" + s)
    #data = r.json()
    assert response.status_code == 200

    s = "20-12-2019"
    response = requests.delete("http://127.0.0.1:5000/tasks/" + s)
    #data = r.json()
    assert response.status_code == 404
