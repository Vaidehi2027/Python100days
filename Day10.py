#FORMING FUNCTIONS WITH OUTPUTS
# .title() can bu used to make the first letter of the word capital
def format_name(f_name,l_name):
    formatted_f_name = f_name.title()
    foramtted_l_name = l_name.title()
    return f"{formatted_f_name}  {foramtted_l_name }"
output = format_name("Angela","YU")
print(output)

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False


# def days_in_month(year,month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if is_leap(year):
#     month_days[1] = 29

#   return month_days[month-1]
#   # #🚨 Do NOT change any of the code below 
# year_input = int(input("Enter a year: "))
# month_input = int(input("Enter a month: "))
# days = days_in_month(year= year_input, month= month_input)
# print(days)

# TRAINER'S WAY:
# def is_leap(year):
#   if year % 4 == 0:
#     if year % 100 == 0:
#       if year % 400 == 0:
#         return True
#       else:
#         return False
#     else:
#       return True
#   else:
#     return False


# def days_in_month(year,month):
#   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#   if month > 12 or month<1:
#     return "Invalid input"
#   if is_leap(year) and month== 2:
#     return 29
#   return month_days[month-1] 
#   # #🚨 Do NOT change any of the code below 
# year_input = int(input("Enter a year: "))
# month_input = int(input("Enter a month: "))
# days = days_in_month(year= year_input, month= month_input)
# print(days)

# def my_function():
#     """ This function is used to print Hello world!"""
#     print ("Hi")
#     print ("World")
# my_function()

# CALCULATOR CODE
# from replit import clear
# from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def calculator():
  # print logo
  num1 = float(input("What's the first number: "))
  for symbol in operations:
    print(symbol)
  # WE are calling a flag here
  should_continue = True
  while should_continue:   
    operation_symbol = input("Pick an operation: ") 
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    game = input("Type y to continue with the same number or n to start with a new number")
    if game == "y":
      num1 = answer
    else:
      should_continue = False
      # WHEN A FUNCTION CALLS ITSELF IT IS KNOWN AS RECURSION WE ARE GOING TO USE RECURSION TO START THE FUNCTION FROM BEGINNING
      # clear()
      calculator()
calculator()
      
      
      

