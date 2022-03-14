from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-290, 260)
        self.level = 1
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="Left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="Center", font=FONT)
