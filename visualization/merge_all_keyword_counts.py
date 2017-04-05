# empty diction, which will eventually be our results
results = {}

# data directory
directory = "data_keywords_count/"

# the collection of Keyword Dictionary CSV files we want to work with
files = ["2000keyDict.csv", "2001keyDict.csv","2002keyDict.csv", "2003keyDict.csv",
         "2004keyDict.csv", "2005keyDict.csv", "2006keyDict.csv", "2007keyDict.csv",
         "2008keyDict.csv", "2009keyDict.csv", "2010keyDict.csv", "2011keyDict.csv",
         "2012keyDict.csv", "2013keyDict.csv", "2014keyDict.csv", "2015keyDict.csv"] 

# the range of keywords we're interested in
# for instance, 1600 to 1699 if we want to limit the results to Global Change
# 0 to 9999 if we want everything
start = int(input("Enter starting keyword value: "))
end = int(input("Enter ending keyword value: "))

# the CSV file containing all possible AGU keywords
# we use this for reference
keywordFile = open("all_agu_keywords.csv", "r")
for line in keywordFile:

    # each line has three parts, we only care about the second value - keyword #
    parts = line.split(",")
    keyword = int(parts[1].strip())

    # is this keyword in the range we're interested in?
    if ( (keyword >= start) and (keyword <= end) ):
        
        # print out a status update so we know where we are
        statusLine = "Working on keyword " + str(keyword) + "..."
        print(statusLine)
        
        # loop over all the keyword dictionary files
        for f in files:
            keyDictFile = open(directory + f, "r")
        
            # get the year from the filename
            year = int(f[0:4])

            # variable to hold the number of times we saw this keyword each year
            # reset to zero before we start a new year
            count = 0

            # within each keyword dictionary file loop over all the lines in the file
            for l in keyDictFile:

                # split the line into parts, remove whitespaces
                parts = l.split(",")
                k = int(parts[0].strip())
                keywordCount = int(parts[1].strip())

                # now check if it's equal to our current place on the reference list
                if ( k == keyword ):
                    count = keywordCount

            # reached end of the year file
            if (year == 2000):
                results[keyword] = str(year) + ":" + str(count)
            else:
                v = results[keyword]
                results[keyword] = v + "," + str(year) + ":" + str(count)

# ok, now we have all the data, let's output it to another CSV file
outFile = open("all_agu_keyword_counts_all_years.csv", "w")

# iterating over a dictionary changed from Python 2 to Python 3
# here we list both ways so this code will run in either environment, just uncomment

#for key, value in results.iteritems(): # python 2.x
for key, value in results.items(): # python 3.x

    outputLine = str(key)
    
    # data has the form - year:keywordCount,year:KeywordCount
    
    # value contains all years, break this apart to individual years
    parts = value.split(",")

    # loop over all the individual years
    for v in parts:
        
        # still need to do more separating
        moreParts = v.split(":")
        year = moreParts[0].strip()
        count = moreParts[1].strip()
        outputLine = outputLine + "," + count

    # write the line to the output file
    outputLine = outputLine + "\n"
    outFile.write(outputLine)

# close the output file
outFile.close()
        
