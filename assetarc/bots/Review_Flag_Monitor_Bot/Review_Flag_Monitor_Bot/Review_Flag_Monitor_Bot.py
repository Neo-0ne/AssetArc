import json

def review_flag_monitor(input_json):
    try:
        data = json.loads(input_json)
        flagged_sessions = [session for session in data['sessions'] if session.get('flagged')]
        if not flagged_sessions:
            return "No flagged sessions found."
        review_summary = []
        for session in flagged_sessions:
            entry = f"Session ID: {session['id']} | Reason: {session['reason']} | User Comment: {session['comment']}"
            review_summary.append(entry)
        return "\n".join(review_summary)
    except Exception as e:
        return f"Error processing input: {e}"

# Example usage
if __name__ == "__main__":
    with open("flagged_input.txt", "r") as f:
        input_json = f.read()
    output = review_flag_monitor(input_json)
    print(output)
