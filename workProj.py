import re
myDict = {"2019-92362": "1002287O Labels DTD 11/13", 
          "2018-91252": "ok to mix - liquid eta 11/09", 
          "2017-91253":"1000605 Parsley Root DTD 11/23/20,", 
          "2020-88721": "ntermediate test till 11/10. .liquid in qc 11/03" 
          }
dateRegex = re.compile(r"(\d\d)/(\d\d)")
for v in myDict.values():
    mo = dateRegex.search(v)
    print(mo.group())


