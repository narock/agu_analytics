import csv

year = input("Enter year to query: ")
year = str(year)

Dictfilename = year + "keyDict.csv"
Readfilename = year + "keyword.csv"

with open(Dictfilename, 'wb') as csvfile:
    resultwriter = csv.writer(csvfile, delimiter= ',' ,
                              quoting=csv.QUOTE_MINIMAL)

    keyDictionary = {}
    keyCount = 0

    infile = open(Readfilename, "r")
    for line in infile:
        result = line.split(",")
        keyword = result[0]
        section = result[1]

        if keyword in keyDictionary:
            keyCount = keyDictionary[keyword]
            keyCount = keyCount + 1
            keyDictionary[keyword] = keyCount
        else:
            keyDictionary[keyword] = 1

        #{keyword:keyCount}
             
    # print(keyDictionary)

    for key,value in keyDictionary.iteritems():
        resultwriter.writerow([key, value])
   # print(value, key)
    

