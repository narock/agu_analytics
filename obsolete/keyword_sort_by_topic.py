def mapper( keyword ):
        result = ""
        keywordFile = open("all_agu_keywords.csv", "r")
        for line in keywordFile:
            parts = line.split(",")
            k = int(parts[1].strip())
            name = parts[2].strip()
            if ( keyword == k ):
                    result = name
        return result

# the range of keywords we're interested in
# for instance, 1600 to 1699 if we want to limit the results to Global Change
# 0 to 9999 if we want everything
start = int(input("Enter starting keyword value: "))
end = int(input("Enter ending keyword value: "))

# setup output JSON
outFile = open("keyword_timeseries.json", "w")
outFile.write("{   ")
counter = 0

# input data file
inFile = open("all_agu_keyword_counts_all_years.csv", "r")

# loop over all the lines in the file
for line in inFile:

        # get the keyword, first value
        parts = line.split(",")
        keyword = int(parts[0].strip())

        # check if it's in our range
        if ( (keyword >= start) and (keyword <= end) ):

                if counter == 0:
                        outline = '    "' + mapper(keyword) + '": ['
                else:
                        outline = outline + '    "' + mapper(keyword) + '": ['

                # skip the 1st value, we already got it
                for p in parts[1:]:
                        outline = outline + str(p).strip() + ','
                outline = outline[:-1] # remove last character, in this case unneeded ,
                outline = outline + "],\n"
                counter = counter + 1

outline = outline.strip()
outline = outline[:-1] # remove last character, in this case unneeded ,
outFile.write(outline)
outFile.write("\n}")
                
outFile.close()

