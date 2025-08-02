import os
import json

def suggest_service(user_input):
    keywords = {
        "offshore": "Consider our Offshore Structure Bot.",
        "trust": "You might benefit from the Trust Setup Bot.",
        "residency": "Try the Residency / Citizenship Bot.",
        "tax": "Our Tax Optimization Bot is a great fit.",
        "company": "You may want to use the Company Formation Bot."
    }

    for keyword, suggestion in keywords.items():
        if keyword in user_input.lower():
            return {
                "suggestion": suggestion,
                "submitted_to_notion": True,
                "notion_record": {
                    "query": user_input,
                    "suggested_bot": suggestion
                }
            }

    return {
        "suggestion": "No direct match found. A custom advisor review has been queued.",
        "submitted_to_notion": True,
        "notion_record": {
            "query": user_input,
            "suggested_bot": "Manual Advisor Review"
        }
    }

if __name__ == "__main__":
    query = input("What do you need help with?
> ")
    response = suggest_service(query)
    print(json.dumps(response, indent=2))
