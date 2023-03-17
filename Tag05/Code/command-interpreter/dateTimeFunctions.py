import datetime


def calcDateFromNow():
  isValidDayInput = False

  while not isValidDayInput:
  
    try:
      numOfDays = input('Number of days: ')
      numOfDays = int(numOfDays)
    except ValueError:
      print("The number of days is not valid.")
      break

    # check if numOfDays is a number
    if not isinstance(numOfDays, int):
      print("The number of days is not valid.")
      break
    
    if numOfDays < 0:
      print("The number of days is not valid. Has to be bigger then 0.")
      break

    isValidDayInput = True

  # get current date
  currentDate = datetime.datetime.now()

  # calculate new date
  newDate = currentDate + datetime.timedelta(days=numOfDays)

  # print new date
  print("The new date is: " + str(newDate))

  return

def calcNegDateFromNow():
  isValidDayInput = False

  while not isValidDayInput:
  
    try:
      numOfDays = input('Number of days: ')
      numOfDays = int(numOfDays)
    except ValueError:
      print("The number of days is not valid.")
      break

    # check if numOfDays is a number
    if not isinstance(numOfDays, int):
      print("The number of days is not valid.")
      break
    
    if numOfDays < 0:
      print("The number of days is not valid. Has to be bigger then 0.")
      break

    isValidDayInput = True

  # get current date
  currentDate = datetime.datetime.now()

  # calculate new date
  newDate = currentDate + datetime.timedelta(days=-numOfDays)

  # print new date
  print("The new date is: " + str(newDate))

  return

def getDateAndDaysAndCalcDate():
  isValidDateInput = False
  isValidDayInput = False

  while not isValidDateInput:
    try:
      inputDate = input("Please enter a date (YYYY-MM-DD): ")
      inputDate = datetime.datetime.strptime(inputDate, "%Y-%m-%d")
    except ValueError:
      print("The date is not valid.")
      break

    isValidDateInput = True

  while not isValidDayInput:
  
    try:
      numOfDays = input('Number of days: ')
      numOfDays = int(numOfDays)
    except ValueError:
      print("The number of days is not valid.")
      break

    # check if numOfDays is a number
    if not isinstance(numOfDays, int):
      print("The number of days is not valid.")
      break
    
    if numOfDays < 0:
      print("The number of days is not valid. Has to be bigger then 0.")
      break

    isValidDayInput = True

  # calculate new date
  newDate = inputDate + datetime.timedelta(days=numOfDays)

  # print new date
  print("The new date is: " + str(newDate))
  return

def getTwoDatesAndCalcDays():
  isValidDate1Input = False
  isValidDate2Input = False

  while not isValidDate1Input:
    try:
      inputDate1 = input("Please enter a date (YYYY-MM-DD): ")
      inputDate1 = datetime.datetime.strptime(inputDate1, "%Y-%m-%d")
    except ValueError:
      print("The date is not valid.")
      break

    isValidDate1Input = True
  
  while not isValidDate2Input:
    try:
      inputDate2 = input("Please enter a date (YYYY-MM-DD): ")
      inputDate2 = datetime.datetime.strptime(inputDate2, "%Y-%m-%d")
    except ValueError:
      print("The date is not valid.")
      break

    isValidDate2Input = True

  # calculate time delta with datetime
  timeDelta = inputDate2 - inputDate1

  # print time delta in days
  print("The time delta in days is: " + str(timeDelta.days))

  return