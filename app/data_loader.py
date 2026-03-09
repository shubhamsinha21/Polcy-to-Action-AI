import json

def load_schemes(filepath="data/schemes.json"):
    with open(filepath, "r") as f:
        schemes = json.load(f)
    return schemes