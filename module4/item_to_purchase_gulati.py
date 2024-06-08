# Define Class for Shopping Cart Items
class ItemToPurchase:
    # Default constructor, with defaults
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # this method will print the item object
    def print_item_cost(self):
        item_cost = self.item_price * self.item_quantity
        print(f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${item_cost}')


def main():
    # define max cart item as variable, this allows us to adjust value from one location.
    max_cart_items = 2
    # initialize list for cart item objects
    cart_items = list(range(max_cart_items))
    # for loop to get user input, loop will iterate exactly max_cart_items times
    for i in range(max_cart_items):
        # print item number
        print(f"Item {i+1}")
        # prompt user to input item details
        item_name = input("Enter item name: ")
        item_price = float(input("Enter item price: "))
        item_quantity = int(input("Enter item quantity: "))
        # place item in the list
        cart_items[i] = ItemToPurchase(item_name, item_price, item_quantity)
    else:
        # initialize cart total
        cart_total = 0.0
        # print cart
        print("       TOTAL COST")
        for item in cart_items:
            item.print_item_cost()
            cart_total = cart_total + (item.item_quantity * item.item_price)
        print(f"      Total: ${cart_total}")


if __name__ == "__main__":
    main()
