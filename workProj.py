import re, csv

#REGEX_TEST = [("1002287O Labels DTD 11/13", "11/13"),
              #("ok to mix - liquid eta 11/09", "11/09"),
              #("1000605 Parsley Root DTD 11/23/20", "11/23/20"),
              #("ntermediate test till 11/10. .liquid in qc 11/03", "11/10", "11/03"),
              #("articulating splines 4/2/2020", "4/2/2020"),
              #("ladeedah 04/01/20", "04/01/20"),
              #("five ten 12/1/2020", "12/1/2020")]

#myDict = {"2019-92362": "1002287O Labels DTD 11/13", 
          #"2018-91252": "ok to mix - liquid eta 11/09", 
          #"2017-91253":"1000605 Parsley Root DTD 11/23/20,", 
          #"2020-88721": "ntermediate test till 11/10. .liquid in qc 11/03" 
         # }
# dateRegex = re.compile(r"(\d\d)/(\d\d)")
# for v in myDict.values():
#     mo = dateRegex.search(v)
#     print(mo.group())

#def TestDateRegex(regexStr):
    for test in REGEX_TEST:
        res = [x.group() for x in re.finditer(regexStr, test[0])]
        cases = len(test) - 1
        for n in range(1, cases + 1):
            match = res[n - 1]
            print(match)
            assert match == test[n]

#if __name__ == "__main__":
    testRegexStr = "\d{1,2}/\d{1,2}(/\d{1,4}){0,1}"
    TestDateRegex(testRegexStr)

#1st step. Read the salesData.csv and turn the data into a Dict
myDict = {}
>>> with open("salesData.csv", newline="") as csvfile:
	reader = csv.reader(csvfile)
	for row in reader:
		myDict[row[0]] = row[1]