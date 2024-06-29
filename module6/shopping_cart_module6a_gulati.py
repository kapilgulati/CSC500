"""
Step 4: Build the ShoppingCart class with the following data attributes and related methods.
Note: Some can be method stubs (empty methods) initially, to be completed in later steps

"""
from datetime import date

from item_to_purchase_module6a_gulati import ItemToPurchase

# Dynamic attribute for the ItemToPurchase
ITEM_DESCRIPTION_ATTR = "description"

# Format string global variable
FORMAT_STRING = "{label:^75}"


class ShoppingCart:

    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        """
        Parameterized default constructor, has the following data attributes:
        customer_name (string)
        current_date (string)
        cart_items (list)
        :param customer_name: string, Initialized in default constructor to "none"
        :param current_date: string, Initialized in default constructor to "January 1, 2020"

        """
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def _find_item_by_name(self, item_name):
        """
        This private method iterates over the cart items and returns the index of an item for a given item name value.
        :param item_name: string
            name value of the item
        :return: int
            index of the item matching the given name value, returns "-1" if not found
        """
        item_to_purchase: ItemToPurchase
        for pos, item_to_purchase in enumerate(self.cart_items):
            if item_to_purchase.item_name == item_name:
                return pos
        return -1  # indicates not found

    def get_cart_title(self):
        """
        This method returns the concatenated string value of the customer name and current date
        :return: string = concatenated value
        """
        return f"{self.customer_name} - {self.current_date}"

    def add_item(self, item_to_purchase):
        """
        Adds an item to the cart_items list.
        :param item_to_purchase: ItemToPurchase
            Object of type ItemToPurchase
        :return: Does not return anything
        """
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        """
        Removes an item from the cart_items list that matches the given item name value. If the item name
        cannot be found, it outputs this message: "Item not found in cart. Nothing removed."
        :param item_name: string
            Item name value
        :return: Does not return anything.
        """
        item_index = self._find_item_by_name(item_name)
        if item_index >= 0:
            self.cart_items.pop(self.cart_items.index(item_index))
            # print(f"Item removed from cart: {item_name}")
        else:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase: ItemToPurchase):
        """
        Modifies an item's description, price, and/ or quantity of cart item that matches the given item name value.
        If an item can be found (by name) in the cart, it checks if matching item attributes have default values for
        description, price, and quantity. If not, then modify the item in the cart. If an item cannot be found (by name)
        in the cart, output this message: "Item not found in the cart. Nothing modified."
        :param item_to_purchase: ItemToPurchase
        :return: Does not return anything.
        """
        item_index = self._find_item_by_name(item_to_purchase.item_name)
        if 0 <= item_index < len(self.cart_items):
            if not item_to_purchase.has_default_values(ITEM_DESCRIPTION_ATTR):
                self.cart_items[item_index] = item_to_purchase
        else:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        """
        Returns quantity of all items in cart
        :return: int = number of items in cart
        """
        cart_quantity = 0
        item_to_purchase: ItemToPurchase
        for item_to_purchase in self.cart_items:
            cart_quantity += item_to_purchase.item_quantity
        return cart_quantity

    def get_cost_of_cart(self):
        """
        Determines and returns the total cost of items in the cart. If there are no items in the cart, then returns 0.0
        :return: float = total cost of items in cart
        """
        cart_total = 0.0
        item_to_purchase: ItemToPurchase
        for item_to_purchase in self.cart_items:
            cart_total += item_to_purchase.item_price * item_to_purchase.item_quantity
        return cart_total

    def print_total(self):
        """
        Displays Cart title, number of items in the cart, content of the cart and total cost of items in cart
        If cart is empty, outputs this message: "SHOPPING CART IS EMPTY".
        :return: Does not return anything.
        """
        if len(self.cart_items) > 0:
            print(FORMAT_STRING.format(label="OUTPUT SHOPPING CART"))
            print(FORMAT_STRING.format(label=self.get_cart_title()))
            print(FORMAT_STRING.format(label=f"Number of Items: {self.get_num_items_in_cart()}"))
            c_item: ItemToPurchase
            for c_item in self.cart_items:
                print(FORMAT_STRING.format(label=c_item.print_item_cost()))
            print(FORMAT_STRING.format(label=f"Total: ${self.get_cost_of_cart()}"))
        else:
            print("SHOPPING CART IS EMPTY")

    def print_descriptions(self):
        """
        Outputs/displays cart title and each item's description in the cart
        :return: Does not return anything
        """
        print(FORMAT_STRING.format(label="OUTPUT ITEMS' DESCRIPTIONS"))
        print(FORMAT_STRING.format(label=self.get_cart_title()))
        print(FORMAT_STRING.format(label="Item Descriptions"))
        cart_item: ItemToPurchase
        for cart_item in self.cart_items:
            print(FORMAT_STRING.format(label=f"{cart_item.item_name}: {getattr(cart_item, ITEM_DESCRIPTION_ATTR)}"))


def print_menu():
    print(FORMAT_STRING.format(label="MENU"))
    print(FORMAT_STRING.format(label="a - Add item to cart"))
    print(FORMAT_STRING.format(label="r - Remove item from cart"))
    print(FORMAT_STRING.format(label="c - Change item quantity"))
    print(FORMAT_STRING.format(label="i - Output items' descriptions"))
    print(FORMAT_STRING.format(label="o - Output shopping cart"))
    print(FORMAT_STRING.format(label="q - Quit"))


def get_string_input(user_input, error_message):
    while True:
        try:
            user_input_str = user_input
            if len(user_input_str.strip()) == 0:
                raise ValueError
            break
        except:
            user_input = input(f"{error_message}, try again: ")
    return user_input_str


def get_float_input(user_input, error_message):
    while True:
        try:
            user_input_float = float(user_input)
            if user_input_float <= 0:
                raise ValueError
            break
        except:
            user_input = input(f"{error_message}, try again: ")
    return user_input_float


def get_integer_input(user_input, error_message):
    while True:
        try:
            user_input_int = int(user_input)
            if user_input_int <= 0:
                raise ValueError
            break
        except:
            user_input = input(f"{error_message}, try again: ")
    return user_input_int


def main():
    # ask to enter customer name
    customer_name = get_string_input(input("Enter customer name: "), "Invalid customer name")
    transaction_date = date.today().strftime("%B %d, %Y")

    # prime the cart with sample data
    shopping_cart = ShoppingCart(customer_name, transaction_date)

    # infinite loop, print menu and ask user to select a menu option
    while True:
        print_menu()
        selected_menu = input("Choose an option:")
        if selected_menu == 'q':
            # quit loop
            break
        elif selected_menu == "i":
            # output cart description
            shopping_cart.print_descriptions()
            print("\n")
        elif selected_menu == "o":
            # output cart totals
            shopping_cart.print_total()
            print("\n")
        elif selected_menu == "a":
            # output cart totals
            item_name = get_string_input(input("Enter item name: "), "Invalid item name")
            item_description = get_string_input(input("Enter item description: "), "Invalid item description")
            item_price = get_float_input(input("Enter item price: "), "Invalid item price")
            item_quantity = get_integer_input(input("Enter item quantity: "), "Invalid item quantity")
            item = ItemToPurchase(item_name, item_price, item_quantity)
            setattr(item, "description", item_description)
            shopping_cart.add_item(item)
            print("\n")
        elif selected_menu in ['r', 'c']:
            print(FORMAT_STRING.format(label="Menu option not supported try q, i , a or o option"))
            print("\n")
        else:
            print(FORMAT_STRING.format(label="Enter a valid menu option"))
            print("\n")


# Tests class implementation
if __name__ == "__main__":
    main()
