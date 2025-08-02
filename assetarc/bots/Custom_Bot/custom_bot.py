import os

def generate_custom_structure(entities, cross_border_notes):
    with open("prompts/custom_prompt.txt", "r") as f:
        prompt = f.read()
    filled_prompt = prompt.format(
        entities=entities,
        cross_border_notes=cross_border_notes
    )
    print("Custom structuring prompt generated:")
    print(filled_prompt)
    os.makedirs("output", exist_ok=True)
    with open("output/Custom_Structure_Memo.docx", "w") as f:
        f.write("This is the custom multi-entity structure memo.")
    return "Custom_Structure_Memo.docx"
