import os
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

HUMAN_REVIEW_FILE = "pending_reviews.json"

def load_pending_reviews():
    if os.path.exists(HUMAN_REVIEW_FILE):
        with open(HUMAN_REVIEW_FILE, "r") as f:
            return json.load(f)
    return []

def save_pending_reviews(reviews):
    with open(HUMAN_REVIEW_FILE, "w") as f:
        json.dump(reviews, f, indent=2)

@app.route('/submit_for_review', methods=['POST'])
def submit_for_review():
    data = request.json
    pending_reviews = load_pending_reviews()
    pending_reviews.append(data)
    save_pending_reviews(pending_reviews)
    return jsonify({"status": "submitted", "total_pending": len(pending_reviews)})

@app.route('/get_pending_reviews', methods=['GET'])
def get_pending_reviews():
    return jsonify(load_pending_reviews())

@app.route('/approve_review/<int:index>', methods=['POST'])
def approve_review(index):
    reviews = load_pending_reviews()
    if 0 <= index < len(reviews):
        approved = reviews.pop(index)
        save_pending_reviews(reviews)
        return jsonify({"status": "approved", "review": approved})
    return jsonify({"error": "Invalid index"}), 400

if __name__ == '__main__':
    app.run(debug=True)
