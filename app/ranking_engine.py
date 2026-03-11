def rank_schemes(user, schemes):

    ranked = []

    for scheme in schemes:

        score = 0

        if user["occupation"] == scheme["occupation"]:
            score += 0.4

        if user["income"] <= scheme["income_limit"]:
            score += 0.3

        if scheme["state"] == "All" or user["state"] == scheme["state"]:
            score += 0.2

        if not scheme["land_required"] or user["land_owned"]:
            score += 0.1

        ranked.append((scheme, round(score, 2)))

    ranked.sort(key=lambda x: x[1], reverse=True)

    return ranked