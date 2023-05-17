class Item:
    def __init__(self, name, description, quantity):
        self.name = name
        self.description = description
        self.quantity = int(quantity)

    def __str__(self):
        return f"Item: {self.name}\nDescription: {self.description}\nQuantity: {self.quantity}\n"

    def edit_name(self, new_name):
        self.name = new_name

    def edit_description(self, new_description):
        self.description = new_description

    def edit_quantity(self, new_quantity):
        self.quantity = new_quantity