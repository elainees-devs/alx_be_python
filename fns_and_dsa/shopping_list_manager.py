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
           item = input("Enter the item to add")
           print(f"'{item}' has been added to your shopping list")
        elif choice == '2':
            #Prompt and remove an item
            item = input("Enter the item(s) to remove")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping_list:'")
            else:
                print(f"'{item}' not found")

        elif choice == '3':
            #Display the shopping list
            print("Your shopping list: ")
            
            for i, item in enumerate(shopping_list, item = 1):
                print(f"{i}.{item}")
        elif choice == '4':
            print('Goodbye!')
            break
        else:
            print("Invalid choice, please try again later.")