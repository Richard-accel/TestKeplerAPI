from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow requests from any domain (for testing)

# In-memory storage for map data
current_data = {"locations": []}

@app.route('/update_map', methods=['POST'])
def update_map():
    global current_data
    current_data = request.json  # Data from Nocoly
    return jsonify({"status": "Data updated!"})

@app.route('/get_map_data', methods=['GET'])
def get_map_data():
    return jsonify(current_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)