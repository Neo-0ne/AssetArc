import os

def deliver_vault(client_id, structure_type):
    os.makedirs("vaults", exist_ok=True)
    vault_path = f"vaults/{client_id}_{structure_type}_Vault.zip"
    with open("vaults/index.txt", "w") as f:
        f.write(f"Vault package for client: {client_id}\nStructure: {structure_type}\n")
    with open("vaults/readme.txt", "w") as f:
        f.write("This vault contains all documents related to your chosen structure.")
    os.system(f"zip -j {vault_path} vaults/index.txt vaults/readme.txt")
    return vault_path
