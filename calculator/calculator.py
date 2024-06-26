from art import logo
import os

# Add
def add(n1, n2):
  return n1 + n2

# Subtract
def subtract(n1, n2):
  return n1 - n2

# Multiply
def multiply(n1, n2):
  return n1 * n2
  
# Divide
def divide(n1, n2):
  return n1 / n2

# Operations

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
    
  operation_symbol = input("Pick an operation from the line above: ")
  num2 = float(input("What's the second number?: "))
  
  calculation_function = operations[operation_symbol]
  first_answer = calculation_function(num1, num2)
  
  print(f"{num1} {operation_symbol} {num2} = {first_answer}")
  
  # Another operation
  calc_continue = True
  
  while calc_continue:
    should_continue = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to start a new calculation: ")
  
    if should_continue == "y":
      calc_continue = True
  
      operation_symbol = input("Pick another operation: ")
      num3 = float(input("What's the next number?: "))
      calculation_function = operations[operation_symbol]
      second_answer = calculation_function(first_answer, num3)
  
      print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
      first_answer = second_answer
  
    elif should_continue == "n":
      calc_continue = False
      os.system('clear')
      calculator()

calculator()