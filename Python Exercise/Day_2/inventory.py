print("Welcome to the inventory management system")
print("Options")
print("1. Add item: Type add 'item_name' to add to item")
print("2. Remove item: Type 'remove item_name' to remove an item")
print("3. Show Inventory: Type 'show' to show all inventory")
li = []
while(True):
    text = input("Enter your option").split(" ")
    if len(text) == 2:
        item = text[1]
    command = text[0]
    if command == 'add':
        li.append(item)
    elif command == 'remove':
        #check if item is in the list
        if item in li:
            li.remove(item)
        else:
            print("No such item in inventory")
    elif command == 'show':
        print("List of Items")
        print(li)
    else:
        print("No such command")

