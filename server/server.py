from flask import Flask, request, jsonify
from flask_cors import CORS
from models.Service import Service

app = Flask(__name__)
CORS(app, resources={r"/*":{"origins":"http://localhost:3000"}})

@app.route('/segitiga', methods=['POST'])
def segitiga():
    data = request.get_json()
    service = Service("segitiga")
    return jsonify({'data': service.generate_segitiga(data['number'])})

@app.route("/ganjil", methods=["POST"])
def ganjil():
    data = request.get_json()
    service = Service("ganjil")
    return jsonify({"data": service.generate_bilangan_ganjil(data["max"])})

@app.route("/prima", methods=["POST"])
def prima():
    data = request.get_json()
    service = Service("prima")
    return jsonify({"data": service.generate_bilangan_prima(data["max"])})

if __name__ == "__main__":
    app.run(debug=True)