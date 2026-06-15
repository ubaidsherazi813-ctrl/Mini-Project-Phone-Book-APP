phone_book = {}

while True:
    print("\n--- Phone Book ---")
    print("1. Add Contact")
    print("2. Lookup Contact")
    print("3. Delete Contact")
    print("4. View All Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        number = input("Enter phone number: ")

        phone_book[name] = number
        print("Contact added successfully!")

    elif choice == "2":
        name = input("Enter name to search: ")

        if name in phone_book:
            print(f"{name}: {phone_book[name]}")
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter name to delete: ")

        if name in phone_book:
            del phone_book[name]
            print("Contact deleted!")
        else:
            print("Contact not found!")

    elif choice == "4":
        if len(phone_book) == 0:
            print("Phone book is empty.")
        else:
            print("\nContacts:")
            for name, number in phone_book.items():
                print(name, ":", number)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")