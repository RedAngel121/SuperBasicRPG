from item import Item

class Inventory:
    def __init__(self):
        self.items = []

    def convert(self, number):
        try: 
            return int(number)
        except: 
            return str(number)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def display_inventory(self):
        if self.items == []:
            print("You have nothing in your inventory!\n")
        else:
            print("Inventory:\n")
            for i, item in enumerate(self.items, 1):
                print(f"#{i} {item}")

    def edit_item(self, item_index, new_name, new_description, new_quantity):
        item = self.items[item_index]
        item.edit_name(new_name)
        item.edit_description(new_description)
        item.edit_quantity(new_quantity)

    def edit_item_by_index_or_name(self, item_index):
        item_index = self.convert(item_index)
        if isinstance(item_index, str):
            found_item = None
            for index, item in enumerate(self.items):
                if item.name == item_index:
                    found_item = item
                    break
            if found_item:
                print(f"Editing item #{index+1}: {found_item.name}")
                new_name = input("Enter the new name: ")
                new_description = input("Enter the new description: ")
                new_quantity = self.check_input_int("Enter the quantity: ")
                self.edit_item(index, new_name, new_description, new_quantity)
                print(f"Item '{found_item.name}' edited successfully.")
            else:
                print("Item not found in the inventory.")
        elif isinstance(item_index, int) and 0 <= item_index < len(self.items)+1:
            item_index -= 1
            item = self.items[item_index]
            print(f"Editing item #{item_index+1}: {item.name}")
            new_name = input("Enter the new name: ")
            new_description = input("Enter the new description: ")
            new_quantity = self.check_input_int("Enter the quantity: ")
            self.edit_item(item_index, new_name, new_description, new_quantity)
            print(f"Item #{item_index+1} edited successfully.")
        else:
            print("Invalid item index.")

    def add_new_item(self, name, description, quantity):
        item = Item(name, description, int(quantity))
        for existing_item in self.items:
            if existing_item.name == item.name:
                existing_item.quantity += item.quantity
                return
        self.items.append(item)

    def remove_item_by_index_or_name(self, item_index):
        intcheck = self.convert(item_index)
        if isinstance(intcheck, int) and intcheck >= 0 and intcheck < len(self.items)+1:
            intcheck -= 1
            item = self.items[intcheck]
            self.remove_item(item)
            print(f"Item '{item.name}' removed from inventory.")
        elif isinstance(item_index, str):
            for item in self.items:
                if item.name == str(item_index):
                    self.items.remove(item)
                    print(f"Item '{item.name}' removed from inventory.")
                    return True
        else:
            print("Item does not exist.")
            return False

    def use_item(self, item_index):
        intcheck = self.convert(item_index)
        if isinstance(intcheck, int) and intcheck >= 0 and intcheck < len(self.items)+1:
            intcheck -= 1
            item = self.items[intcheck]
            item.quantity -= 1
            print(f"Item '{item.name}' has been used.")
            if item.quantity < 1:
                self.remove_item(item)
                print(f"Item removed because it hit '{str(item.quantity)}'")
        elif isinstance(item_index, str):
            for item in self.items:
                if item.name == str(item_index):
                    item.quantity -= 1
                    print(f"Item '{item.name}' has been used.")
                    if item.quantity < 1:
                        self.remove_item(item)
                        print(f"Item removed because it hit '{str(item.quantity)}'")
        else:
            print("Item does not exist.")
            return False

    def check_input_int(self, prompt):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("A number is required.")

