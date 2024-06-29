FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None: 
        super().__init__()
        self.level_count = 1
        self.penup()
        self.hideturtle()
        self.write_level()
    
    def write_level(self):
        self.goto(-265,265)
        self.write(f'Level {self.level_count}',True,'left',FONT)
    def increase_level(self):
        self.clear()
        self.level_count += 1 
        self.write_level()
    def gameover(self):
        self.goto(0,0)
        self.write('GAME OVER', False, 'center', FONT)