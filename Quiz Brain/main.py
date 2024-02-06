import question_model as qm
import data
import quiz_brain as qz

question_bank = []
for question in data.question_data:
    qtext = question['question']
    qanswer = question['answer']
    new_q = qm.Question(qtext, qanswer)
    question_bank.append(new_q)


quiz = qz.Quiz(question_bank)
while quiz.more_qs():
    quiz.next_q()
else:
    print('You have completed the quiz')
    print(f'Your final score is {quiz.score}/{quiz.question_number}')






