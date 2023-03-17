import osFunctions
import dateTimeFunctions
import plattformFunctions
import requestsFunctions

def main():
  terminate = False

  while not terminate:
    printInstructions()
    choosenCommand = chooseCommand()
    if not isValidCommand(choosenCommand):
      print("Invalid command")
      continue

    if choosenCommand == '?': printInstructions()
    if choosenCommand == 'e': terminate = True

    if choosenCommand == '1': dateTimeFunctions.calcDateFromNow()
    if choosenCommand == '2': dateTimeFunctions.calcNegDateFromNow()
    if choosenCommand == '3': dateTimeFunctions.getDateAndDaysAndCalcDate()
    if choosenCommand == '4': dateTimeFunctions.getTwoDatesAndCalcDays()

    if choosenCommand == '10': osFunctions.printWorkingDirectory()
    if choosenCommand == '11': osFunctions.listDirItems()
    if choosenCommand == '12': osFunctions.changeDir()
    if choosenCommand == '13': osFunctions.changeToSubDir()

    if choosenCommand == '30': plattformFunctions.printComputerName()
    if choosenCommand == '31': plattformFunctions.printOperatingSystem()
    if choosenCommand == '32': plattformFunctions.printPlatformInfo()
    if choosenCommand == '33': plattformFunctions.printPythonVersion()

    if choosenCommand == '40': requestsFunctions.getSourceCode()

def chooseCommand():
  command = input("Please enter a command: ")
  return command

def isValidCommand(command):
  validCommands = ["1", "2", "3", "4", "10", "11", "12", "13", "30", "31", "32", "33", "40", "?", "e"]
  if command in validCommands:
    return True
  else:
    return False


def printInstructions():
  print("""
  1 - ask for an amount of days and calculate and print the date from now (now + days)
  2 - ask for an amount of days and calculate and print when that date was (now - days)
  3 - ask for a date and an amount of days to calculate and  print a second date
  4 - ask for two dates and calculate and print the time delta in days
  
  10 - print current directory
  11 - print items of current directory ('ls'/'dir')
  12 - move one directory up ('cd ..')
  13 - ask for a sub-directory name and go into ('cd xyz')
  
  30 - print computer name
  31 - print operating system
  32 - print platform info
  33 - print Python version

  40 - ask for a URL and print the source code of the website

  ? - print this instructions
  e - exit program

  """)


if __name__ == "__main__":
  main()
