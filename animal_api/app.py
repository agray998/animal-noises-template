from flask import Flask, request, jsonify, Response
import random
app = Flask(__name__)

# animal generator route here
@app.route('/get_animal', methods = ['GET'])
def get_animal():
    animal = random.choice(["Pig", "Cow", "Horse"])
    return Response(animal, mimetype='text/plain')

# animal noise generator route here
@app.route('/get_noise', methods = ['POST'])
def get_noise():
    dict = {"Pig":"oink", "Cow":"moo", "Horse":"neigh"}
    animal = request.data.decode("utf-8")
    noise = dict[animal]
    return Response(noise, mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)