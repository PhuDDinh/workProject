import re, csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
#1st step. Read the salesData.csv and turn the data into a Dict
myDict = {}
with open("salesData.csv", newline="") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		myDict[row[0]] = row[1]