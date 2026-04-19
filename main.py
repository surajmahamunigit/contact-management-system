from file_handler import save_contacts
from contact_manager import add_contacts, view_contacts, search_contacts, delete_contact
from file_handler import load_contacts, save_contacts


def display_menu():
    print("Welcome to Contact Management System:")
    print("1. Add contacts")
    print("2. View contacts")
    print("3. Search contact:")
    print("4. Delete contact")
    print("5. Save contact")
    print("6. Exit")





def main():
    """Main Application"""

    # Load all the contacts when Application starts
    contacts=load_contacts()

    while True:
        display_menu()

        option=input("Enter your choice:").lower().strip()

        if option == "1":
            add_contacts(contacts)
        elif option == "2":
            view_contacts(contacts)
        elif option == "3":
            search_contacts(contacts)
        elif option == "4":
            delete_contact(contacts)
        elif option == "5":
            save_contacts(contacts)
        elif option == "6":
            save_contacts(contacts)
            print("Exiting th application...")
            break
        else:
            print("Invalid option")




if __name__ == "__main__":
    main()