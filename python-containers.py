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

# Exercise 4
# Create a dictionary named home_town containing the keys of city, state and population.
# Print a string with this format: "I was born in city, state - population of population"

home_town = {
    "city": "London",
    "state": "(the UK doesn't have states- RULE BRITANNIA!)",
    "population": "8.982 million"
}
    
print(f"Exercise 4: I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")

# Exercise 5
# Iterate over the key: value pairs in home_town and print a string for each item, for example:
# "city = Arcadia"
# "state = California"
# "population = 58000"

for key, val in home_town.items():
    print(f"Exercise 5: {key} = {val}")

# Exercise 6
# Create an empty list named cohort.

# Using a for loop, add one dictionary to the cohort list for each student name. 
# Each dictionary should have this shape:

#  {
#    'student': 'Tina',
#    'fav_food' 'Cheeseburger'
#  }
# Iterate over cohort printing out each element.



