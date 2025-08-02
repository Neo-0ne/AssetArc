import os
import json

def generate_risk_report(inputs):
    risks = {
        "Data Breach": "High risk if no encryption or access controls in place.",
        "Key Man Risk": "High if the company relies heavily on one person.",
        "Regulatory Risk": "Moderate to high depending on compliance history and jurisdictions.",
        "Succession Risk": "High without a valid succession plan.",
        "Operational Bottlenecks": "Moderate if key tasks depend on few individuals.",
        "Asset Exposure": "Critical if ownership is public or directly tied to the individual.",
        "Client Concentration": "High if one client contributes more than 30% of revenue.",
        "Jurisdictional Conflict": "Elevated if operating across regulatory regimes.",
        "Document Fragmentation": "Severe if trust, company, and asset deeds are held in different jurisdictions with conflicting terms."
    }
    selected = inputs.get("scenarios", [])
    output = ["📋 Risk Assessment Report\n"]
    for scenario in selected:
        desc = risks.get(scenario, "No predefined risk found. Custom analysis required.")
        output.append(f"🔹 {scenario}: {desc}")
    return "\n".join(output)

if __name__ == "__main__":
    input_path = "inputs/scenario_input.json"
    output_path = "outputs/risk_report.txt"
    os.makedirs("outputs", exist_ok=True)
    with open(input_path, "r") as f:
        inputs = json.load(f)
    report = generate_risk_report(inputs)
    with open(output_path, "w") as f:
        f.write(report)
    print("✅ Risk Assessment Report Generated.")
