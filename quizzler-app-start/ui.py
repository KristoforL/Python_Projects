from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg = THEME_COLOR)
        


        self.score = Label(text =  f"Score: 0", bg = THEME_COLOR, fg = "white", font =("Ariel", 10, "bold"))
        self.score.grid(row = 0, column =1)

        self.canvas = Canvas(width = 300, height=250, bg= "white")
        self.questions = self.canvas.create_text(
            150,
            125, 
            width= 280,
            text = "Questions go here",
            fill= THEME_COLOR, 
            font =("Ariel", 20, "italic")
        )
        self.canvas.grid(row=1, column = 0, columnspan=2)
        self.canvas.grid(pady =50)


        checkimg = PhotoImage(file= "E:/Github/100daysOfCode/Day 34/quizzler-app-start/images/true.png")
        ximg = PhotoImage(file= "E:/Github/100daysOfCode/Day 34/quizzler-app-start/images/false.png")

        self.check = Button(image = checkimg,highlightthickness = 0, command = self.correct)
        self.x = Button(image = ximg,highlightthickness = 0, command=self.wrong)

        self.check.grid(row=2, column =0)
        self.x.grid(row=2, column =1)

        self.get_question()


        self.window.mainloop()

    def get_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.questions, text = q_text)
        else:
            self.canvas.itemconfig(self.questions, text="You've reached the end of the quiz")
            self.check.config(state = "disabled")
            self.x.config(state = "disabled")

    def correct(self):
        self.feedback(self.quiz.check_answer("True"))

    def wrong(self):
        is_true = self.quiz.check_answer("False")
        self.feedback(is_true)

    def feedback(self, is_true):
        if is_true:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_question)