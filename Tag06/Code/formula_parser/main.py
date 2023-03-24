from validator import validateFormula

def main():
  print_instructions()
  while True:
    userInput = input("Please enter a formula to parse: ")
    if userInput == 'exit':
     break
    if userInput == 'help':
      print_instructions()
      continue
    if userInput == 'clear':
      print('\033c')
      continue

    try:
      userInput = validateFormula(userInput)
    except Exception as e:
      handleException(e)
      continue

    result = calculateFormula(userInput)

    print(f"\nThe result of the formular {userInput[0]} ({type(userInput[0])}) {userInput[1]} {userInput[2]} ({type(userInput[2])})  is {result}. \n")


def print_instructions():
  print('')
  print('Welcome to the Formula Parser')
  print('Please enter a formula to parse')
  print('Enter "exit" to quit the program')
  print('Enter "help" to see the instructions again')
  print('Enter clear to clear the screen')
  print('')


def handleException(e):
  print("")
  print("There was some exception. See below for details:")
  print(f"Exception type: {e.__class__.__name__}")
  print(f"Exception message: {e.args[0]}")
  print("")

def calculateFormula(formula):
  number1 = formula[0]
  operator = formula[1]
  number2 = formula[2]

  if operator == '+':
    return number1 + number2
  elif operator == '-':
    return number1 - number2
  elif operator == '*':
    return number1 * number2
  elif operator == '/':
    return number1 / number2

if __name__ == '__main__':
  main()
