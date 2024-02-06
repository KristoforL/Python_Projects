class Quiz:

    def __init__(self, qlist):
        self.question_number = 0
        self.questions =  qlist
        self.score = 0

    def more_qs(self):
        return self.question_number < len(self.questions)

    def next_q(self):
        question = self.questions[self.question_number]
        self.question_number += 1
        answer = input(f'Q.{self.question_number}: {question.text}.True/False: ')
        self.check(answer, question.answer)

    def check(self, uanswer, correct_answer):
        if uanswer.lower() == correct_answer.lower():
            self.score += 1
            print(f"Correct\nYour current score:{self.score}/{self.question_number}")
        else:
            print(f'Incorrect\nThe correct answer is {correct_answer}')
            print(f'Your current score:{self.score}/{self.question_number}')
    
