################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope variable only valid within function it was defined in

def drink_potion(): 
    potion_stregnth = 2
    print(potion_stregnth)

drink_potion()

# Global Scope available anywhere because it was defined outside of the function

player_health = 10

def drink_potion(): 
    potion_stregnth = 2
    print(player_health)

drink_potion()
print(player_health)

# There is no block scope in Python

game_level = 3

def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5: 
        new_enemy = enemies[0]
    
    print(new_enemy)
        
# Modifying Global Scope 

enemies = 1

def increase_enemies(): 
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Global Constants (all upercase variable name) like const in JS

PI = 3.14
