# Define a named constant as clock hours and assign the value of 24
CLOCK_HOURS = 24
# approximately 10 years not accounting leap years
ALARM_MAX = 10 * 365 * CLOCK_HOURS


# function to verify user input
def validate_int(input_value, min_value, max_value):
    if input_value.isdigit():
        input_int = int(input_value)
        return min_value <= input_int <= max_value
    else:
        return False


# Get the current hour
is_valid = False
current_hour = 0
while not is_valid:
    current_hour_str = input("Enter the current time in hours: ")
    is_valid = validate_int(current_hour_str, 0, 23)
    if is_valid:
        current_hour = int(current_hour_str)
    else:
        print("Please enter a value between 0 and 23")

# Get the hours to wait
is_valid = False
hours_to_add = 0
while not is_valid:
    hours_to_add_str = input("Enter number of hours to wait for the alarm: ")
    is_valid = validate_int(hours_to_add_str, 0, ALARM_MAX)
    if is_valid:
        hours_to_add = int(hours_to_add_str)
    else:
        print(f"Alarm can not be for the past, and can not be longer than {ALARM_MAX} hrs")

# Calculate the total hours by adding current hours and hours to wait
total_hours = current_hour + hours_to_add
# Calculate the number of days to wait before the alarm is set off
# by dividing (Integer Division //) total hours and clock hours
num_days = total_hours // CLOCK_HOURS
# Calculate the alarm time to go off as modulus (reminder operator %) of the total hours and clock hours
alart_time = total_hours % CLOCK_HOURS
# Display the number of days to wait and at alarm time
if num_days == 0:
    print(f"Alarm will go off today in {alart_time} hours")
else:
    print(f"Alarm will go off in {num_days} days and {alart_time} hours")
