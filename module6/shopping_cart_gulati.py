"""
Step 4: Build the ShoppingCart class with the following data attributes and related methods. Note: Some can be method stubs (empty methods) initially, to be completed in later steps

Parameterized constructor, which takes the customer name and date as parameters
Attributes
customer_name (string) - Initialized in default constructor to "none"
current_date (string) - Initialized in default constructor to "January 1, 2020"
cart_items (list)

"""
from item_to_purchase_gulati import ItemToPurchase


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def _find_item_by_name(self, item_name):
        item_to_purchase: ItemToPurchase
        for pos, item_to_purchase in enumerate(self.cart_items):
            if item_to_purchase.item_name == item_name:
                return pos
        return -1  # indicates not found

    def print_cart_title(self):
        print(f"{self.customer_name} - {self.current_date}")

    # Adds an item to cart_items list. Has parameter ItemToPurchase. Does not return anything.
    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    # Removes item from cart_items list. Has a string (an item's name) parameter. Does not return anything.
    # If item name cannot be found, output this message: Item not found in cart. Nothing removed.
    def remove_item(self, item_name):
        item_index = self._find_item_by_name(item_name)
        if item_index >= 0:
            item = self.cart_items.pop(self.cart_items.index(item_index))
        else:
            print("Item not found in cart. Nothing removed.")

    # Modifies an item's description, price, and/or quantity. Has parameter ItemToPurchase. Does not return anything.
    # If item can be found (by name) in cart, check if parameter has default values for
    # description, price, and quantity. If not, modify item in cart.
    # If item cannot be found (by name) in cart, output this message: Item not found in cart. Nothing modified.
    def modify_item(self, item_to_purchase: ItemToPurchase):
        item_index = self._find_item_by_name(item_to_purchase.item_name)
        if 0 <= item_index < len(self.cart_items):
            if not item_to_purchase.has_default_values():
                # Fixme
                print(self.cart_items[item_index])
                self.cart_items[item_index] = item_to_purchase
        else:
            print("Item not found in cart. Nothing modified.")

    # Returns quantity of all items in cart. Has no parameters.
    def get_num_items_in_cart(self):
        cart_quantity = 0
        item_to_purchase: ItemToPurchase
        for item_to_purchase in self.cart_items:
            cart_quantity += item_to_purchase.item_quantity
        return cart_quantity

    # Determines and returns the total cost of items in cart. Has no parameters.
    def get_cost_of_cart(self):
        cart_total = 0
        item_to_purchase: ItemToPurchase
        for item_to_purchase in self.cart_items:
            cart_total += item_to_purchase.item_price * item_to_purchase.item_quantity
        return cart_total

    # Outputs total of objects in cart.
    # If cart is empty, output this message: SHOPPING CART IS EMPTY
    def print_total(self):
        if len(self.cart_items) > 0:
            self.print_cart_title()
            print(f"Number of Items: {self.get_num_items_in_cart()}")
            c_item: ItemToPurchase
            for c_item in self.cart_items:
                c_item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart()}")

        else:
            print("SHOPPING CART IS EMPTY")

    # print_descriptions()
    # Outputs each item's description.
    def print_descriptions(self):
        cart_item: ItemToPurchase
        self.print_cart_title()
        print("Item Descriptions")
        for cart_item in self.cart_items:
            print(f"{cart_item.item_name}: {cart_item.__getattribute__('description')}")


if __name__ == "__main__":
    shopping_cart = ShoppingCart("John Doe's Shopping Cart", "February 1, 2020")
    item = ItemToPurchase("Nike Romaleos", 189, 2)
    item.__setattr__("description", "Volt color, Weightlifting shoes")
    shopping_cart.add_item(item)
    item = ItemToPurchase("Chocolate Chips", 3, 5)
    item.__setattr__("description", "Semi-sweet")
    shopping_cart.add_item(item)
    item = ItemToPurchase("Powerbeats 2 Headphones", 128, 1)
    item.__setattr__("description", "Bluetooth headphones")
    shopping_cart.add_item(item)
    shopping_cart.print_total()
    shopping_cart.print_descriptions()
