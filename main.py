
#calculator1

def add(n1,n2):
  return n1 + n2

def subtract(n1, n2):
  return n1- n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "/" : divide,
  "*" : multiply
}

def calculator():
 
  num1 = float(input("input the frist number "))
  for symbol in operations:
    print(symbol)
  operation_symbol = input("pick an operations symbol from the line above ")
  num2 = float(input("input the second number "))
  answer = operations[operation_symbol](num1,num2)
  print(f"{num1} {operation_symbol}  {num2} = {answer}")
  
  
  #asking user for another operation or continue with the answer or start fresh
  next_calc = input(f"Type 'y' to continue calculating with {answer} or 'n' to to start new calculation ")
  if next_calc == "n":
    calculator()

  while next_calc == "y":
    for symbol in operations:
      print(symbol)
    operation_symbol = input("pick an operations symbol from the line above ")
    num3 = int(input("input the next number "))
    
    second_answer = operations[operation_symbol](answer,num3)
    
    print(f"{answer} {operation_symbol}  {num3} = {second_answer}")
    #asking the user if they want or continue with the answer or start fresh
    next_calc = input(f"Type 'y' to continue calculating with {second_answer} or 'n' to exit ")
    if next_calc == "y":
      answer = second_answer
      second_answer = 0
    else:
      calculator()
    
  
calculator()