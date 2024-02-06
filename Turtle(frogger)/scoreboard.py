from turtle import Turtle as t

ALIGN = "center"
FONT = ("Courier", 12, "normal")


class Sb(t):
    
    def __init__(self):
        super().__init__()
        self.color('black')
        self.pu()
        self.ht()
        self.score = 1
        self.goto(-250, 280)
        self.write(f"Level: {self.score}", align= ALIGN, font= FONT)

    
    def su(self):
        self.clear()
        self.score+=1
        self.write(f"Level: {self.score}", align= ALIGN, font= FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGN, font = ("Comic_san", 24, "bold"))

