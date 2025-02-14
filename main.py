from turtle import *
from ball import *
from player_paddle import *
from tiles import *
import time

screen = Screen()
screen.title("BREAKDOWN")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)


# objects
paddle = Paddle((0, -250))
ball = Ball()
# ---------------------------------------------

screen.onkeypress(key="a", fun = paddle.move_left)
screen.onkeypress(key="d", fun = paddle.move_right)

speed = 0.007
game_on = True
while game_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    # bounce on left and right side
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    # bounce of top side
    if ball.ycor() > 280:
        ball.bounce_y()

    # bounce on paddle
    if ball.distance(paddle) < 70 and ball.ycor() < -230:
        ball.bounce_y()



screen.mainloop()