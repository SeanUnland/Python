# Object Oriented Programming
# from another_module import another_variable
from turtle import Screen, Turtle

# assigning a variable to a Class()
timmy = Turtle()
print(timmy)

# Object Methods
#  object.method() separated by a . and () on end of method
timmy.shape("turtle")
timmy.color("#D8D500")
timmy.forward(100)


# Object Attributes
# object.attribute separated by a . the attribute may need to = a value
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)