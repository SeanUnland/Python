# Object Oriented Programming
from another_module import another_variable
from turtle import Turtle, Screen

# print(another_variable)

timmy = Turtle()
print(timmy)
# Object Methods
#  object.method() separated by a . and () on end of method
timmy.shape("turtle")
timmy.color("#D8D500")
timmy.forward(100)


# Object Attributes
my_screen = Screen()
# object.attribute separated by a .
print(my_screen.canvheight)
my_screen.exitonclick()
