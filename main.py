
import colorgram


rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colors = (r, g, b)
    rgb_colors.append(colors)

print(rgb_colors)


from turtle import Turtle, Screen, colormode
import random

colormode(255)

tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.goto(-200, 200)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


# Draw a dot with size 10
def lines():
    for _ in range(20):
        tim.dot(10, random.choice(color_list))
        tim.penup()
        tim.forward(20)
        tim.pendown()


for _ in range(20):
    lines()
    tim.penup()
    tim.goto(-200, tim.ycor()-20)


#my_turtle.dot(10, (202, 164, 110))


screen = Screen()
screen.exitonclick()
