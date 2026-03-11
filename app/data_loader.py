import json

def load_schemes(path="data/schemes.json"):
    with open(path, "r") as f:
        return json.load(f)