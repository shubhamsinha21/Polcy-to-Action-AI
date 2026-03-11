def evaluate_rule(user_data, rule):

    field = rule["field"]
    operator = rule["operator"]
    value = rule["value"]

    user_value = user_data.get(field)

    if operator == "==":
        return user_value == value

    if operator == "<":
        return user_value < value

    if operator == ">":
        return user_value > value

    return False


def check_eligibility(user_data, scheme):

    rules = scheme["eligibility_rules"]

    results = []

    for rule in rules:
        result = evaluate_rule(user_data, rule)
        results.append(result)

    matched = sum(results)
    total = len(rules)

    confidence = matched / total

    eligible = matched == total

    return eligible, confidence, results