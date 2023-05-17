from item import Item
from inventory import Inventory
import os, platform, sys
from os import path
os.chdir(sys.path[0])

def autosave(inventory):
    filename = "inv.char"
    try:
        with open(filename, "w") as file:
            for item in inventory.items:
                file.write(f"{item.name},{item.description},{item.quantity}\n")
        print("\n")
    except IOError:
        print("Error saving the inventory.")

def load_inventory(inventory):
    filename = "inv.char"
    try:
        with open(filename, "r") as file:
            for line in file:
                item_data = line.strip().split(",")
                if len(item_data) == 3:
                    name, description, quantity = item_data
                    item = Item(name, description, quantity)
                    inventory.add_item(item)
        print("Inventory loaded successfully.")
    except IOError:
        print("Error loading the inventory.")

# Create an inventory
inventory = Inventory()

# Load the inventory from the saved file
load_inventory(inventory)


def clear():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

while True:
    print("\n1. Add new item\n2. Remove item\n3. Edit item\n4. Use Item\n5. Display inventory\n6. Exit\n")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        clear()
        name = input("Enter the name of the item: ")
        description = input("Enter the description of the item: ")
        quantity = inventory.check_input_int("Enter the quantity: ")
        inventory.add_new_item(name, description, int(quantity))
        print("Item added to the inventory.")
        autosave(inventory)

    elif choice == 2:
        clear()
        inventory.display_inventory()
        item_index = input("Enter the item to remove: ")
        clear()
        inventory.remove_item_by_index_or_name(item_index)
        autosave(inventory)

    elif choice == 3:
        clear()
        inventory.display_inventory()
        item_index = input("Enter the item to edit: ")
        inventory.edit_item_by_index_or_name(item_index)
        autosave(inventory)
        
    elif choice == 4:
        clear()
        inventory.display_inventory()
        item_index = input("Enter the item to use: ")
        clear()
        inventory.use_item(item_index)
        autosave(inventory)
    
    elif choice == 5:
        clear()
        inventory.display_inventory()

    elif choice == 6:
        break

    else:
        print("Invalid choice. Please try again.")