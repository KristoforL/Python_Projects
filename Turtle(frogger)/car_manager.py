from turtle import Turtle as t
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(t):
    
    def __init__(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []


    def create_car(self):
        chance = r.randint(1,6)
        if chance == 6:
            car = t("square")
            car.pu()
            car.shapesize(stretch_wid=1, stretch_len = 2)
            car.color(r.choice(COLORS))
            y = r.randint(-250, 240)
            car.goto(300, y)
            self.all_cars.append(car)

    def go(self):
        for car in self.all_cars:
            car.backward(self.car_speed)


    def speed_up(self):
        self.car_speed += (MOVE_INCREMENT * .5)