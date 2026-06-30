from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/grid", methods=["GET"])
def get_grid():
    return jsonify({"message": "hello"})

if __name__ == "__main__":
    app.run(debug=True)