from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.color('red')
        self.write(f'Score : {self.score}',False,'center',('Arial', 24,'normal'))
       

    def update(self):
        self.clear()
        self.score += 1
        self.write(f'Score : {self.score}',False,'center',('Arial', 24,'normal'))
        
    def gameover(self):
        self.color('white')
        self.goto(0,0)
        self.write('GAME OVER!', False,'center',('Arial', 24,'normal'))
        
        