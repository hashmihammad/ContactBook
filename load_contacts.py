import json

filename = "contacts.json"
contacts = {}

def load_contacts():
    global contacts
    try:
        with open(filename, "r") as f:
            contacts = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = {}

def save_contacts():
    global contacts
    with open(filename, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact():
    global contacts
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    save_contacts()
    print(f"{name} added successfully.")

def search_contact():
    global contacts
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def delete_contact():
    global contacts
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        save_contacts()
        print(f"{name} deleted successfully.")
    else:
        print("Contact not found.")

load_contacts()
