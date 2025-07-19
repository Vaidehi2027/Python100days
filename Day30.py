# from tkinter import *
# from tkinter import messagebox
# import random
# import pyperclip
# import json
# FONT = "Times New Roman"

# # ------------------------------PASSWORD FINDER ---------------------------------- #
# # use exception handling only when u dont have an easy alternative
# def find_password():
#     website = website_input.get()
#     try:
#         with open("data.json", "r") as data:
#             Json = json.load(data)
#     except FileNotFoundError:
#         messagebox.showinfo(title="File not found", message="No data file found")
#     else:
#         if website in Json:
#             email = Json[website]["email"]
#             password = Json[website]["password"]
#             messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
#         else:
#             messagebox.showinfo(title="No details found", message=f"No details for the {website} found")


# # ---------------------------- PASSWORD GENERATOR ------------------------------- #

# # Password Generator Project
# def password_generator():
#     import random
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#     symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#     nr_letters = random.randint(8, 10)
#     nr_symbols = random.randint(2, 4)
#     nr_numbers = random.randint(2, 4)

#     list1 = [random.choice(letters) for _ in range(nr_letters)]
#     list2 = [random.choice(numbers) for _ in range(nr_numbers)]
#     list3 = [random.choice(symbols) for _ in range(nr_symbols)]

#     password_list = list1 + list2 + list3
#     random.shuffle(password_list)
#     password = "".join(password_list)
#     Password_entry.insert(0, password)
#     pyperclip.copy(password)

# # ---------------------------- SAVE PASSWORD ------------------------------- #
# def save():
#     website = website_input.get()
#     email = Email_entry.get()
#     password = Password_entry.get()
#     new_data = {
#         website: {
#             "email": email,
#             "password": password,
#         }
#     }
#     if len(website) == 0 or len(password) == 0:
#         messagebox.showwarning(title="Empty data", message="The fields cant be empty!")
#     else:
#         try:
#             with open("data.json", "r") as data:
#                 Json = json.load(data)
#         except FileNotFoundError:
#             with open("data.json", "w") as data:
#                 json.dump(new_data, data, indent=4)
#         else:
#             #Updating old data with new data
#             Json.update(new_data)

#             with open("data.json", "w") as data:
#                 # Saving like writing the updated data
#                 json.dump(Json, data, indent=4)
#         finally:
#                 website_input.delete(0, END)
#                 Password_entry.delete(0, END)

# # ---------------------------- UI SETUP ------------------------------- #
# window = Tk()
# window.title("Vedu's Password Generator")
# window.config(padx=50, pady=50)
# canvas = Canvas(width=200, height=200, highlightthickness=0)
# my_pass_logo = PhotoImage(file="logo.png")
# canvas.create_image(100, 100, image=my_pass_logo)
# canvas.grid(column=1, row=0)

# # columnspace is the no of columns over which we want to stretch the column to fro the starting column
# website_label = Label(text="Website:", font=(FONT, 11, "normal"))
# website_label.grid(row=1, column=0)

# website_input = Entry(width=30)
# website_input.grid(row=1, column=1)
# website_input.focus()

# Username = Label(text="Email/Username:", font=(FONT, 11, "normal"))
# Username.grid(row=2, column=0)

# Email_entry = Entry(width=52)
# Email_entry.grid(row=2, column=1, columnspan=2)
# Email_entry.insert(0, "vaidehimahale180@gmail.com")

# Password = Label(text="Password:", font=(FONT, 11, "normal"))
# Password.grid(row=3, column=0)

# Password_entry = Entry(width=30)
# Password_entry.grid(row=3, column=1)

# Generate_password = Button(text="Generate Password", font=(FONT, 11, "normal"), command=password_generator)
# Generate_password.grid(row=3, column=2)

# Add_button = Button(text="Add", width=39, font=(FONT, 11, "normal"), command=save)
# Add_button.grid(row=4, column=1, columnspan=2)

# Search = Button(text="Search", font=(FONT, 11, "normal"),width=15, command=find_password)
# Search.grid(row=1, column=2)
# window.mainloop()
