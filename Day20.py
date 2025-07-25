# # code of main.py
# from turtle import Turtle, Screen
# from snake import Snake
# import time

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My ping-pong snake game")
# screen.tracer(0)
# snake = Snake()

# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")
# # the arrow keys are case sensitive

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)

#     snake.move()
# screen.exitonclick()

# code of snake.py
# from turtle import Turtle
# STARTING_POSITIONS = [(0, 0), (-20, 0), (-40,0)]
# MOVE_DISTANCE = 20
# UP = 90
# DOWN = 270
# LEFT = 180
# RIGHT = 0
# # making the starting positions as constant so we can use them

# class Snake:
#     def __init__(self):
#         self.segments = []
#         self.create_snake()
#         # making an attribute for the head
#         self.head = self.segments[0]

#     def create_snake(self):
#         for position in STARTING_POSITIONS:
#             new_segment = Turtle("square")
#             new_segment.color("white")
#             new_segment.penup()
#             new_segment.goto(position)
#             self.segments.append(new_segment)
#             # to refer to the attribute segments

#     def move(self):
#         for seg_num in range(len(self.segments)- 1, 0, -1):
#                 new_x = self.segments[seg_num - 1].xcor()
#                 new_y = self.segments[seg_num - 1].ycor()
#                 self.segments[seg_num].goto(new_x, new_y)
#         self.head.forward(MOVE_DISTANCE)
    
#     def up(self):
#         if self.head.heading() != DOWN:
#             self.head.setheading(UP)

#     def down(self):
#         if self.head.heading() != UP:
#             self.head.setheading(DOWN)

#     def left(self):
#         if self.head.heading() != RIGHT:
#             self.head.setheading(LEFT)

#     def right(self):
#         if self.head.heading() != LEFT:
#             self.head.setheading(RIGHT)
    
# if it is going left it cant go right iff it is going down then it cant go up and son on
# we will restrict the turtle from going back in reverse directions
# now here our snkae moves in opposite directions as well but we want tos top that as it is not allowed in the official snake game