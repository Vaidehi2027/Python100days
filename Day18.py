# from turtle import Turtle,Screen
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("purple")
# # timmy.forward(100)
# # timmy.right(90)
# # challenge1 - draw a square

# # timmy.forward(100)
# # timmy.left(90)
# # timmy.forward(100)
# # timmy.left(90)
# # timmy.forward(100)
# # timmy.left(90)
# # timmy.forward(100)
# # timmy.left(90)
# # for _ in range(4):
# #     timmy.forward(100)
# #     timmy.left(90)
# my_screen = Screen()
# my_screen.exitonclick()

# ways to import can be
# 1. siddha import then using module.class()
# 2. if we are using a class many times then from module import class
# 3. to import everything thats in a module we can use  from module import *

# there are modules with long names they can be given names as alias
# For eg:import turtle as t 
#     tim = t.Turtle()

# some modules cant be imported they have to be installed

# draw a dashed line
#penup means no drawing #pendowm means drawing while moving
# for _ in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

#  drawing diff shapes
from turtle import Screen
import turtle as t
import random
tim = t.Turtle()
tim.shape("turtle")
# colors = ["medium blue","sea green","firebrick","violet","thistle","maroon"]
# def draw_shape(num_sides):
#     angle = 360/num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
# for i in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shape(i)

#TURTLE CHALLENGE 04
# directions = [0,90,180,270]
# tim.pensize(15)
# tim.speed(10)
# for _ in range(200):
#     tim.forward(30)
#     tim.setheading(random.choice(directions))
#     tim.color(random.choice(colors))
# my_screen = Screen()
# my_screen.exitonclick()

#python tuples
# python tuples are immutable and cant be changed
# my_tuple = (1,3,8)
# my_tuple[2]
# 8
# my_tuple[2] = 7 is not possible tuples are immutable
# rgb colors are designed using tuples and are in range (0,255)
# we have to shift from colormode 
# t.colormode(255)
# directions = [0,90,180,270]
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     my_tuple = (r,g,b)
#     return my_tuple
# tim.pensize(15)
# tim.speed("fastest")
# for _ in range(1000):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

# drawing the spirograph
# 1. drawing the circle

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     answer = (r,g,b)
#     return answer

# # 2. how to determine the radius
# # 3. how to tilt them
# # 4. how to make a spirograph out of them
# def draw_spirograph(size_of_gap):
#     # size of gap will specify the distance between circles
#     for _ in range(int(360 / size_of_gap)):
#         # for loop jo hain barabar utne circles baithane ke liye
#         tim.color(random_color())
#         tim.circle(50)
#         # to change the heading direction of the turtle use setheading and change headings
#         current = tim.heading()
#         tim.setheading(current + size_of_gap)
# draw_spirograph(15)
# my_screen = Screen()
# my_screen.exitonclick()

# final project
# import colorgram
# # extracts colors from images
# rgb_colors = []
# colors = colorgram.extract('image.jpg',30)
# for color in colors:
# # for using in turtle want the colors in tuples of r,g and b
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color = (r,g,b)
#     rgb_colors.append(color)
# print(rgb_colors)
# color_list = [ (210, 171, 83), (22, 115, 152), (158, 30, 46),(170, 74, 51), (225, 202, 131), (139, 181, 195), (203, 134, 153), (16, 27, 60), (161, 47, 64), (184, 163, 43),
#  (139, 3228), (42, 109, 80), (135, 181, 165), (7, 55, 35), (56, 21, 42), (36, 165, 189), (87, 26, 22), (13, 89, 65),
#  (196, 102, 68), (9, 98, 107), (223, 171, 180)]
#draw the dots
# make a 10 by 10 pattern
# make the dot of 10 size
# move forward without printing
tim = t.Turtle()
# for starting at the end of the page we have to write some lines of code
# tim.speed("fast")
# tim.penup()
# tim.hideturtle()
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
# for dot_count in range(1,number_of_dots + 1):
#     tim.dot(20,random.choice(color_list))
#     tim.forward(50)
#     if(dot_count%10==0):
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)

# screen = Screen()
# screen.exitonclick()