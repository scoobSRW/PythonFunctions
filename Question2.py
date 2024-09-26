shopping_list = []

def add_item(item):
    shopping_list.append(item)

def remove_item(item):
    try:
        shopping_list.remove(item)
        print(f"Removed '{item}' from the shopping list.")
    except ValueError:
        print(f"Item '{item}' not found in the shopping list.")

def print_list():
    if shopping_list:
        print("Shopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("Shopping list is empty.")

def shopping_list_maker():
    while True:
        action = input("Would you like to add, remove, print, or quit? ").lower()

        if action == 'add':
            item = input("Enter the item to add: ")
            add_item(item)
            print(f"Added '{item}' to the shopping list.")
        elif action == 'remove':
            item = input("Enter the item to remove: ")
            remove_item(item)
        elif action == 'print':
            print_list()
        elif action == 'quit':
            print("Exiting the shopping list maker.")
            break
        else:
            print("Invalid action. Please try again.")

shopping_list_maker()
