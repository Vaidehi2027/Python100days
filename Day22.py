# # Ping-pong game
# #main.py
# from turtle import Turtle, Screen
# from paddle import Paddle
# from ball import Ball
# from scoreboard import Scoreboard
# import time

# # creating a screen
# screen = Screen()
# screen.tracer(0)
# screen.setup(width=800, height=600)
# screen.bgcolor("black")
# screen.title("Welcome to ping-pong!")

# r_paddle = Paddle((350, 0))
# l_paddle = Paddle((-350, 0))
# attacker = Ball()
# score = Scoreboard()

# screen.listen()
# screen.onkey(fun=r_paddle.up, key="Up")
# screen.onkey(fun=r_paddle.down, key="Down")
# screen.onkey(fun=l_paddle.up, key="w")
# screen.onkey(fun=l_paddle.down, key="s")

# game_is_on = True
# while game_is_on:
#     time.sleep(attacker.move_speed)
#     screen.update()
#     attacker.move()

#     # detect the collision with the wall
#     if attacker.ycor() > 280 or attacker.ycor() < -280:
#         attacker.bounce_y()

#     # detect the collision with the  paddle
#     # we will check both the x distance and the paddle distance to ensure collision even if it hits at end
#     # distance is calculated between centre of ball and the paddle
#     if (attacker.distance(r_paddle) < 50 and attacker.xcor() > 320) or (attacker.distance(l_paddle) < 50 and attacker.xcor() < -320):
#         attacker.bounce_x()
#         attacker.speed()

#     # detect if the r_paddle missed the ball
#     if attacker.xcor() > 380:
#         attacker.reset_position()
#         score.l_point()

#     # detect if the l_paddle missed the ball
#     if attacker.xcor() < -380:
#         attacker.reset_position()
#         score.r_point()
# screen.exitonclick()

# #scoreboard.py
# from turtle import Turtle
# class Scoreboard(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.color("white")
#         self.penup()
#         self.hideturtle()
#         self.l_score = 0
#         self.r_score = 0
#         # scoreboard takes care of both the left score and right score
#         self.update_scoreboard()

#     def update_scoreboard(self):
#         self.clear()
#         self.goto(-100, 180)
#         self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
#         self.goto(100, 180)
#         self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

#     def l_point(self):
#         self.l_score += 1
#         self.update_scoreboard()

#     def r_point(self):
#         self.r_score += 1
#         self.update_scoreboard()

# #ball.py
# from turtle import Turtle
# class Ball(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape("circle")
#         self.color("white")
#         self.penup()
#         self.x_move = 10
#         self.y_move = 10
#         self.move_speed = 0.1

#     def move(self):
#         new_x = self.xcor() + self.x_move
#         new_y = self.ycor() + self.y_move
#         self.goto(new_x,new_y)

#     def bounce_y(self):
#         self.y_move *= -1

#     def bounce_x(self):
#         self.x_move *= -1
#         # bounced in x direction means got hit by a paddle
#         self.move_speed *= 0.9

#     def reset_position(self):
#         self.goto(0, 0)
#         self.move_speed = 0.1
#         # just to ensure it doesnt go increasing indefinitely
#         self.bounce_x()
#     #dont try to interact with the self.move attributes it will nullify the effect instead call the bounce_x function

# #paddle.py
# from turtle import Turtle
# class Paddle(Turtle):
#     def __init__(self,position):
#         super().__init__()
#         self.color("white")
#         self.shape("square")
#         self.shapesize(stretch_wid=5, stretch_len=1)
#         self.penup()
#         self.goto(position)

#     def up(self):
#         new_y = self.ycor() + 20
#         self.sety(y=new_y)

#     def down(self):
#         new_y = self.ycor() - 20
#         self.sety(y=new_y)
 