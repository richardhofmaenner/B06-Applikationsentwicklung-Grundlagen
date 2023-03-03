import json
import os


def main():
    json_file_name = "Tag03/Übungen/the_gang.json"
    allGangMembers = loadFileContentFromJson(json_file_name)

    averageAge = calculateAverageAge(allGangMembers)
    print(f"The average age of all gang members is {averageAge} years.")

    hairColors = getHairColors(allGangMembers)
    print(f"The hair colors of all gang members are: {hairColors}")

    saveResultsToJson(averageAge, hairColors)


# Get the json file content and load it into a dictionary
def loadFileContentFromJson(json_file_name):
    result = dict()
    # Check if the given file exists
    if os.path.exists(json_file_name):
        with open(json_file_name, "r") as f:
            result = json.load(f)
    return result


# Calculate the average age of all gang members
def calculateAverageAge(allGangMembers):
    sumOfAllAges = 0
    # Iterate over all gang members.
    for key, value in allGangMembers.items():
        sumOfAllAges += value["Age"]
    return sumOfAllAges / len(allGangMembers)


# Get all hair colors of all gang members
def getHairColors(allGangMembers):
    hairColors = dict()
    for key, value in allGangMembers.items():
        if value["Hair"] in hairColors:
            hairColors[value["Hair"]] += 1
        else:
            hairColors[value["Hair"]] = 1
    return hairColors


# Save the results to a json file
def saveResultsToJson(averageAge, hairColors):
    path = "Tag03/Übungen/the_gang_result.json"
    result = dict()
    result["AverageAge"] = averageAge
    result["HairColors"] = hairColors

    if os.path.exists(path):
        os.remove(path)

    with open(path, "w") as file:
        json.dump(result, file)


if __name__ == "__main__":
    main()
