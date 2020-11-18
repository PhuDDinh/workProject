import re, csv

#1st step. Read the salesData.csv and turn the data into a Dict
myDict = {}
>>> with open("salesData.csv", newline="") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		myDict[row[0]] = row[1]