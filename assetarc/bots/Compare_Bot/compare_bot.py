import json

def compare_structures(structure1, structure2):
    with open("prompts/compare_prompt.txt", "r") as f:
        prompt = f.read()
    return prompt.format(structure1=structure1, structure2=structure2)
