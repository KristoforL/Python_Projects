from turtle import Turtle as t
ALIGN = "center"
FONT = ("Arial", 24, "normal")

class sb(t):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.pu()
        self.goto(0, 410)
        self.write(f"Score: {self.score}", align= ALIGN, font= FONT)
        self.ht()
        
    def score_up(self):
        self.clear()
        self.score +=1
        self.write(f"Score: {self.score}", align= ALIGN, font= FONT)


    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALIGN, font = FONT)