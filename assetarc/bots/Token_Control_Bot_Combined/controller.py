
from main import load_tokens, generate_token

def interface():
    print("Token Control Interface")
    advisor_id = input("Advisor ID: ")
    tokens = load_tokens()
    new_token = generate_token(advisor_id, tokens)
    print(f"New token created: {new_token}")

if __name__ == "__main__":
    interface()
