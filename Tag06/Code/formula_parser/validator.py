from exceptions.InvalidOperatorException import InvalidOperator
from exceptions.NotANumberException import NotANumber

def validateFormula(input):
  validatedInput = []

  # check if the input contains of 3 tokens
  tokens = input.split(' ')
  if len(tokens) != 3:
      raise Exception('Invalid formula. Should be of the form "number operator number"')
    
  validatedNumber1 = validateNumber(tokens[0])
  validatedOperator = validateOperator(tokens[1])
  validatedNumber2 = validateNumber(tokens[2])
    
  validatedInput.append(validatedNumber1)
  validatedInput.append(validatedOperator)
  validatedInput.append(validatedNumber2)

  return validatedInput;
    

def validateNumber(num):
  try:
    validatedNumber = float(num)
    if (validatedNumber.is_integer()):
      validatedNumber = int(validatedNumber)
  except ValueError:
    raise NotANumber(f"Invalid Number on token {num}. Should be a float")
  return validatedNumber


def validateOperator(operator):
  validOperators = ['+', '-', '*', '/']
  # check if the second token is a valid operator
  if operator not in validOperators:
    raise InvalidOperator(f'Invalid Operator on token {operator}')
  return operator
