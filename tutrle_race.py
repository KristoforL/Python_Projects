#This will be covering more on classes OOP by making a turtle race

from turtle import Turtle as t
from turtle import Screen as s
import random as r



 
screen = s()
screen.setup(width=900, height=400)

user_bet = screen.textinput(title="Make your wager", prompt="Which turtle will win the race. Pick a color: ")
colors = ['red', 'blue', 'green', 'brown', 'black', 'purple']
turts = []

print(user_bet)


length = len(colors)
x=-230
y=-100

while length >= 1:
    turtle = t(shape='turtle')
    turtle.color(colors[length-1])
    turtle.pu()
    turts.append(turtle)
    turtle.goto(x, y)
    y+=40
    length-=1

def forward(turtle):
    turtle.forward(r.randint(0,10))




def race():
    
    finished = False
    while not finished:
        
        for turtle in turts:
            if turtle.xcor()>230:
                finished = True
                winner = turtle.pencolor()
            
                if winner == user_bet:
                    print(f"You win. {winner.title()} crossed first")
                    screen.clear()
                else:
                    print(f"You lost. {winner.title()} crossed first")
                    screen.clear()    
            else:
                forward(turtle)
        
        

print(turts)

# Working on making this a loop so that it can run multiple times. 
# letsRace = True
# while letsRace:
#     race()
#     if input('Want to race again? Y/N:' ).lower() == 'y':
#         turtle.Screen.bye()
        
screen.exitonclick()