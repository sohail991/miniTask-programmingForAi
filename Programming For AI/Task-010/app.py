from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

HOSPITAL_DATA = {
    "doctors": "We have Dr. Smith (Cardiology) and Dr. Sarah (Pediatrics) available.",
    "departments": "Our main wings are Cardiology, Pediatrics, and Radiology.",
    "hours": "We are open 8:00 AM to 6:00 PM, Monday to Friday."
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def chatbot_response():
    user_data = request.json
    user_msg = user_data.get("message", "").lower().strip()
    

    if any(greet in user_msg for greet in ["hi", "hello", "hey"]):
        return jsonify({"reply": "Welcome! I can help you with doctor info or booking an appointment. What do you need?"})


    if "book" in user_msg or "appointment" in user_msg:
        return jsonify({"reply": "To book an appointment, please provide your **Full Name** and **Preferred Date**."})

    for key in HOSPITAL_DATA:
        if key in user_msg:
            return jsonify({"reply": HOSPITAL_DATA[key]})

    return jsonify({"reply": "I'm not sure about that. Would you like to book an appointment?"})

if __name__ == "__main__":
    app.run(debug=True)
