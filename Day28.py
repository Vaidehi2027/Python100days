# from tkinter import *
# import math
# # ---------------------------- CONSTANTS ------------------------------- #
# PINK = "#e2979c"
# RED = "#e7305b"
# GREEN = "#9bdeac"
# YELLOW = "#f7f5dd"
# FONT_NAME = "Courier"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
# reps = 0
# timer = None
# # ---------------------------- TIMER RESET ------------------------------- # 
# def reset_timer():
#     window.after_cancel(timer)
#     canvas.itemconfig(timer_text, text="00:00")
#     my_label.config(text="Timer")
#     checkmarks.config(text="")
#     global reps
#     reps = 0

# #---------------------------- TIMER MECHANISM ------------------------------- #

# def start_timer():
#     global reps
#     reps += 1
#     work_sec = WORK_MIN * 60
#     short_break_sec = SHORT_BREAK_MIN * 60
#     long_break_sec = LONG_BREAK_MIN * 60

#     if reps % 8 == 0:
#         count_down(long_break_sec)
#         my_label.config(text="Long Break", fg=RED)
#     elif reps % 2 == 0:
#         count_down(short_break_sec)
#         my_label.config(text="Break", fg=PINK)
#     else:
#         count_down(work_sec)
#         my_label.config(text="WORK", fg=GREEN)

# # ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# def count_down(count):
#     count_min = math.floor(count / 60)
#     count_sec = count % 60
#     # changing the datatype by assigning different value is known as dynamic typing
#     if count_sec < 10:
#         count_sec = f"0{count_sec}"
#     canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
#     if count > 0:
#         global timer
#         timer = window.after(1000, count_down, count-1)
#     else:
#         start_timer()
#         marks = " "
#         work_sessions = math.floor(reps/2)
#         for _ in range(work_sessions):
#             marks += "✔"
#         checkmarks.config(text=marks)
# # ---------------------------- UI SETUP ------------------------------- #
# window = Tk()
# window.title("Pomodoro")
# window.config(padx=100, pady=50, bg=YELLOW)
# # we have to create a canvas to layer things
# canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# tomato_img = PhotoImage(file="tomato.png")
# canvas.create_image(100, 112, image=tomato_img)
# timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.grid(column=1, row=1)
# my_label = Label(text="Timer", font=(FONT_NAME, 35, "normal"))
# my_label.config(fg=GREEN, bg=YELLOW)
# my_label.grid(column=1, row=0)

# start = Button(text="Start", font=(FONT_NAME, 12, "normal"), highlightthickness=0, command=start_timer)
# start.grid(column=0, row=2)

# reset = Button(text="Reset", font=(FONT_NAME, 12, "normal"), highlightthickness=0, command=reset_timer)
# reset.grid(column=2, row=2)

# checkmarks = Label(fg=GREEN, bg=YELLOW)
# checkmarks.grid(column=1, row=3)
# window.mainloop()