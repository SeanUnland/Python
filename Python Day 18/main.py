from turtle import Turtle, Screen
from heroes import *




# imports everything in module using *
# from turtle import *

# Alias modules import module name as alias name
# import turtle as t

tim = Turtle()
tom = Turtle()
terry = Turtle()

# tim.shape("turtle")
# tim.color("#7FFFD4")

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)



print(heroes.gen())











screen = Screen()
screen.exitonclick()