# initialize reward points to 0
reward_points = 0
# this can be solved by individual if conditions or if-elif conditions
number_of_books = int(input("Enter number of books purchased for this month: "))
# If a customer purchases 0 books, they earn 0 points
if number_of_books < 2:
    reward_points = 0
# If a customer purchases 2 books, they earn 5 points
elif 2 <= number_of_books < 4:
    reward_points = 5
# If a customer purchases 4 books, they earn 15 points
elif 4 <= number_of_books < 6:
    reward_points = 15
# If a customer purchases 6 books, they earn 30 points
elif 6 <= number_of_books < 8:
    reward_points = 30
# If a customer purchases 8 or more books, they earn 60 points
elif number_of_books >= 8:
    reward_points = 60

# display reward points based on the number of books purchased
print(f"Rewards for this month {reward_points}")