# GREEN = "#B1DDC6"
# from tkinter import *
# import pandas
# import random
# window = Tk()
# window.title("Flashy flash cards")
# window.config(padx=50, pady=50, bg=GREEN)
# current_card = {}
# to_learn = {}
# # afterwards it will be filled with a list of dictionaries

# try:
#     data = pandas.read_csv("data/words_to_learn.csv")
# except FileNotFoundError:
#     original_data = pandas.read_csv("data/french_words.csv")
#     to_learn = original_data.to_dict(orient="records")
# else:
#     to_learn = data.to_dict(orient="records")
# # orient="records" can be used to take out a list of dictionaries

# def card_back():
#     canvas.itemconfig(canvas_image, image=canvas_new_image)
#     canvas.itemconfig(French, text="English", fill="white")
#     canvas.itemconfig(Word, text=current_card["English"], fill="white")

# def is_known():
#     to_learn.remove(current_card)
#     data = pandas.DataFrame(to_learn)
#     data.to_csv("data/words_to_learn.csv", index=False)
#     #by setting index=false it doesnt add the index no while creating the words to learn csv
#     new_word()

# canvas = Canvas(width=800, height=526, highlightthickness=0, bg=GREEN)
# canvas_old_image = PhotoImage(file="images/card_front.png")
# canvas_new_image = PhotoImage(file="images/card_back.png")
# canvas_image = canvas.create_image(400, 263, image=canvas_old_image)
# canvas.grid(row=0, column=0, columnspan=2)

# French = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
# Word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

# flip_timer = window.after(3000, func=card_back)

# def new_word():
#     global current_card,  flip_timer
#     window.after_cancel(flip_timer)
#     current_card = random.choice(to_learn)
#     french_word = current_card["French"]
#     canvas.itemconfig(French, text="French", fill="black")
#     canvas.itemconfig(Word, text=french_word, fill="black")
#     canvas.itemconfig(canvas_image, image=canvas_old_image)
#     flip_timer = window.after(3000, func=card_back)

# right = PhotoImage(file="images/right.png")
# known = Button(image=right, highlightthickness=0, command=is_known)
# known.grid(row=1, column=1)

# wrong = PhotoImage(file="images/wrong.png")
# unknown = Button(image=wrong, highlightthickness=0, command=new_word)
# unknown.grid(row=1, column=0)
# new_word()
# # this function call is to get a first word when we dont click any buttton
# window.mainloop()