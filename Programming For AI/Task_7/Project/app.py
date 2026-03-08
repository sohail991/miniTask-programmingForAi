from flask import Flask, render_template
import requests

app = Flask(__name__)

NASA_API_KEY = "DEMO_KEY"
NASA_URL = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"

@app.route('/')
def index():
    # Fetch data from NASA
    response = requests.get(NASA_URL)
    data = response.json()
    
    # Render the HTML and pass the data to it
    return render_template('index.html', data=data)

if __name__ == '__main__':
    print("Flask server starting for Jahanzaib...")
    app.run(debug=True, port=5000)
