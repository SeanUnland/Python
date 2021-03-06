# Dictionaries or Objects
# "Key": and "Values",

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected",
    "Function": "A piece of code that you can easily call over and over again",
}

# Retrieve items from a dictionary or object
print(programming_dictionary["Bug"])

# Adding new items to a dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

# Creating an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary: 
    print(key)
    print(programming_dictionary[key])
    
#############CODING EXERCISE###############

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores: 
    score = student_scores[student]
    if score > 90: 
        student_grades[student] = "Outstanding"
    elif score > 80: 
        student_grades[student] = "Exceeds Expectations"
    elif score > 70: 
        student_grades[student] = "Acceptable"
    else: 
        student_grades[student] = "Fail"
    
print(student_grades)

###########################################

# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a list in a dictionary or array in object

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

["A", "B", ["C", "D"]]

# Nesting a Dictionary in a Dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

# Nesting a dictionary in a list

travel_log = [
    {
        "country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "total_visits": 12
        },
    {
        "country": "Germany", 
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits": 5
        }
]

############CODING EXERCISE###########

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]


#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visited, times_visited, cities_visited): 
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)
    
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

######################################