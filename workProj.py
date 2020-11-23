import re, csv, os
from datetime import datetime, date, time

os.chdir("c:\\users\\pdinh\\python\\workproject") #for working in shell
#CSV_FILENAME = "salesData.csv"
#"os.getcwd() = {}", os.getcwd()
#"__file__ = {}", __file__
#"os.path.dirname(__file__) = {}", os.path.dirname(__file__)

#fileLocalDir = os.path.dirname(__file__)
#absoluteCsvFilePath = os.path.join(fileLocalDir, CSV_FILENAME)


#1st step. Read the salesData.csv and turn the data into a Dict.
myDict = {}
with open("salesData.csv", newline="") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		myDict[row[0]] = row[1]

#2nd step. Use regex to return a new Dict with the same keys but the values trimmed to be only Dates.
def myDictRegex(dict):
	x = {}
	dateRegex = re.compile(r"\d{1,2}/\d{1,2}(/\d{1,4}){0,1}")
	for k, v in dict.items():
		dates = dateRegex.search(v)
		x[k] = dates.group()
	return x

datesDict = myDictRegex(myDict) #currently only matching the first date if there's multiple dates in the notes.

#3rd step. Use dates lib to compare current date to datesDict's values. If the dates of datesDict is older than current date than append keys to a list.
present = datetime.today()	
def compareDates(dict):
	x = []
	for k, v in dict.items():
		try:
			v += "/20" 
			vDates = datetime.strptime(v, "%m/%d/%y")
			if present > vDates:
				x.append(k)
		except ValueError:
			print("Notes value need to be in month/day format, without the year.")
	return x
#This should cover 99% of case. Required data of month/day only. 
listOfPastDates = compareDates(datesDict) #final list of all past due orders
#4th and last step. Spit the final list into a new csv file. 






