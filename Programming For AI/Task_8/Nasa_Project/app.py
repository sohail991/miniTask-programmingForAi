from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

NASA_API_KEY = "DEMO_KEY"

@app.route('/')
def index():
    # Fetch Astronomy Picture of the Day
    apod_url = f"https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}"
    apod_data = requests.get(apod_url).json()
    return render_template('index.html', apod=apod_data)

@app.route('/get_mars_photos')
def get_mars_photos():
    # Fetch Mars Rover Photos (Curiosity Rover)
    # We use 'sol 1000' as a standard data point for photos
    mars_url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={NASA_API_KEY}"
    try:
        response = requests.get(mars_url)
        data = response.json()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("Jahanzaib, your dynamic NASA app is running at http://127.0.0.1:5000")
    app.run(debug=True)
