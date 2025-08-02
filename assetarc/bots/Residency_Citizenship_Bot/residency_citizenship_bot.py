import json

def generate_residency_options(destination, funds, timeline):
    if destination.lower() == "portugal":
        if funds >= 350000:
            return "Golden Visa program via property or investment fund"
        else:
            return "D7 Visa option for passive income holders"
    elif destination.lower() == "dubai":
        if funds >= 250000:
            return "10-year UAE Golden Visa"
        else:
            return "3-5 year investor visa with LLC setup"
    elif destination.lower() == "st. kitts":
        if funds >= 150000:
            return "Citizenship-by-Investment via donation or real estate"
        else:
            return "Not eligible for direct citizenship"
    else:
        return "Custom evaluation required for destination"

if __name__ == "__main__":
    with open("inputs.json") as f:
        data = json.load(f)
    result = generate_residency_options(data["destination"], data["funds"], data["timeline"])
    with open("residency_plan.txt", "w") as out:
        out.write(f"Recommended residency option: {result}")
