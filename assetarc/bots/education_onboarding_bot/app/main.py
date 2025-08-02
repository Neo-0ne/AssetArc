
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/educate", methods=["POST"])
def educate_user():
    data = request.json
    goals = data.get("goals", "").lower()
    bot_suggestions = []

    if "trust" in goals:
        bot_suggestions.append("Trust Setup Bot")
    if "offshore" in goals:
        bot_suggestions.append("IBC Bot")
    if "tax" in goals:
        bot_suggestions.append("Tax Optimization Bot")
    if "citizenship" in goals or "residency" in goals:
        bot_suggestions.append("Residency / Citizenship Bot")

    return jsonify({"recommended_bots": bot_suggestions})

if __name__ == "__main__":
    app.run(debug=True)
