def print_menu():
    print("1. Print all the Contacts")
    print("2. Add a Contact")
    print("3. Remove a Contact")
    print("4. Lookup a Contact")
    print("5. Quit the program")
    print()

emailid = {}
numbers = {}
birthday = {}
menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        print("All contacts in your contact book are:")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x], "\temail id :",emailid[x], "\tBirthday :",birthday[x])
        print()
    elif menu_choice == 2:
        print("Add Name, Number, E-Mail ID and Birthday")
        name = input("Name: ")
        phone = input("Number: ")
        phone1 = input("email id: ")
        phone2 = input("Birthday: ")
        numbers[name] = phone
        emailid[name] = phone1
        birthday[name] = phone2
    elif menu_choice == 3:
        print("Remove Name and Number from your contacts")
        name = input("Name: ")
        if name in numbers:
            del numbers[name]
        else:
            print(name, "was not found")
    elif menu_choice == 4:
        print("Search for a number")
        name = input("Name: ")
        if name in numbers:
            print("The number is", numbers[name])
        else:
            print(name, "was not found")
    elif menu_choice != 5:
        print_menu()