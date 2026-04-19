import json
from typing import List,Dict
from file_handler import save_contacts


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


def search_contacts(contacts:List[dict])-> None:
    """Search contacts in the list"""

    # [{'name':'john','phone':8182000},{'name':'den','phone':8182000}]

    contact_name= input("Enter name:").strip().lower()

    # List of contact
    # Add contact to contact_list for every contact[name]=contact_name
    contact_list=[contact for contact in contacts if contact_name in contact["name"].lower()]

    # If contact_name is list
    if not contact_list:
        print("No contacts found")

    for contact in contact_list:
        print(f"{len(contact_list)} contact found:\n")
        print(f"Name: {contact['name']}")
        print(f"Phone Number: {contact['phone']}")
        print(f"Email address: {contact['email']}")


def delete_contact(contacts: List[dict])-> None:
    contact_name= input("Enter name:").strip().lower()

    for contact in contacts:
        if contact['name']==contact_name:
            contacts.remove(contact)
            print("Contact removed")
            save_contacts(contacts)

            return
    print("Contact not found.")


