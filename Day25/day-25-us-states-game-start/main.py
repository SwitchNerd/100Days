import pandas
from turtle import Turtle, Screen
import time
csv = 'Day25/day-25-us-states-game-start/50_states.csv'
IMAGE = 'Day25/day-25-us-states-game-start/blank_states_img.gif'
screen = Screen()
screen.title('US states game')
background_turtle = Turtle()
background_turtle.hideturtle()
screen.bgpic(IMAGE)
background_turtle.penup()
states_turtle = Turtle()
states_turtle.penup()
states_turtle.hideturtle()

screen.setup()
states = pandas.read_csv(csv)
states_names = states.state
game_on = True
states_counter = []
while game_on:
    answer = screen.textinput('Guess the states!','Enter a state name:')
    if answer == 'Exit':
        game_on = False
    else:

        found = states[states_names == answer]
        if found.empty:
            background_turtle.goto(0,0)
            background_turtle.write('NO SUCH STATE',False,'center',('Arial',24,'normal'))
            time.sleep(2)
            background_turtle.clear()
        else:
            if answer in states_counter:
                print('Repeated')
            else:
                states_counter.append(answer)
            x_axis = int((found.x).iloc[0])
            y_axis = int((found.y).iloc[0])
            states_turtle.goto(x_axis,y_axis)
            states_turtle.write(answer,False,'center',('Arial',10,'normal'))
    if len(states_counter) == 50:
        time.sleep(1)
        background_turtle.color('red')
        background_turtle.write('CONGRATS YOU HAVE WON!!!',False,'center',('Arial',24,'normal'))
        time.sleep(1)
        game_on = False         
        


