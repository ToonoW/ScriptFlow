# -*- coding: utf-8 -*-
import json


def json_read(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data


def json_append(filepath, item):
    with open(filepath, 'r+', encoding='utf-8') as f:
        data = json.load(f)
        data.append(item)
        json.dump(data, f)


def json_replace(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f)
