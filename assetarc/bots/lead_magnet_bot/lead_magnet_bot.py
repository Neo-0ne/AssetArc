import os
import json
from datetime import datetime

def generate_lead_magnet(email: str, selected_document: str):
    magnets = {
        "Trust Setup Guide": "trust_setup_guide.pdf",
        "Offshore Structuring 101": "offshore_structuring_guide.pdf",
        "Asset Protection Blueprint": "asset_protection_blueprint.pdf"
    }

    if selected_document not in magnets:
        return {"error": "Invalid document selection."}

    log_entry = {
        "email": email,
        "document": selected_document,
        "timestamp": datetime.utcnow().isoformat()
    }

    with open("magnet_download_log.json", "a") as log_file:
        json.dump(log_entry, log_file)
        log_file.write("\n")

    return {
        "message": f"Download link sent to {email} for '{selected_document}'",
        "file": magnets[selected_document]
    }

if __name__ == "__main__":
    email = input("Enter your email: ")
    document = input("Select a document (Trust Setup Guide, Offshore Structuring 101, Asset Protection Blueprint): ")
    result = generate_lead_magnet(email, document)
    print(result)