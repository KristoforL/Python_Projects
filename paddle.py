from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.pu()
        self.goto(position)
        self.shape('square')
        self.color('white')
        self.turtlesize(stretch_len = 1, stretch_wid=4)



    def up(self):
        y =  self.ycor()+20
        self.goto(self.xcor(), y)

    def down(self):
        y =  self.ycor()-20
        self.goto(self.xcor(), y)


