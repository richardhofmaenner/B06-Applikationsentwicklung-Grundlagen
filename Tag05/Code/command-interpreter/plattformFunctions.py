import platform

def printComputerName():
  print("Computer name: " + platform.node())
  return

def printOperatingSystem():
  print("Operating system: " + platform.system())
  return

def printPlatformInfo():
  print("Platform info: " + platform.platform())
  return

def printPythonVersion():
  print("Python version: " + platform.python_version())
  return