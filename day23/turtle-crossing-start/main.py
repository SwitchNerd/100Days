import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
#Player turtle spawned
player = Player()
carManager = CarManager()
scoreBoard = Scoreboard()
screen.listen()
#Moving
screen.onkeypress(player.move, 'w')

Count = 6
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if Count % 4 == 0:
        carManager.create_cars()
    carManager.move()

    if player.ycor() > 280:
        carManager.new_level()
        #call scorreboard function for level here
        scoreBoard.increase_level()
        player.goto(0,-280)
    
    if carManager.check_distance(player) == True:
        game_is_on = False
        #call scoreboard function for gameover here
        scoreBoard.gameover()
        
    
    Count += 1
    
screen.exitonclick()