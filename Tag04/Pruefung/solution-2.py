# open sample file
with open("Tag04/Pruefung/sample-2mb-text-file.txt", "r") as file:
    countOfRows = 0
    countOfEst = 0
    # read file line by line
    for line in file:
        countOfRows += 1
        # check if est is in line. If so, increment the countOfEst
        if "est" in line:
            countOfEst += 1
print(f"Anzahl Zeilen: {countOfRows}")
print(f"Anzahl Zeilen mit 'est': {countOfEst}")