class QuizBrain:
    def __init__(self,list):
        self.question_number = 0
        self.question_list = list
        self.score = 0 
    def next_question(self):
        q_list = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f'Q.{self.question_number}: {q_list.text} (True/False): ')
        self.check_answer(answer, q_list.answer)
        
    def stil_has_questions(self):
        n = len(self.question_list) - 1
        if self.question_number > n:
            return False
        return True
        
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('Your answer is correct!')
            self.score += 1
        else:
            print('Your answer was incorrect.')
        print(f'The correct answer was : {correct_answer}')
        
        print(f'Your current score is : {self.score}/{self.question_number}')
            