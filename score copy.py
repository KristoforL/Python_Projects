from turtle import Turtle as t
ALIGN = "center"
FONT = ("Arial", 24, "normal")

class sb(t):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.pu()
        self.ht()
        self.r_score = 0
        self.l_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 220)
        self.write(self.l_score, align= 'center', font=("courier", 80,"normal"))
        self.goto(100, 220)
        self.write(self.r_score, align= 'center', font=("courier", 80,"normal"))

    def rscore(self):
        self.clear()
        self.r_score += 1
        self.update_score()

    def lscore(self):
        self.clear()
        self.l_score += 1
        self.update_score()
