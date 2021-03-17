print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a crossroad, where do you want to go? Type "left" or "right".\n').lower()

if choice1 == "left": 
    choice2 = input('You\'ve come to a lake. There is an island in the middle. Type "wait" to wait for a boat, or type "swim" to swim across\n').lower()
    if choice2 == "wait":
        choice3 = input("You've arrived at the island. Choose what color door to enter, red, blue, or yellow\n").lower()
        if choice3 == "red": 
            print("That was dumb, you walked into a sword and died. Game Over")
        elif choice3 == "yellow": 
            print("Treasure found! You won")
        elif choice3 == "blue": 
            print("You Od'd and died. Game Over")
        else:
            print("This door doesn't exist. You dead!")
    else: 
        print("You don't know how to swim so you drowned and died. Game Over")
else: 
    print("You just tripped into a pit of glass laced with poison and died. Game Over")