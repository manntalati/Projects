from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer()

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkeypress(r_paddle.up, key="Up")
screen.onkeypress(r_paddle.down, key="Down")
screen.onkeypress(l_paddle.up, key="w")
screen.onkeypress(l_paddle.down, key="s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        ball.x_bounce()
        scoreboard.increase_score("left")

    if ball.xcor() < -380:
        ball.reset_position()
        ball.x_bounce()
        scoreboard.increase_score("right")


screen.exitonclick()
