# Define a named constant as tip percent and assign the value of 18%
TIP_PERCENT = 18/100
# Define a named constant as sales tax percent and assign the value of 0.07
SALES_TAX_RATE = 0.07
# Get the charge for food
invalid_input = True
charge_for_food = -1
while invalid_input:
    try:
        charge_for_food = round(float(input("Enter charge for food: ")), 2)
        if charge_for_food <= 0:
            raise ValueError("Minimum purchase amount is $0.01")
        invalid_input = False
    except:
        print("Enter a valid value")
# Calculate the tip amount by multiplying charge for food and tip
tip_amount = round(charge_for_food * TIP_PERCENT, 2)
# Calculate the sales tax amount by multiplying charge for food and sales tax percent
sales_tax_amount = round(charge_for_food * SALES_TAX_RATE,2)
# Calculate the total amount of meals purchased by adding charge for food, tip amount, and sales tax
total_amount = charge_for_food + tip_amount + sales_tax_amount
# Display the total amount
print("=========================")
print("\t\tSales Receipt")
print("=========================")
print(f"Food charges:\t${charge_for_food}")
print(f"Tip:\t\t\t${tip_amount}")
print(f"Sales Tax:\t\t${sales_tax_amount}")
print("=========================")
print(f"Total:\t\t\t${total_amount}")
print("=========================")