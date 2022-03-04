# import colorgram

# colors = colorgram.extract('image.jpg', 10)
# colors_in_picture = []
# i = 0
# for color in colors:
#    first_color = colors[i]
#    rgb = first_color.rgb
#    red = rgb[0]
#    green = rgb[1]
#    blue = rgb[2]
#    colors_in_picture.append((red, green, blue))
#    i += 1
# print(colors_in_picture)
import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
number_of_dots = 0

color_list = [(45, 100, 160), (141, 159, 181), (199, 141, 172), (212, 158, 97), (236, 212, 62), (62, 19, 29), (150, 70, 80), (234, 90, 12), (78, 90, 56), (51, 73, 49)]
t.colormode(255)
tim.penup()
tim.setposition(-200, -200)
xcor = tim.xcor()
ycor = tim.ycor()
tim.pendown()
while number_of_dots < 100:
    for i in range(0, 10):
        for _ in range(0, 10):
            number_of_dots += 1
            random_color = random.choice(color_list)
            tim.dot(20, random_color)
            tim.penup()
            tim.forward(50)
            tim.pendown()
        tim.penup()
        tim.setposition(xcor, ycor + 50)
        tim.pendown()
        ycor += 50
        tim.penup()

screen = Screen()
screen.exitonclick()
