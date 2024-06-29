from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        #making the midddle thingo
    
        super().__init__()
        self.one_score = 0
        self.two_score = 0
        self.hideturtle()
        self.color('white')

        #making the score
        self.penup()
        self.goto(0,245)
        self.update_score()

        
    def update_score(self):
        self.clear()
        self.write(f'{self.one_score}   {self.two_score}',False,'center',('Arial', 40,'normal'))
    
    def one_scored(self):
        self.one_score += 1
       
        self.update_score() 
        return self.one_score
          

    def two_scored(self):
        self.two_score += 1
        self.update_score()
        return self.two_score