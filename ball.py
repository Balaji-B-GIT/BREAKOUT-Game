from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self,color):
        super().__init__()
        self.shape("circle")
        self.color(color)
        self.penup()
        self.x_move = random.choice([1,-1])
        self.y_move = -1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1