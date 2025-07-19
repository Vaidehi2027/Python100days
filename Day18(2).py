from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("purple")
for _ in range(15):
    timmy.forward(10)
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()
my_screen = Screen()
my_screen.exitonclick()