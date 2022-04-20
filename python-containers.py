# Exercise 1

# Create a list named students containing some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

students = ["Shay", "Jennifer", "Elroy", "Matt"]

print(f"Exercise 1: second student: {students[1]}, last student: {students[-1]}")

# Exercise 2
# Create a tuple named foods containing the same number of foods (strings) as there are names in the students list.
# Use a for loop to print out the string "food goes here is a good food".

foods = ("spaghetti", "sushi", "a burrito", "a curry")

for food in foods:
    print(f"Exercise 2: {food} is a good food")

# Exercise 3
# Using a for loop, print just the last two food strings from foods.

for food in foods:
    if food == foods[-1]:
        print(f"Exercise 3: {food}")
    elif food == foods[-2]:
        print(f"Exercise 3: {food}")



