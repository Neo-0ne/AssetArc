import os

def unlock_document(doc_path, passcode):
    if passcode != "ASSETARC2025":
        return "Access Denied"
    with open(doc_path, "r") as f:
        return f.read()
