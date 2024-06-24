from turtle import Turtle
starting_positions = [(0,0), (-20,0),(-40,0)]
class Snake:
    def __init__(self):
        self.segments = []
        self.initalise_segments()
        
    def initalise_segments(self):
        for position in starting_positions:
            new_seg = Turtle('square')
            new_seg.color('white')
            new_seg.penup()
            new_seg.goto(position)
            self.segments.append(new_seg)
    
    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.segments[0].forward(20)
        
    def north(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
    def east(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
    def west(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
    def south(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
        # 0 east 90 north 180 west 270 south
        
    
