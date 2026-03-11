import json

def load_schemes():

    with open("data/schemes.json") as f:
        return json.load(f)


def check_eligibility(user):

    schemes = load_schemes()

    eligible = []

    for scheme in schemes:

        if user["occupation"] != scheme["occupation"]:
            continue

        if user["income"] > scheme["income_limit"]:
            continue

        if scheme["state"] != "All" and user["state"] != scheme["state"]:
            continue

        if scheme["land_required"] and not user["land_owned"]:
            continue

        eligible.append(scheme)

    return eligible