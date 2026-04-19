import json
from typing import List,Dict

FILE_NAME="data.json"

def load_contacts()->List[Dict]:
    """
    Loads contacts from the JSON file if file exists, otherwise returns empty list
    """

    # Open the file
    try:

        with open(FILE_NAME,'r') as file:
            data = json.load(file)
            return data

    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return []


def save_contacts(contacts:List[Dict]):
    """
    Saves contacts to the JSON file
    """
    # Sort it before saving
    sorted_contacts = sorted(contacts, key=lambda x: x["name"].lower())

    # Open the file
    with open(FILE_NAME,'w') as file:
        json.dump(sorted_contacts, file)