import re, csv, os
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
	datesDict = {}
	dateRegex = re.compile(r"\d{1,2}/\d{1,2}(/\d{1,4}){0,1}")
	for k, v in dict.items():
		dates = dateRegex.search(v)
		datesDict[k] = dates.group()
	return datesDict

	
finalDict = myDictRegex(myDict)
print(finalDict)



