from flask import Flask, request 
import requests

app = Flask(__name__)

# home route here
# must query the animal API for an animal and a noise – the noise should be based on the animal
@app.route('/home', methods = ['GET', 'POST'])
def home():
    if method == 'GET':
        animal = requests.get('http://api:5000/get_animal')
        response = requests.post('http://api:5000/get_noise', data = animal)
        package = response.json()
        noise = package["noise"]
        return f"{animal} goes {noise}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)