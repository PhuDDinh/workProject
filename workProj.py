import re, csv, os

CSV_FILENAME = "salesData.csv"
print("os.getcwd() = {}", os.getcwd())
print("__file__ = {}", __file__)
print("os.path.dirname(__file__) = {}", os.path.dirname(__file__))

fileLocalDir = os.path.dirname(__file__)
absoluteCsvFilePath = os.path.join(fileLocalDir, CSV_FILENAME)
print(absoluteCsvFilePath)

#1st step. Read the salesData.csv and turn the data into a Dict
myDict = {}
with open(absoluteCsvFilePath, newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        myDict[row[0]] = row[1]
