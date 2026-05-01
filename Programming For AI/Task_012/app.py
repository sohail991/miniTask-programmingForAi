from flask import Flask, render_template, request, jsonify
import pandas as pd
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

app = Flask(__name__)

model = SentenceTransformer('all-MiniLM-L6-v2')
df = pd.read_csv("medical_data.csv")
index = faiss.read_index("medical_index.index")

@app.route("/")
def index_page():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def chatbot_response():
    try:
        user_text = request.json.get("message", "").strip()
        if not user_text:
            return jsonify({"reply": "Please ask a question."})

     
        query_embedding = model.encode([user_text]).astype('float32')
        D, I = index.search(query_embedding, k=1) # Find 1 best match
        
      
        if D[0][0] > 1.5: 
            reply = "I'm not sure about that. Please contact our help desk at 555-0123."
        else:
            reply = df.iloc[I[0][0]]['Answer']

        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
