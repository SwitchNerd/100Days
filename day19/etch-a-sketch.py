from turtle import Turtle, Screen

bob = Turtle()
screen = Screen()

def forward():
    bob.forward(20)

def backwards():
    bob.backward(20)
    
def move_counter_clock_wise():
    bob.left(10)
    
def move_clock_wise():
    bob.right(10)

screen.onkeypress(forward,'Up')
screen.onkeypress(backwards,'Down')
screen.onkeypress(move_clock_wise,'Right')
screen.onkeypress(move_counter_clock_wise,'Left')

screen.listen()

screen.exitonclick()
