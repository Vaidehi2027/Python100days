# from turtle import Turtle,Screen
# tim = Turtle()
# screen = Screen()
# def move_forwards():
#     tim.forward(10)
# # interesting thing is all these methods will be executed on the screen object
# #  getting the turtle to listen what we may tell him in future
# screen.listen()
# # we should bind onto some method to to get the turtle do something
# screen.onkey(key="space",fun=move_forwards)
# # when passing function as an input to the method dont use () cause then it wil trigger the function then only but we have to trigger it after the key press
# screen.exitonclick()

# HIGHER ORDER FUNCTIONS
# a function that can work with other function basically can take a function as an input
# def add(n1,n2):
#     return n1 + n2
# # here calculator is called the higher order function
# def calculator(n1,n2,func):
#     return func(n1,n2)
# result = calculator(2,3,add)
# print(result)

# etch a sketch challenge
# from turtle import Turtle, Screen
# tim = Turtle()
# screen = Screen()
# tim.shape('turtle')
# tim.pensize(5)
# tim.color("green")
# tim.speed("fastest")
# def mov_forwards():
#     tim.forward(20)
#
# def mov_backwards():
#     tim.backward(20)
#
# def counter_clockwise():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def clockwise():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
#def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(mov_forwards,"w")
# screen.onkey(mov_backwards, "s")
# screen.onkey(counter_clockwise, "a")
# screen.onkey(clockwise, "d")
# screen.onkey(clear,"c")
# screen.exitonclick()

#final project turtle race
# Creating different examples of the same object are called instances
# Different instances function differently and hence can be in different states according to their attributes, their movement or their funcion call they are invloved in

# from turtle import Turtle, Screen
# import random
# is_race_on = False
# screen = Screen()
# colors = ["violet","indigo","green","yellow","orange","red"]
# # sets up the size of the window
# screen.setup(width=500, height=400)

# #pop up the dialog box
# user_bet = screen.textinput(title="Turtle betting board", prompt="Choose a color to bet on!")
# y_positions = [-70,  -40, -10, 20, 50, 80]
# all_turtles = []
# for turtle_index in range(0, 6):
#     new_turtle = Turtle(shape="turtle")
#     new_turtle.color(colors[turtle_index])
#     # ensures that no drawing while moving happens
#     new_turtle.penup()
#     # a turtle object is of 40px by 40px so subtract half the width from the co-ordinate
#     new_turtle.goto(x=-230, y=y_positions[turtle_index])
#     all_turtles.append(new_turtle)

# # if user has made a bet start the game
# if user_bet:
#     is_race_on = True

# while is_race_on:
#     # making the turtle move by a different amount
#     for turtle in all_turtles:
#         # catching the winning turtle
#         if turtle.xcor() > 230:
#             # stop the game as one turtle has won
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             # by pencolor we will get just the color of body
#             if winning_color == user_bet:
#                 print(f"You won!The winning turtle is {winning_color}")
#             else:
#                 print(f"You lose!The winning turtle is {winning_color}")
#         distance = random.randint(0, 10)
#         turtle.forward(distance)
# 
# screen.exitonclick()