import json


def load_schemes():

    with open("data/schemes.json") as f:
        return json.load(f)


def forecast_income_policy(new_limit):

    schemes = load_schemes()

    affected = []

    for s in schemes:

        if s["income_limit"] < new_limit:

            affected.append(s["scheme_name"])

    return affected