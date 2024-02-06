#This is to make the snake classes
from turtle import Turtle as t 

pos = [(0,-20),(0,0),(0,20)]
dist = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for num in pos:
            self.add_segment(num)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0 ,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
    
        self.head.forward(dist)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):  
        if self.head.heading() != 180: 
            self.head.setheading(0)

    def add_segment(self, pos):
        turtle = t("square")
        turtle.pu()
        turtle.color('white')
        turtle.goto(pos)
        self.segments.append(turtle)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
