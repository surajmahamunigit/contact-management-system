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
    save_contacts(contacts)
    print("Contact added...")


def view_contacts(contacts: List[dict])-> None:
    """View all contacts in the list"""

    print("Contact list:\n")

    for contact in contacts:
        print(f"Name: {contact['name']}")
        print(f"Phone Number: {contact['phone']}")
        print(f"Email Address: {contact['email']}\n")


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
        if contact['name'].lower()==contact_name:
            contacts.remove(contact)
            print("Contact removed")
            save_contacts(contacts)

            return
    print("Contact not found.")


def update_contact(contacts: List[dict])-> None:
    """Update an existing contacts in the list"""

    contact_name= input("Enter name:").strip().lower()

    if not contact_name:
        print("Enter valid name.")

    for contact in contacts:
        if contact['name'].lower()==contact_name:

            contact_field= int(input("Enter new contact field you want to change: \n 1. Name \n 2. Phone Number \n 3. Email \n"))

            # Update the field
            if contact_field==1:
                name= input("Enter new contact name: ")
                contact["name"]=name
            elif contact_field==2:
                phone= input("Enter new contact phone number: ")
                contact['phone']=phone
            elif contact_field==3:
                email= input("Enter new contact email: ")
                contact['email']=contact_field
            else:
                print("Invalid contact field")

            save_contacts(contacts)
            print("Contact updated successfully")
            return

    print("Contact not found.")



