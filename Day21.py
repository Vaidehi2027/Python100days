# # INHERITANCE
# # class Animal:
# #     def __init__(self):
# #         self.num_eyes = 2
    
# #     def breathe(self):
# #         print("Inhale,exhale")

# # # Animal is the super class and Fish is the derived class
# # class Fish(Animal):
# #     def __init__(self):
# #         super().__init__()
# #         # inherites all the data from super class

# #     def breathe(self):
# #         super().breathe()
# #         # inherits the properties of breathe from super class
# #         print("Doing this underwater.")
# #         # adds the modification to breathe in our modified class
    
# #     def swim(self):
# #         print("moving in water.")
    
# # nemo = Fish()
# # nemo.breathe()

# #main.py
# from turtle import Screen
# from snake import Snake
# from food import Food
# from scoreboard import Scoreboard
# import time

# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor("black")
# screen.title("My ping-pong snake game")
# screen.tracer(0)

# snake = Snake()
# food = Food()
# score = Scoreboard()

# screen.listen()
# screen.onkey(snake.up, "Up")
# screen.onkey(snake.down, "Down")
# screen.onkey(snake.left, "Left")
# screen.onkey(snake.right, "Right")
# # the arrow keys are case-sensitive

# game_is_on = True
# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
#     snake.move()
#     # we will detect collision with food by calculating the distance between two Turtle objects the snake and the food
#     if snake.head.distance(food) < 15:
#         food.refresh()
#         snake.extend()
#         score.increase()

#     # DETECT COLLISION WITH A WALL
#     if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
#         game_is_on = False
#         score.game_over()

#     # DETECT TAIL COLLISION
#     # if head collides with any segment in the tail then trigger the game over sequence
#     for segment in snake.segments[1:]:
#         # to bypass the head from this loop
#         # if segment == snake.head:
#         #     pass
#         # elif snake.head.distance(segment) < 10:
#         #     game_is_on = False
#         #     score.game_over()
#         if snake.head.distance(segment) < 10:
#             game_is_on = False
#             score.game_over()
# screen.exitonclick()

# #snake.py
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
#             self.add_segment(position)

#     def add_segment(self,position):
#         new_segment = Turtle("square")
#         new_segment.color("white")
#         new_segment.penup()
#         new_segment.goto(position)
#         self.segments.append(new_segment)
#         # to refer to the attribute segment

#     def extend(self):
#         self.add_segment(self.segments[-1].position())
#         # find the position of the last segment and add new seg there

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
    
# # if it is going left it cant go right iff it is going down then it cant go up and son on
# # we will restrict the turtle from going back in reverse directions
# # now here our snkae moves in opposite directions as well but we want tos top that as it is not allowed in the official snake game

# #food.py
# from turtle import Turtle
# import random
# # class Food:
# #     def __init__(self):
# #         self.food = Turtle()
# #         # one way like this we can make the food class as an object of the Turtle class

# # now we gonna inherit from the Turtle class
# class Food(Turtle):
#     def __init__(self):
#         super().__init__()
#         # here we have made the call to the super class
#         # now we can use everything in food from Turtle
#         self.shape("circle")
#         self.penup()
#         self.shapesize(stretch_len=0.5,stretch_wid =0.5)
#         # we gonna half the circle down from 20 by 20 to 10 by 10
#         self.color("blue")
#         self.speed("fastest")
#         self.refresh()

#     # create a new method to refresh the co-ordinates
#     def refresh(self):
#         random_x = random.randint(-280, 280)
#         random_y = random.randint(-280, 280)
#         self.goto(x=random_x, y=random_y)

# #Scoreboard
# from turtle import Turtle
# ALIGNMENT = "center"
# FONT = ("Courier", 18, "normal")

# class Scoreboard(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.score = 0
#         self.color("white")
#         self.penup()
#         self.goto(0, 260)
#         self.hideturtle()
#         self.update_scoreboard()

#     def update_scoreboard(self):
#         self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)

#     def increase(self):
#         self.score += 1
#         self.clear()
#         self.update_scoreboard()

#     def game_over(self):
#         self.goto( 0, 0)
#         self.write("GAME OVER",align=ALIGNMENT,font=FONT)