#ITEMS,quantity,
user_items = {}
def add_item(item, quantity):
    if item in user_items:
        user_items[item] += quantity
    else:
        user_items[item] = quantity
def remove_item(item, quantity):
    if item in user_items:
        if user_items[item] >= quantity:
            user_items[item] -= quantity
            if user_items[item] == 0:
                del user_items[item]
        else:
            print(f"Not enough {item} to remove.")
    else:
        print(f"{item} not found in inventory.")
def view_inventory():
    if not user_items:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for item, quantity in user_items.items():
            print(f"{item}: {quantity}")
def clear_inventory():
    user_items.clear()
    print("Inventory cleared.")
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Inventory")
        print("4. Clear Inventory")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(item, quantity)
            print(f"Added {quantity} of {item}.")
        elif choice == '2':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            remove_item(item, quantity)
        elif choice == '3':
            view_inventory()
        elif choice == '4':
            clear_inventory()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
