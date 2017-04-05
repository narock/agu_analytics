def updateDictionary (dictionary, keyword):
    if (keyword in dictionary):
        r = dictionary[keyword]
        dictionary[keyword] = r + 1
    else:
        dictionary[keyword] = 1
        
# empty dictionaries, which will eventually be our results
r2000 = {}
r2001 = {}
r2002 = {}
r2003 = {}
r2004 = {}
r2005 = {}
r2006 = {}
r2007 = {}
r2008 = {}
r2009 = {}
r2010 = {}
r2011 = {}
r2012 = {}
r2013 = {}
r2014 = {}
r2015 = {}

# the collection of Keyword CSV files we want to work with
directory = "data_keywords_section/"
files = ["2000keyword.csv", "2001keyword.csv", "2002keyword.csv", "2003keyword.csv",
         "2004keyword.csv", "2005keyword.csv", "2006keyword.csv", "2007keyword.csv",
         "2008keyword.csv", "2009keyword.csv", "2010keyword.csv", "2011keyword.csv",
         "2012keyword.csv", "2013keyword.csv", "2014keyword.csv", "2015keyword.csv"] 

# get the section from the user
section = str(input("Enter the section of interest: "))

# the CSV file containing all possible AGU keywords
# we use this for reference
keywordFile = open("all_agu_keywords.csv", "r")
for line in keywordFile:

    # each line has three parts, we only care about the second value - keyword #
    parts = line.split(",")
    keyword = int(parts[1].strip())

    # print out a status update so we know where we are
    statusLine = "Working on keyword " + str(keyword) + "..."
    print(statusLine)
            
    # loop over all the keyword files
    for f in files:

            # read the next file
            keyFile = open(directory+f, "r")
        
            # get the year from the filename
            year = int(f[0:4])

            # within each keyword file loop over all the lines in the file
            for l in keyFile:

                # split the line into parts, remove whitespaces
                parts = l.split(",")
                keywordNumber = int(parts[0].strip())
                sectionInFile = parts[1].strip()

                # update the results dictionary
                if ( (sectionInFile == section) and (keywordNumber == keyword) ):
                    if (year == 2000):
                        updateDictionary(r2000, keyword)
                    elif ( year == 2001):
                        updateDictionary(r2001, keyword)
                    elif ( year == 2002):
                        updateDictionary(r2002, keyword)
                    elif ( year == 2003):
                        updateDictionary(r2003, keyword)
                    elif ( year == 2004):
                        updateDictionary(r2004, keyword)
                    elif ( year == 2005):
                        updateDictionary(r2005, keyword)
                    elif ( year == 2006):
                        updateDictionary(r2006, keyword)
                    elif ( year == 2007):
                        updateDictionary(r2007, keyword)
                    elif ( year == 2008):
                        updateDictionary(r2008, keyword)
                    elif ( year == 2009):
                        updateDictionary(r2009, keyword)
                    elif ( year == 2010):
                        updateDictionary(r2010, keyword)
                    elif ( year == 2011):
                        updateDictionary(r2011, keyword)
                    elif ( year == 2012):
                        updateDictionary(r2012, keyword)
                    elif ( year == 2013):
                        updateDictionary(r2013, keyword)
                    elif ( year == 2014):
                        updateDictionary(r2014, keyword)
                    else:
                        updateDictionary(r2015, keyword)

# ok, now we have all the data, let's output it to another CSV file
filename = "agu_keywords_section_" + section.strip() + ".csv"
outFile = open(filename, "w")

# list containing all dictionaries
year = 2000
results = [r2000, r2001, r2002, r2003, r2004, r2005, r2006, r2007, r2008, r2009, r2010,
           r2011, r2012, r2013, r2014, r2015]

for r in results:

    # this only works in Python 3.x
    # iterating over dictionary and sorting is different in Python 2.x
    for key, value in sorted(r.items()): # python 3.x
        
        line = str(year) + "," + str(key) + "," + str(r[key]) + "\n"
        outFile.write( line )

    year = year + 1

# close the output file
outFile.close()
        
