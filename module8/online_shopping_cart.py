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

# Format string global variable
FRMT_STR = "{label:^50}"


def format_output(label_str):
    """
    Formats the string to be printed on the console.
    :param label_str: string value to be printed
    :return:
    """
    return FRMT_STR.format(label=label_str)


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
            format_output(
                "{0} {1} @ ${2:.2f} = ${3:.2f}".format(
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
        print(format_output("{}: {}".format(self.item_name, self.item_description)))


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
        self,
        customer_name="none",
        current_date="January 1, 2020",
        cart_items: list[ItemToPurchase] = None,
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

        for pos, item_to_purchase in enumerate(self.cart_items):
            if item_to_purchase.item_name == item_name:
                return pos
        return -1  # indicates not found

    def add_item(self, item_to_purchase):
        """
        This method adds the given item to purchase in the cart_items list.
        :param item_to_purchase: Object of type ItemToPurchase
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
            print(format_output("Item not found in cart. Nothing removed."))

    def modify_item(self, item_to_purchase):
        """
        This method first checks the given item to purchase has default values for description, price and quantity,
        if no then it calls __find_item_by_name() to find a matching item in the cart.
        If a match is found, it updates the matching item's description, price, and/ or quantity with the given values.
        If no match is found, then it output this message: "Item not found in the cart. Nothing modified."
        :param item_to_purchase: Object of type ItemToPurchase
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
            print(format_output("Item not found in cart. Nothing modified."))

    def get_num_items_in_cart(self):
        """
        Iterates cart items and returns the total number of items in cart.
        :return: int = total quantity of all items in the cart
        """
        cart_quantity = 0
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
            print(format_output("OUTPUT SHOPPING CART"))
            print(
                format_output(
                    f"{self.customer_name}'s Shopping Cart - {self.current_date}"
                )
            )
            print(format_output(f"Number of Items: {self.get_num_items_in_cart()}"))
            c_item: ItemToPurchase
            for c_item in self.cart_items:
                c_item.print_item_cost()
            print(format_output("Total: ${:.2f}".format(self.get_cost_of_cart())))
        else:
            print("SHOPPING CART IS EMPTY")

    def print_descriptions(self):
        """
        Outputs/displays cart title and each item's description in the cart
        :return: Does not return anything
        """
        print(format_output("OUTPUT ITEMS' DESCRIPTIONS"))
        print(
            format_output(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        )
        print(format_output("Item Descriptions"))
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
            print(format_output(f"{user_input_prompt}"))
            user_input = input(f"{chr(187)}\t")
        else:
            user_input = input(f"{user_input_prompt}\n{chr(187)} ")

        if len(user_input.strip()) == 0:
            print(format_output("invalid input, try again..."))
        else:
            return user_input


def get_float_input(user_input_prompt, format_prompt=True):
    while True:
        try:
            if format_prompt:
                print(format_output(f"{user_input_prompt}"))
                user_input = float(input(f"{chr(187)}\t"))
            else:
                user_input = float(input(f"{user_input_prompt}\n{chr(187)} "))
            if user_input <= 0:
                raise ValueError
            break
        except:
            print(format_output("invalid input, try again..."))
    return user_input


def get_int_input(user_input_prompt, format_prompt=True):
    while True:
        try:
            if format_prompt:
                print(format_output(f"{user_input_prompt}"))
                user_input = int(input(f"{chr(187)}\t"))
            else:
                user_input = int(input(f"{user_input_prompt}\n{chr(187)} "))
            if user_input <= 0:
                raise ValueError
            break
        except:
            print(format_output("invalid input, try again..."))
    return user_input


"""
===========================================
Function to prompt menu
===========================================
"""


def print_menu(shopping_cart: ShoppingCart):
    show_menu = True

    # while customer exits using the q command
    while True:
        # only show menu if it is the first run of the loop or if customer enters 'm'
        if show_menu:
            print(format_output("MENU"))
            print(format_output("a - Add item to cart"))
            print(format_output("r - Remove item from cart"))
            print(format_output("c - Change item quantity"))
            print(format_output("i - Output items' descriptions"))
            print(format_output("o - Output shopping cart"))
            print(format_output("q - Quit"))
            show_menu = False

        selected_menu = get_string_input(f"Choose an option:")
        if selected_menu == "q":
            print(format_output("QUIT"))
            # quit loop
            break
        elif selected_menu == "i":
            # output cart description
            shopping_cart.print_descriptions()
            print(
                format_output("Enter a menu option, or press 'm' to see menu again.\n")
            )
        elif selected_menu == "o":
            # output cart totals
            shopping_cart.print_total()
            print(
                format_output("Enter a menu option, or press 'm' to see menu again.\n")
            )
        elif selected_menu == "a":
            print(format_output("ADD ITEM TO CART"))
            # ask user to enter an item, then add the item to the cart
            item_name = get_string_input("Enter item name:")
            item_description = get_string_input("Enter the item description:")
            item_price = get_float_input("Enter the item price:")
            item_quantity = get_int_input("Enter the item quantity:")
            shopping_cart.add_item(
                ItemToPurchase(item_name, item_price, item_quantity, item_description)
            )
            print(
                format_output(
                    "Item added to cart. Enter a menu option, or press 'm' to see menu again.\n"
                )
            )
        elif selected_menu == "r":
            print(format_output("REMOVE ITEM FROM CART"))
            # remove item
            item_to_remove = get_string_input("Enter name of item to remove:")
            shopping_cart.remove_item(item_to_remove)
            print(
                format_output("Enter a menu option, or press 'm' to see menu again.\n")
            )
        elif selected_menu == "c":
            # change quantity
            print(format_output("CHANGE ITEM QUANTITY"))
            item_name = get_string_input("Enter the item name:")
            item_quantity = get_int_input("Enter the new quantity:")
            shopping_cart.modify_item(
                ItemToPurchase(item_name=item_name, item_quantity=item_quantity)
            )
            print(
                format_output("Enter a menu option, or press 'm' to see menu again.\n")
            )
        elif selected_menu == "m":
            # show menu
            show_menu = True
        else:
            print(
                format_output(
                    "Enter a valid menu option, or press 'm' to see menu again.\n"
                )
            )
            print("\n")


"""
===========================================
Main method
===========================================
"""


def main():
    # ask to enter customer's name
    customer_name = get_string_input("Enter customer's name: ")
    example_date = date.today().strftime("%B %d, %Y")
    # ask to enter today's date
    current_date = get_string_input(f"Enter today's date (ex. {example_date}): ")
    # Output customer name and date
    print(format_output(f"Customer name: {customer_name}"))
    print(format_output(f"Today's date: {current_date}"))
    print(format_output("=" * 30))
    # initialize shopping cart object
    shopping_cart = ShoppingCart(customer_name, current_date)
    # call print menu (print menu has the loop)
    print_menu(shopping_cart)


if __name__ == "__main__":
    main()
