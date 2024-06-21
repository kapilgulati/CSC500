# Define Class for Shopping Cart Items
class ItemToPurchase:
    # Default constructor, with defaults
    def __init__(self, item_name="none", item_price=0.0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity

    # this method will print the item object
    def print_item_cost(self):
        """
        Concatenates and returns string consisting of item name, quantity and cost
        :return: string = formatted value
        """
        item_cost = self.item_price * self.item_quantity
        return f'{self.item_name} {self.item_quantity} @ ${self.item_price} = ${item_cost}'

    def has_default_values(self, dynamic_attr):
        """
        Checks and returns True, if dynamic attribute doesn't exist or if the object's class attributes
        are set to their default values
        :param dynamic_attr: string - name if the dynamic attribute to check if it exists
        :return: boolean
        """
        return (not hasattr(self, dynamic_attr)) or (
                    self.item_name.strip().lower() == "none" and self.item_price == 0.0 and self.item_quantity == 0)
