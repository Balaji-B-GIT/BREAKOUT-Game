import turtle
from turtle import *
from ball import *
from player_paddle import *
from tiles import *
import time


breakable_paddles = []
screen = Screen()
screen.title("BREAKDOWN")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.listen()
screen.tracer(0)


sec = 0
def timer():
    global sec
    sec += 1
    screen.ontimer(timer, 1000)
timer()


# objects
text = turtle.Turtle()
player_paddle = Paddle((0, -250))
ball = Ball("white")

# Create breakable paddles
colors = ["red", "orange", "yellow", "green", "blue"]
y_positions = [270, 210, 150, 90, 30]

# for y, color in zip(y_positions, colors):
#     for i in range(1, 10):
#         add = 85 * i
#         pos = (-430 + add, y)
#         brp = BreakoutPaddles(position=pos, color=color)
#         breakable_paddles.append(brp)
for i in range(1,10):
    add = 85 * i
    pos = (-430 + add, 90)
    brp = BreakoutPaddles(position=pos, color="green")
    breakable_paddles.append(brp)
# ---------------------------------------------

screen.onkeypress(key="a", fun = player_paddle.move_left)
screen.onkeypress(key="d", fun = player_paddle.move_right)

died = 0
paddles_broken = 0
speed = 0.001
speeds = [0.004]
game_on = True
while game_on:
    if speed < 0:
        speed = 0
    time.sleep(speed)
    screen.update()
    ball.move()

    for paddle in breakable_paddles:
        if paddle.distance(ball) < 45 and paddle.ycor() - 20 < ball.ycor() < paddle.ycor() + 20:
            paddles_broken += 1
            if paddles_broken % 5 == 0:
                speed -= 0.0007
            ball.color(paddle.getturtle().color()[1])
            paddle.reset()
            paddle.penup()
            paddle.goto((-280,380))
            ball.bounce_y()


    # bounce on left and right side
    if ball.xcor() > 380 or ball.xcor() < -390:
        ball.bounce_x()

    # bounce of top side
    if ball.ycor() > 280:
        ball.bounce_y()

    # bounce on paddle
    if ball.distance(player_paddle) < 70 and ball.ycor() < -230 and ball.y_move < 0:
        player_paddle.color(ball.getturtle().color()[1])
        ball.bounce_y()

    if ball.ycor() < -280:
        died += 1
        time.sleep(1)
        ball.home()
    if paddles_broken == 9:
        ball.reset()
        player_paddle.reset()
        game_on = False

text.write(arg="Completed",font=("ariel",50,"bold"))

screen.mainloop()