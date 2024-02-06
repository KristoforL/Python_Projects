

from turtle import Turtle as t
import random as r

class Food(t):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('blue')
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        rand_x = r.randint(-430,430)
        rand_y = r.randint(-430,430)
        self.goto(rand_x, rand_y)