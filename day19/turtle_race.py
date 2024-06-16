from turtle import Turtle,Screen
import random



screen = Screen()
screen.setup(500,400)
choice = screen.textinput("Make a bet","Which turtle will win? Enter a color: ")
colors = ['red','orange','yellow','green','blue','purple']
variables = ['red','orange','yellow','green','blue','purple']

for i in range(6):
    variables[i] = Turtle('turtle')
    variables[i].penup()
    variables[i].goto(-240 ,-100+ (i*35))
    variables[i].color(colors[i])

if choice != '':
    race = True

while race:
    for turtle in variables:
        forward = random.randint(1,10)
        turtle.forward(forward)
        if int(turtle.xcor()) > 222:
            race = False
            pencolor = turtle.pencolor()

print(f'Turtle {pencolor} has won!')
if choice == pencolor:
    print('You have guessed correctly!')
else:
    print('Better luck next time!')

screen.exitonclick()