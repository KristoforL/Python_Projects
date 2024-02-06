from turtle import Turtle as t 

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(t):
    
    def __init__(self):
        super().__init__()
        self.pu()
        self.seth(90)
        self.shape('turtle')
        #self.color('black')
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)