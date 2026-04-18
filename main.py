from file_handler import save_contacts
from file_handler import load_contacts, save_contacts


def display_menu():
    print("Welcome to Contact Management System:")
    print("1. Load contacts")
    print("2. View contacts")
    print("3. Exit")





def main():
    """Main Application"""

    # Load all the contacts when Application starts
    contacts=load_contacts()
    while True:
        display_menu()

        option=input("Enter your choice:").lower().strip()

        if option == "1":
            load_contacts()
        elif option == "2":
            save_contacts(contacts)
        elif option == "3":
            save_contacts(contacts)
            print("Exiting th application...")
            break
        else:
            print("Invalid option")




if __name__ == "__main__":
    main()