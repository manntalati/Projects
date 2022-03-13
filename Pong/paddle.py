from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, xcor, ycor):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.setposition(xcor, ycor)

    def up(self):
        if self.ycor() < 260:
            self.goto(x=self.xcor(), y=self.ycor() + 20)

    def down(self):
        if self.ycor() > -260:
            self.goto(x=self.xcor(), y=self.ycor() - 20)