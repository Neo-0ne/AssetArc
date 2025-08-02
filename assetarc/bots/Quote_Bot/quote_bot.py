import os
import random

def generate_quote(category):
    with open("prompts/quotes.txt", "r") as f:
        quotes = f.readlines()
    themed_quotes = [q for q in quotes if category.lower() in q.lower()]
    return random.choice(themed_quotes).strip() if themed_quotes else "No quote available for this theme."
