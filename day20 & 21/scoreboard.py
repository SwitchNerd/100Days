from turtle import Turtle
with open('udemy\day20 & 21\highscore.txt','r') as f:
    placeholder = int(f.readline())

class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.score = 0
        self.highscore = placeholder
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.color('red')
        self.write(f'Score : {self.score} | HighScore: {self.highscore}',False,'center',('Arial', 24,'normal'))
       

    def update(self):
        self.clear()
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
        self.write(f'Score : {self.score} | HighScore: {self.highscore}',False,'center',('Arial', 24,'normal'))
        
    def gameover(self):
        self.color('white')
        self.goto(0,0)
        self.write('GAME OVER!', False,'center',('Arial', 24,'normal'))
        
        with open('udemy\day20 & 21\highscore.txt','w') as f:
            f.write(str(self.highscore))
        
        