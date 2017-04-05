# the collection of Keyword CSV files we want to work with
directory = "data_keywords_section/"
files = ["2000keyword.csv", "2001keyword.csv", "2002keyword.csv", "2003keyword.csv",
         "2004keyword.csv", "2005keyword.csv", "2006keyword.csv", "2007keyword.csv",
         "2008keyword.csv", "2009keyword.csv", "2010keyword.csv", "2011keyword.csv",
         "2012keyword.csv", "2013keyword.csv", "2014keyword.csv", "2015keyword.csv"] 

# get the range of keywords
keywordRange = [1600, 1605, 1610, 1615, 1616, 1620, 1621, 1622, 1625, 1626, 1627, 1630,
                1631, 1632, 1635, 1637, 1640, 1641, 1645, 1650, 1655, 1694, 1699]

# get the section from the user
section = str(input("Enter the section of interest: "))

# rows and columns
row = 1
column = 1
counter = 0

# output to tsv
filename = "heatmap_" + section + ".tsv"
outFile = open(filename, "w")
outFile.write( "day\thour\tvalue\n" )

# loop over the keywords we're looking for
for k in keywordRange:

    # status update
    print("Working on keyword: " + str(k))

    # loop over all the keyword files
    for f in files:
        
        # within each keyword file loop over all the lines in the file
        # read the next file
        keyFile = open(directory+f, "r")
        for l in keyFile:
                
            # split the line into parts, remove whitespaces
            parts = l.split(",")
            keywordNumber = int(parts[0].strip())
            sectionInFile = parts[1].strip()
            if ( (sectionInFile == section) and (k == keywordNumber) ):
                counter = counter + 1

        # output to file
        line = str(row) + "\t" + str(column) + "\t" + str(counter) + "\n"
        outFile.write( line )

        # next column
        column = column + 1
        counter = 0
        
    # increment and reset
    row = row + 1
    column = 1
    
# close the output file
outFile.close()
        
