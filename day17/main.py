from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    Text = i['text']
    Answer = i['answer']
    new_question = Question(Text,Answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
flag = True
while flag:
    quiz.next_question()
    flag = quiz.stil_has_questions()