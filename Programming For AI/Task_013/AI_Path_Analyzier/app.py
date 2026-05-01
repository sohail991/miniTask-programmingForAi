from flask import Flask, render_template, request
from career_data import career_data

app = Flask(__name__)

def predict_career(user_input):
    user_input = user_input.lower()
    scores = {}

    for career, data in career_data.items():
        score = 0
        for interest in data["interests"]:
            if interest in user_input:
                score += 1
        scores[career] = score

    best = max(scores, key=scores.get)

    if scores[best] == 0:
        return ["General Career"]

    # return TOP 3 careers
    sorted_careers = sorted(scores, key=scores.get, reverse=True)
    return sorted_careers[:3]


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_input = request.form["skills"]

        careers = predict_career(user_input)

        results = []

        for c in careers:
            if c in career_data:
                results.append({
                    "career": c,
                    "roadmap": career_data[c]["roadmap"],
                    "resources": career_data[c]["resources"]
                })

        return render_template("result.html", results=results)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)