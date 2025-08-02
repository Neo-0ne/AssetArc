import json
from difflib import get_close_matches

# Load sample FAQ data (can be replaced with real Notion integration)
with open('faqs.json', 'r') as file:
    faq_data = json.load(file)

def suggest_bot(user_query):
    questions = [faq["question"] for faq in faq_data]
    match = get_close_matches(user_query, questions, n=1, cutoff=0.5)
    if match:
        for faq in faq_data:
            if faq["question"] == match[0]:
                return {
                    "answer": faq["answer"],
                    "recommended_bot": faq.get("recommended_bot", "Please contact support for further help.")
                }
    return {
        "answer": "Sorry, we couldn't find a good match for your query.",
        "recommended_bot": "FAQ/NLP Bot"
    }

# Example usage
if __name__ == "__main__":
    query = input("Describe your need or question: ")
    result = suggest_bot(query)
    print(f"Suggested Bot: {result['recommended_bot']}")
    print(f"Answer: {result['answer']}")
