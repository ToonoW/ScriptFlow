import json


def json_read(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data


def json_append(filepath, item):
    with open(filepath, 'r+') as f:
        data = json.load(f)
        data.append(item)
        json.dump(data, f)


def json_replace(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)
