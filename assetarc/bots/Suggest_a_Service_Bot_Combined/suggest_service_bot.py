import json

def suggest_service(user_input):
    keywords = {
        "trust": "Try the Trust Setup Bot to establish a secure legal trust.",
        "company": "Try the Company Formation Bot to register your business.",
        "tax": "Try the Tax Optimization Bot for structuring your tax strategy.",
        "residency": "Try the Residency/Citizenship Bot for cross-border migration structuring.",
        "risk": "Try the Risk Assessment Bot to assess and reduce your vulnerabilities.",
    }

    suggestions = []
    for keyword, suggestion in keywords.items():
        if keyword in user_input.lower():
            suggestions.append(suggestion)

    if not suggestions:
        suggestions.append("No direct match found. A human advisor will review your request and get back to you.")

    return {
        "input": user_input,
        "suggestions": suggestions
    }

if __name__ == "__main__":
    test_input = "I want to set up a company to manage my crypto and reduce my taxes."
    response = suggest_service(test_input)
    print(json.dumps(response, indent=2))
