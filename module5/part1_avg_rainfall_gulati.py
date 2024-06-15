# tuple for months in a year
MONTH_TUPLE = (
    "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
    "December")


# validate user input
def get_valid_value(user_input):
    while True:
        try:
            user_input_float = float(user_input)
            if user_input_float < 0:
                raise ValueError
            break
        except:
            user_input = input(f"Try again: ")
    return user_input


# ask for the number of years, we can validate this input as well
number_of_years = int(input("Enter number of years: "))
# initialize total rainfall as zero
total_rainfall = 0
# initialize month count as zero
month_count = 0
# initialize current year as zero
current_year = 0
# Iterate while number of years is reduced to zero
while number_of_years > 0:
    # increase count of current year by one, this will be used for displaying
    current_year += 1
    print("======================")
    print(f"Enter rainfall data for year {current_year}")
    print("======================")
    # for each month in the tuple
    for month in MONTH_TUPLE:
        # ask user to enter rainfall for this month in inches
        rainfall_for_month = float(
            get_valid_value(input(f"Enter rainfall for the month of {month} (inches #.#) ")))
        # add rainfall for the month to previous total rainfall
        total_rainfall = total_rainfall + rainfall_for_month
        # increment month count by one
        month_count = month_count + 1
    # decrement number of years count by one after each iteration of while loop
    number_of_years = number_of_years - 1

# protect division by 0 in case user enters 0 for years
avg_rainfall = total_rainfall / month_count if month_count > 0 else 0
# program output
print("======================")
print("======================")
print(f"Total number of months: {month_count}")
print(f"Total rainfall for the entire period: {total_rainfall}")
print(f"Average rainfall per month for the entire period (inches, rounded): {round(avg_rainfall, 2)}")
