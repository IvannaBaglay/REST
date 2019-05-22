import json
filename = 'data.json'

def load_file():
    try:
        with open(filename, 'r') as libfile:
            tasks = json.load(libfile)
            libfile.close()
    except FileNotFoundError:
        print('\n File not found, creating new empty one')
    return tasks

def write_file(tasks):
    with open(filename, 'w') as libfile:
        json.dump(tasks, libfile)
        libfile.close()