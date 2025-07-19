# # with open("WEATHER_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)

# # how do we make use of csv files in data preprocessing
# # import csv
# # with open("weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     # print(data)
# #     # after creation of the object it can be looped through
# #     temperatures = []
# #     for row in data:
# #         # we have to exclude the label wali line
# #         if row[1] != "Temp":
# #             temperatures.append(int(row[1]))
# # print(temperatures)
# import pandas
# # data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # temperatures = data["Temp"]
# # print(type(temperatures))
# # the whole sheet is called the dataframe and each column is called the series
# # data_dict = data.to_dict()
# # will make the dict in dict and each column is the key where column is its value stored in a dict
# # print(data_dict)
# # temp_list = data["Temp"].to_list()
# # printing the average of the values
# # average = int(sum(temp_list) / len(temp_list))
# # print(average)
# # alternate way to return the mean
# # print(data["Temp"].mean())

# # how to return the maximum of all values
# # print(temperatures.max())

# #Get the data in columns
# # print(data["Condition"])
# # # in the backend pandas takes the tags and converts them into attributes
# # print(data.Condition)

# # how to get the data in the rows of the dataframe
# # print(data[data.Day == "Monday"])
# #
# # #print the row of data where temp was maximum
# # print(data[data.Temp == data.Temp.max()])
# #
# # monday = data[data.Day == "Monday"]
# # print(monday.Condition)

# #convert mondays temp to Fahrenheit
# # monday = data[data.Day == "Monday"]
# # mon_temp = int(monday.Temp)
# # mon_fah = (9/5) * (mon_temp) + 32
# # print(mon_fah)

# #Create a dataframe from scratch
# # data_dict = {
# #     "students": ["Amy", "James", "Angela"],
# #     "scores": [76, 56, 65]
# # }
# # data = pandas.DataFrame(data_dict)
# # # in argument we will have to pass the path of the file which we want it to get saved
# # data.to_csv("new_data.csv")

# # data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# # grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# #
# # # after getting the rows it gets treated like an iterable basically like a list so we can len function on it
# # cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# # black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# #
# # data_dict = {
# #     "color": ["Gray", "Cinnamon", "Black"],
# #     "count": [grey_squirrels_count,cinnamon_squirrels_count, black_squirrels_count ]
# # }
# # Squirrel = pandas.DataFrame(data_dict)
# # Squirrel.to_csv("squirrel_count.csv")

# import turtle
# import pandas
# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# # once we load the image as a shape it can be used by turtle as a shape
# turtle.shape(image)
# # def get_mouse_click_coor(x, y):
# #     print(x, y)
# # turtle.onscreenclick(get_mouse_click_coor)
# # turtle.mainloop()
# data = pandas.read_csv("50_states.csv")
# all_states = data["state"].to_list()
# correct_guess = []
# while len(correct_guess) < 50:
#     answer_state = screen.textinput(title=f"{len(correct_guess)}/50 states correct", prompt="Whats another state's name?").title()
#     if answer_state == "Exit":
#         missing = []
#         for state in all_states:
#             if state not in correct_guess:
#                 missing.append(state)
#         new_data = pandas.DataFrame(missing)
#         new_data.to_csv("Missed_states.csv")
#         break
#     if answer_state in all_states:
#             t = turtle.Turtle()
#             t.hideturtle()
#             t.penup()
#             state_data = data[data["state"] == answer_state]
#             t.goto(int(state_data.x), int(state_data.y))
#             t.write(answer_state)
#             correct_guess.append(answer_state)
# missing = []



