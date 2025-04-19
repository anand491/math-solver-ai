from flask import Flask, request, jsonify
import sympy as sp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

@app.route('/solve', methods=['POST'])
def solve_math():
    data = request.get_json()
    problem = data.get("problem", "")

    try:
        expression = sp.sympify(problem)
        simplified = sp.simplify(expression)
        return jsonify({
            "original": str(expression),
            "simplified": str(simplified)
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)