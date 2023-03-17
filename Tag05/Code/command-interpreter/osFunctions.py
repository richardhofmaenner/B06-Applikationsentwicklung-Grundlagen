import os

def printWorkingDirectory():
  print(os.getcwd())
  return

def listDirItems():
  print(os.listdir())
  return

def changeDir():
  os.chdir('..')
  print(os.getcwd())
  return

def changeToSubDir():
  dirs = os.listdir()
  validDirInput = False

  print('There are the following directories:')

  while validDirInput == False:
    for dir in dirs:
      print(dir)
    inputDir = input('Please enter a directory name: ')
    if inputDir in dirs:
      validDirInput = True
  
  currentDir = os.getcwd()
  newDir = os.path.join(currentDir, inputDir)

  os.chdir(newDir)

  print(os.getcwd())
  
  return