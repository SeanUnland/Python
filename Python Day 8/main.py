# Functions with Inputs

# def greet(): 
#     print("hello")
#     print("world")
#     print("test")

# greet()

# Functions that allows for input

def greet_with_name(name): 
    print(f"Hello {name}")
    print(f"How are you {name}?")
    
greet_with_name("Sean")

#  Functions with more than one input

def greet_with(name, location): 
    print(f"Hello {name} from {location}")
    
greet_with("Sean", "New York City")
# Keyword Argument 
greet_with(name="Sean", location="NYC")

# Keyword Arguments

def number_function(a, b, c): 
    print(f"Hello {a}, {b}, and {c}")
number_function(a=1, b=2, c=3)

# Coding Exercise ##########################

import math
def paint_calc(height, width, cover): 
    area = height * width
    num_of_cans = math.ceil(area / cover) # math.ceil rounds up numbers, need to import math
    print(f"You'll need {num_of_cans} cans of paint")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

##########################################################

# Coding Exercise ######################

def prime_checker(number): 
    is_prime = True
    for i in range(2, number): 
        if number % i == 0: 
            is_prime = False
        if is_prime: 
            print(f"It is a prime number")
        else: 
            print("It's not a prime number")

n = int(input("Check this number: "))
prime_checker(number=n)

#######CODING EXERCISE######################################

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount): 
    cipher_text = ""
    for letter in plain_text: 
        position = alphabet.index(letter)
        new_position = position + shift_amount 
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

encrypt(plain_text=text, shift_amount=shift)

######################################################

######CODING EXERCISE#########################

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction): 
    end_text = ""
    if cipher_direction == "decode": 
            shift_amount *= -1
    for letter in start_text: 
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
##############################################