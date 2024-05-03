import json


def load():
    with open('src/config/config.json') as f:
        data = json.load(f)
        return data['mysql']
