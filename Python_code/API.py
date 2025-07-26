import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import LeadsManager

# Flask config for static file serving
app = Flask(
    __name__,
    static_folder=os.path.abspath(os.path.join(os.path.dirname(__file__), '../Website')),
    static_url_path="/"
)

CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/leads', methods=['GET'])
def get_leads():
    leads = LeadsManager.Get()
    return jsonify(leads), 200

@app.route('/leads', methods=['POST'])
def create_lead():
    lead = request.get_json()
    if not lead:
        return jsonify({"error": "No data provided"}), 400
    updated_inventory = LeadsManager.Add(LeadsManager.Get(), lead)
    return jsonify({"message": "Lead created successfully", "data": lead}), 201

@app.route('/leads/<int:lead_id>', methods=['DELETE'])
def delete_lead(lead_id):
    updated_inventory = LeadsManager.Remove(LeadsManager.Get(), lead_id)
    return jsonify({"message": "Lead deleted successfully"}), 200

@app.route('/leads/<int:lead_id>', methods=['PUT'])
def update_lead(lead_id):
    lead = request.get_json()
    if not lead:
        return jsonify({"error": "No data provided"}), 400
    updated_inventory = LeadsManager.Update(LeadsManager.Get(), lead_id, lead)
    return jsonify({"message": "Lead updated successfully", "data": lead}), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
