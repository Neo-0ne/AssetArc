
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/metrics', methods=['GET'])
def get_metrics():
    user_type = request.args.get('user_type', 'advisor')

    with open('client_data.json') as f:
        data = json.load(f)

    with open('advisor_metrics.json') as f:
        advisor_data = json.load(f)

    with open('admin_metrics.json') as f:
        admin_data = json.load(f)

    if user_type == 'client':
        return jsonify(data)
    elif user_type == 'admin':
        return jsonify(admin_data)
    else:
        return jsonify(advisor_data)

if __name__ == '__main__':
    app.run(debug=True)
