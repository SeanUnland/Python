import random
import my_module

# print(my_module.pi)

# random_integer = random.randint(1, 10)
# print(random_integer)

# random_float = random.random() * 5
# print(random_float)

# love_score = random.randint(1, 100)

# print(f"your love score is {love_score}")

# Coin toss exercise
# random_side = random.randint(0, 1)
# if random_side == 1: 
#     print("Heads")
# else: 
#     print("tails")

# Array's or List's

# states_of_america = ["Delaware", "Pennsylvania", "New York"]

# states_of_america[1] = "Pencilveinya"

# # adding to end of array or list .append
# states_of_america.append("Sean")
# # adds a list to an array .extend
# states_of_america.extend(["New Jersey", "Maine"])

# num_of_states = len(states_of_america)

# print(len(states_of_america))
# print(states_of_america[num_of_states -1])

# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes"]
vegtebles = ["Spinach", "Kale", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegtebles]

print(dirty_dozen)







# coding exercise
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# # get total number of items in array or list len() function
# num_items = len(names)
# random_choice = random.randint(0, num_items - 1)
# person_who_will_pay = names[random_choice]
# # using choice() method
# person_who_will_pay = random.choice(names)
# print(person_who_will_pay + " is going to buy the meal today")




# CODING EXERCISE

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(position[0]) #2
vertical = int(position[1]) #3

selected_row = (map[vertical - 1])

selected_row[horizontal - 1] = "X"

# or like this
map[vertical - 1][horizontal - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")