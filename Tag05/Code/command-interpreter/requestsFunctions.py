import requests

def getSourceCode():
  url = input("Please enter a URL: ")

  response = requests.get(url)

  if response.status_code == 200:
    print(response.text)
  return