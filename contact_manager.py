import json
from typing import List,Dict


def add_contacts(contacts: List[dict]):
    """Adds new contact to the list"""

    name=input("Enter your name:")
    phone=input("Enter your phone number:")
    email=input("Enter your email address:")

    contact={'name':name,'phone':phone,'email':email}
    contacts.append(contact)
    print("Contact added...")


def view_contacts(contacts: List[dict])-> None:
    """View all contacts in the list"""

    print("Contact list:\n")

    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone Number: {contact['phone']}")
        print(f"Email Address: {contact['email']}")
