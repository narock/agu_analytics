import json
import glob

inDir = '/Users/narock/Desktop/AGU_Graph/keywords/section_level_timeseries_*_'
outDir = '/Users/narock/Desktop/AGU_Graph/keyword_totals/'

keywordGroups = ["300", "400", "500", "600", "700", "800", "900", "1000", "1100", "1200", "1500",
                 "1600", "1700", "1800", "1900", "2100", "2400", "2700", "3000", "3200", "3300",
                 "3600", "3900", "4200", "4300", "4400", "4500", "4800", "4900", "5100", "5200",
                 "5400", "5700", "6000", "6200", "6300", "6600", "6900", "7200", "7500", "7800",
                 "7900", "8000", "8100", "8400", "9300", "9600", "9800"]

# loop over all the keyword groups
for group in keywordGroups:

    # status update
    print("Working on group:", group)
    
    # glob all the files for this section
    files = glob.glob(inDir + group + '.json')
    files.sort()

    # iterate over all the files
    for file in files:

        # open the file and read the JSON
        with open(file) as f:
            data = json.load(f)

        # get the section name from the filename
        parts = file.split("_")
        section = parts[4].strip()
        
        # list to hold the yearly usage of the keywords
        yearlySums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        # count up how many times the keywords were used
        for key in data:
            lst = data[key]
            for i in range( len(yearlySums) ):
                yearlySums[i] += lst[i]

        # write the results to a file
        outFile = outDir + 'totals_' + group + '.csv'
        of = open(outFile, 'a')
        line = section + "," 
        for v in yearlySums:
            line += str(v) + ","
        line = line[:-1] + "\n"
        of.write(line)
        of.close()

