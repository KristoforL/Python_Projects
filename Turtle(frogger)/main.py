import time
from turtle import Screen
from player import *
from car_manager import CarManager as cm
from scoreboard import *

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p1 = Player()
score = Sb()
vehicle = cm()

screen.listen()
screen.onkey(p1.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    vehicle.create_car()
    vehicle.go()

    #Detect contact with vehicle
    for car in vehicle.all_cars:
        if car.distance(p1)< 25: #checks the distance between the object and the parameter then compares it to the 25 and provides a true or false 
            game_is_on =False
            score.gameover()

    if p1.ycor()>280:
        score.su()
        p1.reset()
        vehicle.speed_up()


screen.exitonclick()