#This will a mini etch and sketch project



#Importing the classes needed for this
from turtle import Turtle as t
from turtle import Screen as s

#Creating objects for the turtle on the screen and the screen itself
tim = t()
screen = s()

def move_forward():
    tim.forward(10)

def move_back():
    tim.backward(10)

def turn_left():
    new_heading = tim.heading() +10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() -10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.pu()
    tim.home()
    tim.pd()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()