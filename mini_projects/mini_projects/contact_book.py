# mini_projects/contact_book.py
# 📒 Contact Book using functions

contacts = {}

def add_contact(name, phone):
    """Add a new contact to the book."""
    contacts[name] = phone
    print(f"Added {name} with number {phone}")

def view_contacts():
    """View all saved contacts."""
    if not contacts:
        print("No contacts saved yet.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def delete_contact(name):
    """Delete a contact by name."""
    if name in contacts:
        del contacts[name]
        print(f"Deleted contact: {name}")
    else:
        print(f"{name} not found in contacts.")

def main():
    while True:
        print("\n--- Contact Book ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            add_contact(name, phone)
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            name = input("Enter name to delete: ")
            delete_contact(name)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()

