from collections import namedtuple
from typing import Any

# Define named constant, this will be used for answer validation
ANSWER_EXIT = 'x'
# Define namedtuple to hold constants such as tip percent and sales tax percent
TransactionConstants = namedtuple('TransactionConstants',
                                  ['TIP_PCT', 'TAX_PCT', 'ROUND_PRECISION', 'MIN_SALES_AMT'])
transaction_const = TransactionConstants(18 / 100, 7 / 100, 2, 0.01)
# Define namedtuple to hold sales data indices for easy readability
SalesDataIndices = namedtuple('SalesDataIndices', ['FOOD_CHARGE', 'TIP', 'SALES_TAX'])
sales_data_indices = SalesDataIndices(0, 1, 2)
# Define list to hold sales data and initialize using Sales Data Indices
sales_data: list[float | Any] = [0 for i in range(len(sales_data_indices))]

# define a function to print the sales receipt For a given itemized list, this function will print:
# first value as "Food Charges" second value as "Tip" third value as "Sales Tax"
# and Total by adding the above three values


def print_sales_receipt(itemized_list):
    print("=========================")
    print("\t\tSales Receipt")
    print("=========================")
    print(f"Food charges:\t${itemized_list[sales_data_indices.FOOD_CHARGE]}")
    print(f"Tip:\t\t\t${itemized_list[sales_data_indices.TIP]}")
    print(f"Sales Tax:\t\t${itemized_list[sales_data_indices.SALES_TAX]}")
    print("=========================")
    # loop through all items in the list and calculate sum by adding the elements
    total = 0
    for item in itemized_list:
        total += item
    # Display the total amount
    print(f"Total:\t\t\t${round(total, transaction_const.ROUND_PRECISION)}")
    print("=========================")


# Get the charge for food
keep_going = True
# keep running the loop until exit conditions are met:
# 1) program is existed such as ctrl-c
# 2) user chooses to exit when prompted
while keep_going:
    try:
        # ask user to enter the charge for the food
        charge_for_food_str = input("Enter charge for the food: ")
        # convert user input to float value, round it to a precision value
        sales_data[sales_data_indices.FOOD_CHARGE] = (
            round(float(charge_for_food_str), transaction_const.ROUND_PRECISION))
        # validate that amount entered meets minimum transaction amount
        if sales_data[sales_data_indices.FOOD_CHARGE] >= transaction_const.MIN_SALES_AMT:
            # if valid, then calculate the tip amount by multiplying charge for food and tip percent
            sales_data[sales_data_indices.TIP] = round(
                (sales_data[sales_data_indices.FOOD_CHARGE]) * transaction_const.TAX_PCT,
                transaction_const.ROUND_PRECISION)
            # Calculate the sales tax amount by multiplying charge for food and tax percent
            sales_data[sales_data_indices.SALES_TAX] = round(
                (sales_data[sales_data_indices.FOOD_CHARGE]) * transaction_const.TAX_PCT,
                transaction_const.ROUND_PRECISION)
            # Call print_sales_receipt function to print the sales receipt
            print_sales_receipt(sales_data)
            # Prompt user if they want to continue with another transaction
            # exist if user chooses to do so else continue to enter next food charge
            keep_going = True if (input(
                "Enter 'X or x' if you want to exit else press any key to start another transaction: ").lower()
                                  != ANSWER_EXIT) else False
        else:
            # if in valid, then display input error message
            print(f"Minimum purchase allowed is ${transaction_const.MIN_SALES_AMT}")
    except ValueError:
        # if the value couldn't be converted to float, then display error message
        print("Enter a numeric value in the form of #.## or #")
    except KeyboardInterrupt:
        # exit gracefully if program is exited via keyboard interruption such as ctrl-c
        keep_going = False
