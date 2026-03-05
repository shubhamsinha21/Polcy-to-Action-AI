def evaluate_rule(user_data, rule):
    field = rule["field"]
    operator = rule["operator"]
    value = rule["value"]

    user_value = user_data.get(field)

    if operator == "==":
        return user_value == value

    if operator == "<":
        return user_value is not None and user_value < value

    if operator == ">":
        return user_value is not None and user_value > value

    return False


def check_eligibility(user_data, scheme):
    rules = scheme.get("eligibility_rules", [])
    
    if not rules:
        return False, 0.0

    results = [evaluate_rule(user_data, rule) for rule in rules]

    match_count = sum(results)
    total_rules = len(rules)

    confidence_score = match_count / total_rules

    is_eligible = match_count == total_rules

    return is_eligible, confidence_score