# Creating a Phone Book app Using Dictionary

phone_book = {}

while True:

    print("\n---Phone book app---")
    print("Enter: 1 for add contact")
    print("Enter: 2 for lookup contact")
    print("Enter: 3 for delete contact")
    print("Enter: 4 for update contact")
    print("Enter: 5 for view all contact")
    print("Enter: 6 for Quit")

    choice = input("Enter your choice: ")

    if choice == '1':

        name = input("Enter your name: ")
        number = int(input("Enter your phone number: "))

        phone_book[name] = number
        print("\nContact Successfully added!\n")

    elif choice == '2':

        name = input("Enter your name: ")

        if name in phone_book:
            print(f"{name}: {phone_book[name]}\n")

        else:
            print("\ncontact not found!\n")

    elif choice == '3':
        name  = input("Enter your name to delete: ")

        if name in phone_book:
            del phone_book[name]
            print("\nContact deleted\n")

        else:
            print("\ncontact not found!\n")
        
    elif choice == '4':
        name = input("Enter contact name: ")

        if name in phone_book:
            new_number = input("Enter new number: ")
            phone_book[name] = new_number
            print("\nContact updated!\n")
        else:
            print("\nContact not found!\n")

    elif choice == '5':
        if len(phone_book) == 0:
            print("\nPhone book is empty!\n")
        else:
            print("--- All COntacts ---")
            for name , number , in phone_book.items():
                print(f"\n{name} : {number}\n")

    elif choice == '6':
        print("GoodBye!")
        break

    else:
        print("Invalid number!")   
                        






