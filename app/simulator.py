def simulate_income_change(user, schemes, new_income):

    lost = []
    retained = []

    updated_user = user.copy()
    updated_user["income"] = new_income

    for scheme in schemes:

        if new_income > scheme["income_limit"]:
            lost.append(scheme["scheme_name"])
        else:
            retained.append(scheme["scheme_name"])

    return lost, retained