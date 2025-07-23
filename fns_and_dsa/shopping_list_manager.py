shopping_list = []

while True:
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
    def display_menu():
        choice = input("Enter your choice: ")

        if choice =='1':
            # Prompt and add an item
            pass
        elif choice == '2':
            #Prompt and remove an item
            pass
        elif choice == '3':
            #Display the shopping list
            pass
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print("Invalid choice, please try again later.")