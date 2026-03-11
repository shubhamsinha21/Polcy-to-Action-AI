def recommend_schemes(user_data, schemes):

    recommendations = []

    for scheme in schemes:

        if user_data["occupation"].lower() in scheme["scheme_name"].lower():
            recommendations.append(scheme["scheme_name"])

    return recommendations