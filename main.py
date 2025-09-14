import load_contacts

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        load_contacts.add_contact()
    elif choice == "2":
        load_contacts.search_contact()
    elif choice == "3":
        load_contacts.delete_contact()
    elif choice == "4":
        print("Exiting Contact Book...")
        break
    else:
        print("Invalid choice. Try again.")
