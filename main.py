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


# objects
player_paddle = Paddle((0, -250))
ball = Ball("white")

for i in range(1,10):
    add = 85*i
    pos = (-430+add,270)
    brp = BreakoutPaddles(position=pos,color="red")
    breakable_paddles.append(brp)


for i in range(1,10):
    add = 85 * i
    pos = (-430 + add, 210)
    brp = BreakoutPaddles(position=pos, color="orange")
    breakable_paddles.append(brp)

for i in range(1,10):
    add = 85 * i
    pos = (-430 + add, 150)
    brp = BreakoutPaddles(position=pos, color="yellow")
    breakable_paddles.append(brp)

for i in range(1,10):
    add = 85 * i
    pos = (-430 + add, 90)
    brp = BreakoutPaddles(position=pos, color="green")
    breakable_paddles.append(brp)

for i in range(1,10):
    add = 85 * i
    pos = (-430 + add, 30)
    brp = BreakoutPaddles(position=pos, color="blue")
    breakable_paddles.append(brp)

# ---------------------------------------------

screen.onkeypress(key="a", fun = player_paddle.move_left)
screen.onkeypress(key="d", fun = player_paddle.move_right)

speed = 0.007
game_on = True
while game_on:
    time.sleep(speed)
    screen.update()
    ball.move()

    for paddle in breakable_paddles:
        if paddle.distance(ball) < 50 and (ball.ycor() == 250 or ball.ycor() == 190 or ball.ycor() == 130 or ball.ycor() == 70 or ball.ycor() == 10):
            if speed > 0.00010:
                speed -= 0.001
            color = paddle.getturtle().color()
            if color[1] == "black":
                pass
            else:
                ball.color(color[1])
            ball.bounce_y()
            print("collided")
            paddle.reset()
            del paddle


    # bounce on left and right side
    if ball.xcor() > 380 or ball.xcor() < -390:
        ball.bounce_x()

    # bounce of top side
    if ball.ycor() > 280:
        ball.bounce_y()

    # bounce on paddle
    if ball.distance(player_paddle) < 70 and ball.ycor() < -230:
        ball.bounce_y()



screen.mainloop()