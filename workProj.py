import re, csv, os
from datetime import datetime, date, time

def myDictRegex(dict): # Use regex to return a new Dict with the same keys but the values trimmed to be only Dates.
	x = {}
	dateRegex = re.compile(r"\d{1,2}/\d{1,2}(/\d{1,4}){0,1}")
	for k, v in dict.items():
		dates = dateRegex.search(v)
		x[k] = dates.group()
	return x
def compareDates(dict): #Use dates lib to compare current date to datesDict's values. If the dates of datesDict is older than current date than append keys to a list.
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

if __name__ == "__main__":
	CSV_FILENAME = "salesData.csv"
	"os.getcwd() = {}", os.getcwd()
	"__file__ = {}", __file__
	"os.path.dirname(__file__) = {}", os.path.dirname(__file__)

	fileLocalDir = os.path.dirname(__file__)
	absoluteCsvFilePath = os.path.join(fileLocalDir, CSV_FILENAME)
	#os.chdir("c:\\users\\pdinh\\python\\workproject") #for working in shell
present = datetime.today()
#Read the salesData.csv and turn the data into a Dict.
myDict = {}
with open("salesData.csv", newline="") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		myDict[row[0]] = row[1]
	
datesDict = myDictRegex(myDict) #currently only matching the first date if there's multiple dates in the notes.
listOfPastDates = compareDates(datesDict) #final list of all past due orders

#Spit the final list into a new csv file called orders. 
with open ("orders.csv", "w", newline="") as myFile:
	wr = csv.writer(myFile)
	wr.writerows([f] for f in listOfPastDates)
	






