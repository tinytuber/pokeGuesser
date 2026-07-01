from flask import Flask, request, jsonify
from gridGenerator import generator

app = Flask(__name__)

@app.route('/')
def index():
    return "pokeGuesser API is running"

@app.route("/grid", methods=["GET"])
def get_grid():
    global grid_indices
    grid_indices = generator()
    return jsonify(grid_indices)

@app.route('/guess', methods=['POST'])
def post_guess():
    

if __name__ == "__main__":
    app.run(debug=True)