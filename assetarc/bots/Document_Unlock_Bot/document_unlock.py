
import json
import os
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route('/unlock-document', methods=['POST'])
def unlock_document():
    data = request.json
    token = data.get('token')
    session_id = data.get('session_id')

    if not token or not session_id:
        return jsonify({'error': 'Token and session ID required'}), 400

    # Simulated logic
    document_path = f"./unlocked/{session_id}_document.pdf"
    if os.path.exists(document_path):
        return send_file(document_path, as_attachment=True)
    else:
        return jsonify({'error': 'Document not found or not yet approved'}), 404

if __name__ == '__main__':
    app.run(debug=True)
