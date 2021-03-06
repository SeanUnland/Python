#Number Guessing Game Objectives:

from art import logo 

from random import randint

# Global Constant Variables written in all caps
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TRUNS = 5

# Function to check user's guess against actual answer

def check_answer(guess, answer, turns): 
    '''Checks answer against guess, returns the number of turns remaining'''
    if guess > answer: 
        print("Too high")
        return turns - 1
    elif guess < answer: 
        print("Too low")
        return turns - 1
    else: 
        print(f"You got it! The answer was {answer}")
        
# Make function to set difficulty

def set_difficulty(): 
    level = input(f"Choose a difficulty. Type 'easy' or 'hard':")
    if level == "easy": 
        return EASY_LEVEL_TURNS
    else: 
        return HARD_LEVEL_TRUNS
        
def game():
    print(logo)
    # Choosing a random number between 1 and 100

    print(f"Welcome to the Guessing Game")
    print("I'm thinking of a number between 1 and 100")

    answer = randint(1, 100)
    print(f"The answer is {answer}")

    turns = set_difficulty()

    # Repeat the guessing functionality if they get it wrong
    guess = 0
    while guess != answer: 
        print(f"You have {turns} attempts remaining to guess the number.")
        # Let the user guess a number
        guess = int(input(f"Make a guess:\n"))
        # Track the number of turns and reduce by 1 if they get it wrong
        turns = check_answer(guess, answer, turns)
        if turns == 0: 
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer: 
            print("Guess again")


game()