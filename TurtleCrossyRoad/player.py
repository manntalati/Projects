from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.reset()

    def up(self):
        self.penup()
        if self.ycor() < FINISH_LINE_Y:
            self.goto(0, self.ycor() + MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)
