from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)

@app.route('/structure_comparison', methods=['POST'])
def structure_comparison():
    data = request.get_json()
    jurisdiction1 = data.get("jurisdiction1")
    jurisdiction2 = data.get("jurisdiction2")

    # Mock comparison logic
    comparison_result = {
        "Jurisdiction 1": jurisdiction1,
        "Jurisdiction 2": jurisdiction2,
        "Summary": f"Comparison between {jurisdiction1} and {jurisdiction2}: Tax efficiency, compliance, residency advantages, and cost structure have been compared."
    }

    # Generate a mock PDF/Word file placeholder
    with open(os.path.join(bot_folder, "Structure_Comparison_Report.txt"), "w") as f:
        f.write("Structure Comparison Report\n")
        f.write(json.dumps(comparison_result, indent=2))

    return jsonify({"message": "Structure Comparison report generated successfully."})

if __name__ == '__main__':
    app.run(debug=True)
