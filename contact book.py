import json
Contact_FILE = "contact.json"

def load_contacts():
    try:
        with open(Contact_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def add_contact():
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    save_contact(contacts)
    print(f" Contact '{name}' added successfully!")

def save_contact(contacts):
    with open(Contact_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

def view_contacts():
    if not contacts:
        print(" No contacts found.")
    else:
        print("\n Contact List:")
        for idx, contact in enumerate(contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}-{contact['email']}-{contact['address']}")

def search_contact():
    query = input("Enter name or phone number to search: ").strip().lower()
    found_contacts = [c for c in contacts if query in c["name"].lower() or query in c["phone"]]

    if found_contacts:
        print("\n Search Results:")
        for idx, contact in enumerate(found_contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}-{contact['email']}-{contact['address']}")
    else:
        print(" No matching contacts found.")


def update_contact():
    view_contacts()
    name_to_update = input("Enter the contact name to update: ").strip().lower()

    for contact in contacts:
        if contact["name"].lower() == name_to_update:
            print(f"Editing Contact: {contact['name']}")

            contact['name'] = input("Enter new name (leave blank to keep current): ") or contact['name']
            contact['phone'] = input("Enter new phone (leave blank to keep current): ") or contact['phone']
            contact['email'] = input("Enter new email (leave blank to keep current): ") or contact['email']
            contact['address'] = input("Enter new address (leave blank to keep current): ") or contact['address']

            save_contact(contacts)
            print(" Contact updated successfully!")

            return


    print("⚠ Contact not found.")

def delete_contact():
    view_contacts()
    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            deleted = contacts.pop(index)
            save_contact(contacts)
            print(f"🗑 Contact '{deleted['name']}' deleted successfully!")
        else:
            print(" Invalid contact number.")
    except ValueError:
        print(" Please enter a valid number.")

contacts = load_contacts()

while True:
    print("\n Contact Manager")
    print("[1] Add Contact  [2] View Contacts  [3] Search Contact  [4] Update Contact  [5] Delete Contact  [6] Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print(" Your contacts are saved!")
        break
    else:
        print("Invalid choice, try again.")