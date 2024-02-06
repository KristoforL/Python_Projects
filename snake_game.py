from snake import *
from turtle import Screen as s
import score 
import food as f
import time

screen = s()
screen.setup(width=900, height =900)
screen.bgcolor("Black")
screen.title("Snake")
screen.tracer(0)


python = Snake()
food = f.Food()
scores = score.sb()

screen.listen()
screen.onkey(python.up, "Up")
screen.onkey(python.down, "Down")
screen.onkey(python.left, "Left")
screen.onkey(python.right, "Right")


gameOn = True
while gameOn:
    screen.update()
    time.sleep(.1)
    python.move()   

    #Detecting collision with food
    if python.head.distance(food) < 15:
        food.refresh()
        scores.score_up()
        python.extend()
        
        

    #Detect collision with wall
    if python.head.xcor() > 439 or python.head.xcor() < -439 or python.head.ycor() > 439 or python.head.ycor() < -439:
        gameOn = False
        scores.game_over()

    #Detect collision with tail
    for segment in python.segments[1:]:
        if python.head.distance(segment) < 10:
            gameOn = False
            scores.game_over()

screen.exitonclick()