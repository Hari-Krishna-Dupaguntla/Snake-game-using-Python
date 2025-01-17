from turtle import Turtle
starting_pos = [(0, 0), (-20, 0), (-40, 0)]
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]
    def create_snake(self):
        for positions in starting_pos:
            self.Add_segment(positions)
    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def Add_segment(self,position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extedn(self):
        self.Add_segment(self.segments[-1].position())
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)
    def up(self):

        if self.head.heading()!=DOWN:
            self.head.setheading(90)
    def down(self):

        if self.head.heading()!=UP:
            self.head.setheading(270)
    def left(self):

        if self.head.heading()!=RIGHT:
            self.head.setheading(180)
    def right(self):

        if self.head.heading()!=LEFT:
            self.head.setheading(0)
