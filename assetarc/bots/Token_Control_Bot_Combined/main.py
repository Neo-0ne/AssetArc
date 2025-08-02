
import json

def load_tokens(file_path='advisor_tokens.json'):
    with open(file_path, 'r') as f:
        return json.load(f)

def save_tokens(tokens, file_path='advisor_tokens.json'):
    with open(file_path, 'w') as f:
        json.dump(tokens, f, indent=4)

def generate_token(advisor_id, tokens):
    new_token = f"{advisor_id}_TOKEN_{len(tokens)+1}"
    tokens.append({"advisor_id": advisor_id, "token": new_token, "status": "active"})
    save_tokens(tokens)
    return new_token

if __name__ == "__main__":
    tokens = load_tokens()
    advisor_id = input("Enter Advisor ID: ")
    token = generate_token(advisor_id, tokens)
    print(f"Generated Token: {token}")
