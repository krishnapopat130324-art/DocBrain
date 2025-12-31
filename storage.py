import json
import os

FILE_NAME = "documents.json"


def load_documents():
    """Load documents from JSON file"""
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_documents(documents):
    """Save documents to JSON file"""
    with open(FILE_NAME, "w") as file:
        json.dump(documents, file, indent=4)


def add_document(name, number, expiry, notes=""):
    """Add a new document"""
    documents = load_documents()

    document = {
        "name": name,
        "number": number,
        "expiry": expiry,
        "notes": notes
    }

    documents.append(document)
    save_documents(documents)
