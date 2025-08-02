import os

def generate_trust_structure(jurisdiction, settlor, trustee, beneficiaries, assets):
    with open("prompts/trust_prompt.txt", "r") as f:
        prompt = f.read()
    filled_prompt = prompt.format(
        jurisdiction=jurisdiction,
        settlor=settlor,
        trustee=trustee,
        beneficiaries=beneficiaries,
        assets=assets
    )
    print("Prompt prepared for AI generation:")
    print(filled_prompt)
    # Simulate document creation
    os.makedirs("output", exist_ok=True)
    with open("output/Trust_Deed_Sample.docx", "w") as f:
        f.write("This would be the generated Trust Deed based on AI output.")
    return "Trust_Deed_Sample.docx"
