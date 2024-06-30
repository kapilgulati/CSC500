import csv


def load_data(file_name, discard_header=True):
    """
    Reads data from a CSV file and returns dictionary (key-value pairs).
    It assumes that data file has only two columns, first column is the key and the second column is the value.
    :param file_name: file name to load (relative path)
    :param discard_header: discard first row if True, default True
    :return:
    """
    data_dict = {}
    with open(file_name) as data_file:
        data_reader = csv.reader(data_file, delimiter=',')
        # if first row is header row, we will discard it
        if discard_header:
            header = next(data_reader)
        #  iterate through each row and load data into dictionary
        for row in data_reader:
            # index 0 = key, index 1 = value
            data_dict[row[0]] = row[1]
    return data_dict


def get_course_number_for_display(key_set):
    """
    Computes the available course number string by concatenating the given set of values.
    :param key_set: set of course numbers
    :return: String - Comma separated course numbers
    """
    course_numbers_for_display = ""
    for pos, course in enumerate(key_set):
        course_numbers_for_display = course_numbers_for_display + course + (
            "" if (pos == len(key_set) - 1) else ", ")
    return course_numbers_for_display


def get_value_for_key(data_dict, key):
    """
    Returns the value of a given key from a dictionary (key-value pairs).
    Returns "No match found" if the key is not present in the dictionary.
    :param data_dict: data dictionary (key-value pairs) to use for lookup
    :param key: String - key to look for in given data dictionary
    :return: string - value of a given key or "No match found" if key is not present in the dictionary.
    """
    if key in data_dict:
        return data_dict[key]
    else:
        return "No match found"


# ask user to enter a course number
def main():
    # first we load the application data into dictionary, assuming data is provided in a CSV file as key-value pairs
    # we can also lazy load it in the while loop
    course_to_room_dict = load_data("course_to_room_data.csv")
    course_to_instructor_dict = load_data("course_to_instructor_data.csv")
    course_to_meeting_time_dict = load_data("course_to_meeting_time_data.csv")

    # create a set of all unique keys
    course_numbers = set(course_to_room_dict.keys())
    course_numbers.update(course_to_instructor_dict.keys())
    course_numbers.update(course_to_meeting_time_dict.keys())

    # Create a course number string of available courses
    course_numbers_for_display = get_course_number_for_display(course_to_room_dict)

    # start the infinite while loop, as we want to run the program until user short-circuits and exits
    while True:
        # Ask the customer to enter the room number for which they want information
        course_number_input = input(
            f"Input a course number from available courses - {course_numbers_for_display} or press 'q' to exit: ")
        # if user enter "q" then exit the loop
        if course_number_input.strip() == "q":
            print("User opted to exit, exiting...")
            break
        # if user enter any other value besides "q" then
        # validate user input by comparing it with course_to_room_dict keys
        elif course_number_input not in course_to_instructor_dict.keys():
            print(
                f"Invalid input, try again.")
        else:
            # used for formatting the display
            format_table = "{label:25}{value:10}"
            print("-" * 35)
            print(f"Information for Course number {course_number_input}")
            print("-" * 35)
            # if a valid value was entered, lookup and print the room using course to room dictionary,
            # print "not found" if no match was found
            print(format_table.format(label="Room number:",
                                      value=f"{get_value_for_key(course_to_room_dict, course_number_input)}"))
            # if a valid value was entered, lookup and print the room using course to room dictionary,
            # print "not found" if no match was found
            print(format_table.format(label="Instructor:",
                                      value=f"{get_value_for_key(course_to_instructor_dict, course_number_input)}"))
            # if a valid value was entered, lookup and print the room using course to room dictionary,
            # print "not found" if no match was found
            print(
                format_table.format(label="Meeting time:",
                                    value=f"{get_value_for_key(course_to_meeting_time_dict, course_number_input)}"))


if __name__ == "__main__":
    main()
