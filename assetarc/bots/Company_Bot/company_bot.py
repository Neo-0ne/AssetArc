import os

def generate_company_documents(country, company_name, shareholders, directors):
    with open("prompts/company_prompt.txt", "r") as f:
        prompt = f.read()
    filled_prompt = prompt.format(
        country=country,
        company_name=company_name,
        shareholders=shareholders,
        directors=directors
    )
    print("Prompt ready for processing:")
    print(filled_prompt)
    os.makedirs("output", exist_ok=True)
    with open("output/Memorandum_and_Articles.docx", "w") as f:
        f.write("Generated Memorandum and Articles of Association")
    return "Memorandum_and_Articles.docx"
