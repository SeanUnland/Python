# for loops

fruits = ["Apple", "Pear", "Peach"]
for fruit in fruits: 
    print(fruit)
    print(fruit + " Pie")
    

    
    
    
# CODING EXERCISE 
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

total_height = 0
for height in student_heights: 
    total_height += height
# print(total_height)

number_of_students = 0

for student in student_heights: 
    number_of_students += 1
# print(number_of_students)

average_height = round(total_height / number_of_students)
print(average_height)


# CODING EXERCISE 

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
# max() function returns highest value in array
print(max(student_scores))
# min() function returns lowest value in array
print(min(student_scores))

highest_score = 0
for score in student_scores: 
    if score > highest_score: 
        highest_score = score
print(f"The highest score in the class is {highest_score}")

# for loop with range() function

for number in range(1, 11, 3): 
    print(number)

total = 0
for number in range(1, 101): 
    total += number
print(total)

# CODING EXERCISE

total = 0
for number in range(2, 101, 2): 
    total += number
print(total)

# FIZZBUZZ CODING EXERCISE

for number in range(1, 101): 
    if number % 3 == 0 and number % 5 == 0: 
        print("FizzBuzz")
    elif number % 3 == 0: 
        print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else: 
        print(number)