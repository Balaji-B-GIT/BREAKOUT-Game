from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(180)
        self.shapesize(stretch_wid=1,stretch_len=7)
        self.penup()
        self.goto(position)

    def move_left(self):
        self.setheading(180)
        self.forward(20)

    def move_right(self):
        self.setheading(360)
        self.forward(20)
