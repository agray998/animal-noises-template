from flask import Flask, request, jsonify, Response
import requests
import random
app = Flask(__name__)

# animal generator route here
@app.route('/get_animal', methods = ['GET'])
def get_animal():
    dict = {1:"pig", 2:"cow", 3:"horse"}
    num = random.randint(1, 4)
    animal = dict[num]
    return Response(animal, mimetype='text/plain')

# animal noise generator route here
@app.route('/get_noise', methods = ['POST'])
def get_noise():
    dict = {"pig":"oink", "cow":"moo", "horse":"neigh"}
    animal = request.data.decode("utf-8")
    noise = dict[animal]
    return jsonify({"animal":animal, "noise":noise})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)