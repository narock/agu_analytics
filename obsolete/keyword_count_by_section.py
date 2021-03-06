# empty dictionary, which will eventually be our results
results = {}

# the collection of Keyword CSV files we want to work with
directory = "data_keywords_section/"
files = ["2000keyword.csv", "2001keyword.csv", "2002keyword.csv", "2003keyword.csv",
         "2004keyword.csv", "2005keyword.csv", "2006keyword.csv", "2007keyword.csv",
         "2008keyword.csv", "2009keyword.csv", "2010keyword.csv", "2011keyword.csv",
         "2012keyword.csv", "2013keyword.csv", "2014keyword.csv", "2015keyword.csv"] 

# get the range of keywords from the user
start = int(input("Enter starting keyword number: "))
end = int(input("Enter ending keyword number: "))

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

        # is it in the range we're looking for?
        if ( (keywordNumber >= start) and (keywordNumber <= end) ):
            if ( sectionInFile in results ):
                count = results[sectionInFile]
                count = count + 1
                results[sectionInFile] = count
            else:
                results[sectionInFile] = 1
                
# ok, now we have all the data, let's output it to another CSV file
filename = "agu_keywords_by_section.csv"
outFile = open(filename, "w")

# this only works in Python 3.x
# iterating over dictionary and sorting is different in Python 2.x
for key, value in results.items(): # python 3.x
        
    line = str(key) + "\t" + str(value) + "\n"
    outFile.write( line )

# close the output file
outFile.close()
        
