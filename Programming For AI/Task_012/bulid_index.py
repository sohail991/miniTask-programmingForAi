import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer


data = {
    "Question": [
        "How do I book an appointment?", 
        "What are the hospital hours?", 
        "Who is the cardiologist?",
        "What departments do you have?"
    ],
    "Answer": [
        "You can book via our portal or call 555-0123.",
        "We are open 8 AM to 6 PM, Monday to Friday.",
        "Our senior cardiologist is Dr. Smith.",
        "We have Cardiology, Pediatrics, and Radiology."
    ]
}
df = pd.DataFrame(data)
df.to_csv("medical_data.csv", index=False)


model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(df['Question'].values)


dimensions = embeddings.shape[1]
index = faiss.IndexFlatL2(dimensions)
index.add(np.array(embeddings).astype('float32'))

faiss.write_index(index, "medical_index.index")
print("Index built successfully!")
