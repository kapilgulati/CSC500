"""
Module 8: Portfolio Project
Online Shopping Cart

The project solution consists of two classes:
Items to Purchase
    has attributes to describe an item
    methods to display item information

Shopping Cart
    has attributes to describe customer to whom this cart belongs to
    list attributed ( one-to-many relationship) for Items to Purchase
    methods to mutate the cart items
    methods to display cart contents

In addition, the solution will have main method and convenience methods to simulate online experience

"""
from datetime import date
from typing import List, Any

# Format string global variable
FORMAT_STRING = "{label:^50}"


"""
===========================================
Class definition: ItemToPurchase.
===========================================
"""


class ItemToPurchase:
    """
    Item to purchase class that represents an item model
    """

    # class attributes - used as default values
    default_item_name = "none"
    default_item_price = 0.0
    default_item_quantity = 0
    default_item_description = ""

    def __init__(
        self,
        item_name=default_item_name,
        item_price=default_item_price,
        item_quantity=default_item_quantity,
        item_description=default_item_description,
    ):
        """
        default constructor for ItemToPurchase.
        :param item_name: String - defaults to "none"
        :param item_price: float - defaults to 0.0
        :param item_quantity: integer - defaults to 0
        :param item_description: String - defaults to empty string
        """
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

    def calculate_cost(self):
        return self.item_price * self.item_quantity

    def print_item_cost(self):
        """
        Displays item cost using the format "name quantity @ $price = $total"
        :return: does not return anything
        """
        # format using positional replacement
        print(
            FORMAT_STRING.format(
                label="{0} {1} @ ${2:.2f} = ${3:.2f}".format(
                    self.item_name,
                    self.item_quantity,
                    self.item_price,
                    (self.calculate_cost()),
                )
            )
        )

    def print_item_description(self):
        """
        Displays item description using the format "name: description"
        :return: does not return anything
        """
        # format using inferred positional replacement
        print(
            FORMAT_STRING.format(
                label="{}: {}".format(self.item_name, self.item_description)
            )
        )


"""
===========================================
Class definition: ShoppingCart.
===========================================
"""


class ShoppingCart:
    """
    ShoppingCart class that represents a virtual shopping cart model
    """

    def __init__(
        self, customer_name="none", current_date="January 1, 2020", cart_items=None
    ):
        """
        Parameterized default constructor, has the following data attributes:
        customer_name string)
        current_date (string)
        cart_items (list)
        :param customer_name: string, Initialized in default constructor to "none"
        :param current_date: string, Initialized in default constructor to "January 1, 2020"

        """
        self.customer_name = customer_name
        self.current_date = current_date
        # If cart item is provided as parameter then use it otherwise initialize to empty list
        self.cart_items = list() if cart_items is None else cart_items

    def __find_item_by_name(self, item_name):
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

    def add_item(self, item_to_purchase):
        """
        This method adds the given item to purchase in the cart_items list.
        :param item_to_purchase: ItemToPurchase
            Object of type ItemToPurchase
        :return: no value is returned
        """
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        """
        This method will iterate list of cart items, for each item in the cart it compares the given item name with cart
        item's name and removes the matching item. If no match was found, then it prints a message
        "Item not found in cart. Nothing removed."
        :param item_name: string
            Item name value
        :return: no value is returned
        """
        item_index = self.__find_item_by_name(item_name)
        if item_index >= 0:
            self.cart_items.pop(item_index)
            # print(f"Item removed from cart: {item_name}")
        else:
            print("Item not found in cart. Nothing removed.")

    def modify_item(self, item_to_purchase: ItemToPurchase):
        """
        This method first checks the given item to purchase has default values for description, price and quantity,
        if no then it calls __find_item_by_name() to find a matching item in the cart.
        If a match is found, it updates the matching item's description, price, and/ or quantity with the given values.
        If no match is found, then it output this message: "Item not found in the cart. Nothing modified."
        :param item_to_purchase: ItemToPurchase
        :return: no value is returned.
        """

        item_index = self.__find_item_by_name(item_to_purchase.item_name)

        if item_index != -1:
            if (
                item_to_purchase.item_description
                != ItemToPurchase.default_item_description
            ):
                self.cart_items[
                    item_index
                ].item_description = item_to_purchase.item_description

            if item_to_purchase.item_quantity != ItemToPurchase.default_item_quantity:
                self.cart_items[
                    item_index
                ].item_quantity = item_to_purchase.item_quantity
            if item_to_purchase.item_price != ItemToPurchase.default_item_price:
                self.cart_items[item_index].item_price = item_to_purchase.item_price
        else:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        """
        Iterates cart items and returns the total number of items in cart.
        :return: int = total quantity of all items in the cart
        """
        cart_quantity = 0
        item_to_purchase: ItemToPurchase
        for item_to_purchase in self.cart_items:
            cart_quantity += item_to_purchase.item_quantity
        return cart_quantity

    def get_cost_of_cart(self):
        """
        Iterates cart items, calculates cost by multiplying quantity and price of each item,
        returns the total for the cart. If there are no items in the cart, then returns 0.0
        :return: float = total cost of items in cart
        """
        cart_total = 0.0
        item_to_purchase: ItemToPurchase
        for item_to_purchase in self.cart_items:
            cart_total += item_to_purchase.calculate_cost()
        return cart_total

    def print_total(self):
        """
        This method displays:
         Cart title by concatenating customer name and date,
         number of items in the cart by calling get_num_items_in_cart() method of the ShoppingCart,
         content of the cart by iterating through the cart items, and calling print_item_cost() method of ItemToPurchase
         and total cost of items in cart by calling get_cost_of_cart() method of the ShoppingCart
        If cart is empty, outputs this message: "SHOPPING CART IS EMPTY".
        :return: Does not return anything.
        """
        if len(self.cart_items) > 0:
            print(FORMAT_STRING.format(label="OUTPUT SHOPPING CART"))
            print(
                FORMAT_STRING.format(
                    label=f"{self.customer_name}'s Shopping Cart - {self.current_date}"
                )
            )
            print(
                FORMAT_STRING.format(
                    label=f"Number of Items: {self.get_num_items_in_cart()}"
                )
            )
            c_item: ItemToPurchase
            for c_item in self.cart_items:
                c_item.print_item_cost()
            print(
                FORMAT_STRING.format(
                    label="Total: ${:.2f}".format(self.get_cost_of_cart())
                )
            )
        else:
            print("SHOPPING CART IS EMPTY")

    def print_descriptions(self):
        """
        Outputs/displays cart title and each item's description in the cart
        :return: Does not return anything
        """
        print(FORMAT_STRING.format(label="OUTPUT ITEMS' DESCRIPTIONS"))
        print(
            FORMAT_STRING.format(
                label=f"{self.customer_name}'s Shopping Cart - {self.current_date}"
            )
        )
        print(FORMAT_STRING.format(label="Item Descriptions"))
        cart_item: ItemToPurchase
        for cart_item in self.cart_items:
            cart_item.print_item_description()


"""
===========================================
Convenience functions to validate user input.
===========================================
"""


def get_string_input(user_input_prompt, format_prompt=True):
    while True:
        if format_prompt:
            user_input_str = input(
                FORMAT_STRING.format(label=f"{user_input_prompt}\n{chr(187)} ")
            )
        else:
            user_input_str = input(f"{user_input_prompt}\n{chr(187)} ")

        if len(user_input_str.strip()) == 0:
            print("invalid input, try again...")
        else:
            return user_input_str


def get_float_input(user_input_prompt):
    while True:
        try:
            user_input_float = float(
                input(FORMAT_STRING.format(label=f"{user_input_prompt}\n{chr(187)} "))
            )
            if user_input_float <= 0:
                raise ValueError
            break
        except:
            print("invalid input, try again...")

    return user_input_float


def get_int_input(user_input_prompt):
    while True:
        try:
            user_input_float = int(
                input(FORMAT_STRING.format(label=f"{user_input_prompt}\n{chr(187)} "))
            )
            if user_input_float <= 0:
                raise ValueError
            break
        except:
            print("invalid input, try again...")

    return user_input_float


"""
===========================================
Function to prompt menu
===========================================
"""


def print_menu(shopping_cart: ShoppingCart):
    show_menu = True

    def menu():
        print(FORMAT_STRING.format(label="MENU"))
        print(FORMAT_STRING.format(label="a - Add item to cart"))
        print(FORMAT_STRING.format(label="r - Remove item from cart"))
        print(FORMAT_STRING.format(label="c - Change item quantity"))
        print(FORMAT_STRING.format(label="i - Output items' descriptions"))
        print(FORMAT_STRING.format(label="o - Output shopping cart"))
        print(FORMAT_STRING.format(label="q - Quit"))

    while True:
        if show_menu:
            menu()
            show_menu = False

        selected_menu = get_string_input(f"Choose an option:")
        if selected_menu == "q":
            print(FORMAT_STRING.format(label="QUIT"))
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
            print(FORMAT_STRING.format(label="ADD ITEM TO CART"))
            # ask user to enter an item, then add the item to the cart
            item_name = get_string_input("Enter item name:")
            item_description = get_string_input("Enter the item description:")
            item_price = get_float_input("Enter the item price:")
            item_quantity = get_int_input("Enter the item quantity:")
            shopping_cart.add_item(
                ItemToPurchase(item_name, item_price, item_quantity, item_description)
            )
            print("Item added to cart.\n")
        elif selected_menu == "r":
            print(FORMAT_STRING.format(label="REMOVE ITEM FROM CART"))
            # remove item
            item_to_remove = get_string_input("Enter name of item to remove:")
            shopping_cart.remove_item(item_to_remove)
            print("\n")
        elif selected_menu == "c":
            # change quantity
            print(FORMAT_STRING.format(label="CHANGE ITEM QUANTITY"))
            item_name = get_string_input("Enter the item name:")
            item_quantity = get_int_input("Enter the new quantity:")
            shopping_cart.modify_item(
                ItemToPurchase(item_name=item_name, item_quantity=item_quantity)
            )
            print("\n")
        elif selected_menu == "m":
            # show menu
            show_menu = True
        else:
            print(FORMAT_STRING.format(label="Enter a valid menu option"))
            print("\n")


"""
===========================================
Main method
===========================================
"""


def main():
    # Milestone #1 needs formatting
    # items_to_purchase = [prompt_item_to_purchase(), prompt_item_to_purchase()]
    # total_cost = 0
    # print(FORMAT_STRING.format(label="TOTAL COST"))
    # for item_to_purchase in items_to_purchase:
    #     total_cost = total_cost + item_to_purchase.calculate_cost()
    #     item_to_purchase.print_item_cost()
    # print(FORMAT_STRING.format(label=f"Total: ${total_cost:.2f}"))
    # Milestone #2 needs formatting
    # prompt for customer name
    customer_name = get_string_input("Enter customer's name: ", False)
    current_date = date.today().strftime("%B %d, %Y")
    cart_date = get_string_input(f"Enter today's date (ex {current_date}): ", False)

    shopping_cart = ShoppingCart(customer_name, cart_date)
    print_menu(shopping_cart)


if __name__ == "__main__":
    main()
