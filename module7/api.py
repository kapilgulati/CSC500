from typing import Union

import uvicorn
from fastapi import FastAPI
from csv_loader.data_loader import (
    load_data,
    get_course_number_for_display,
    get_value_for_key,
)

app = FastAPI()

# we can also lazy load it in the while loop
course_to_room_dict = load_data("csv_loader/course_to_room_data.csv")
course_to_instructor_dict = load_data("csv_loader/course_to_instructor_data.csv")
course_to_meeting_time_dict = load_data("csv_loader/course_to_meeting_time_data.csv")

# create a set of all unique keys
course_numbers = set(course_to_room_dict.keys())
course_numbers.update(course_to_instructor_dict.keys())
course_numbers.update(course_to_meeting_time_dict.keys())

# Create a course number string of available courses
course_numbers_for_display = get_course_number_for_display(course_to_room_dict)


@app.get("/")
def read_root():
    return {"Courses": f"{course_numbers_for_display}"}


@app.get("/items/{item_id}")
def read_item(item_id: str, q: Union[str, None] = None):
    if item_id not in course_to_instructor_dict.keys():
        return {"Supported_Courses": f"{course_numbers_for_display}"}
    else:
        return {
            "Room number": f"{get_value_for_key(course_to_room_dict, item_id)}",
            "Instructor": f"{get_value_for_key(course_to_instructor_dict, item_id)}",
            "Meeting time": f"{get_value_for_key(course_to_meeting_time_dict, item_id)}",
        }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
