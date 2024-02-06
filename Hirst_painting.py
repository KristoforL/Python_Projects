from turtle import *
from random import *
#Needs to be set to 255 so that the program understands to use RGB sequence
colormode(255)

#Colorgram is a module imported to grab colors from pictures and only has one method called extract
# import colorgram as cg
# colors = cg.extract('Day 18\Hirst_painting.jpg', 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r,g,b)
#     rgb_colors.append(rgb)

# print(rgb_colors)

rgb_colors = [
    (234, 241, 247), (247, 240, 245), (244, 249, 246), (141, 163, 182), 
    (14, 119, 185), (206, 138, 168), (199, 175, 9), (240, 213, 62), 
    (220, 156, 97), (150, 17, 34), (122, 72, 100), (13, 143, 53), (74, 29, 35), (59, 34, 31), (204, 67, 26), (226, 170, 199), (242, 80, 27), (16, 172, 189), (34, 176, 93), (2, 114, 63), (247, 214, 2), (114, 188, 142), (181, 95, 111), 
    (188, 182, 211), (40, 39, 46), (157, 207, 217), (229, 173, 162), 
    (162, 208, 181), (118, 117, 163)
    ]


def left(turtle):
    """Makes left uturn with turtle"""
    turtle.seth(90)
    turtle.fd(50)
    turtle.seth(180)
    turtle.fd(50)

def right(turtle):
    """Makes right uturn with turtle"""
    turtle.seth(90)
    turtle.fd(50)
    turtle.seth(0)
    turtle.fd(50)

def rand_color():
    """Chooses random color from list of tuples"""
    color = choice(rgb_colors)
    return color

def dots(turtle, repeat):
    """Moves turtle forward and places dots down for painting"""
    turtle.pu()
    # turtle.pd() #You can use this if you would like to see the pen draw the lines on each row
    turtle.goto(-200,-200)
    count = 0
    
    while count < 5:
        for i in range(repeat):
            turtle.dot(20, rand_color())
            turtle.forward(50)
        left(turtle)
        for i in range(repeat):
            turtle.dot(20, rand_color())
            turtle.forward(50) 
        right(turtle) 
        count += 1

    turtle.ht()


timmy = Turtle()
timmy.shape('turtle')
screen = Screen()

dots(timmy, 10)

screen.exitonclick() 

