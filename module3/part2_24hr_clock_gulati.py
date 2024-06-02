from collections import namedtuple

# Define named constant, this will be used for answer validation
SENTINEL_VALUE = 'x'
# Define AlartSystem named tuple that will hold constants for the alarm
AlarmSystem = namedtuple("AlarmSystem",
                         ["clock_start_hour", "clock_last_hour", "hours_in_day", "alarm_min_wait", "alarm_max_wait"])
# create alarm tuple using AlarmSystem named tuple with values as 0 for clock start hour, 23 for clock last hour,
# 0 as minimum value allowed for wait hours and 10 yrs(not accounting leap years) as max wait hours allowed
alarm = AlarmSystem(0, 23, 24, 0, 10 * 365 * 24)
# create dictionary for capturing user input for current hour and hours to wait before setting off the alarm
alarm_dict = {"current_hour": 0, "hours_to_wait": 0}


# function to verify user input, raises error if input is invalid otherwise returns an integer equivalent of input
def read_int_input(input_prompt, min_value, max_value):
    is_valid = False
    while not is_valid:
        try:
            # convert value to an integer value
            input_int = int(input(input_prompt))
            # validate if the integer value is with in the range
            is_valid = min_value <= input_int <= max_value
            if not is_valid:
                # raise error if value is not in the range
                raise ValueError
            else:
                # return input value as integer
                return input_int
        except (ValueError, TypeError):
            # display error message if there was error converting input to integer or if value is not in allowed range
            print(f"Input must be a whole number >= {min_value} and <= {max_value}.")


set_new_alarm = True
while set_new_alarm:
    try:
        # Input current hour
        alarm_dict["current_hour"] = read_int_input("Enter the current time in hours: ", alarm.clock_start_hour,
                                                    alarm.clock_last_hour)
        # Input hours to wait 
        alarm_dict["hours_to_wait"] = read_int_input("Enter number of hours to wait for the alarm: ",
                                                     alarm.alarm_min_wait, alarm.alarm_max_wait)
        # Calculate the number of days to wait before the alarm is set off
        # by dividing (Integer Division //) total hours and clock hours
        num_days = (alarm_dict["current_hour"] + alarm_dict["hours_to_wait"]) // alarm.hours_in_day
        # Calculate the alarm time to go off as modulus (reminder operator %) of the total hours and clock hours
        alart_time = (alarm_dict["current_hour"] + alarm_dict["hours_to_wait"]) % alarm.hours_in_day
        # Display the number of days to wait and at alarm time
        if num_days == 0:
            print(f"Alarm will go off today in {alart_time} hours")
        else:
            print(f"Alarm will go off in {num_days} days and {alart_time} hours")
        set_new_alarm = True if (input(
            "Enter 'X or x' if you want to exit else press any key to start another transaction: ").lower()
                                 != SENTINEL_VALUE) else False
    except ValueError as err:
        print(err)
    except KeyboardInterrupt:
        set_new_alarm = False
