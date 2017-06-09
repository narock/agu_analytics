def updateDictionary( dictionary, section ):
    p = section.split("/")
    l = len(p)
    s = p[l-1]
    if ( s in dictionary.keys() ):
        count = dictionary[s] + 1
        dictionary[s] = count
    else:
        dictionary[s] = 1
        
file1="/Users/narock/University/Projects/agu_analytics/esip_summer_2017/MeetingAttendeeData/csv/results/results_summer/sectionResults.csv"
file2="/Users/narock/University/Projects/agu_analytics/esip_summer_2017/MeetingAttendeeData/csv/results/results_winter/sectionResults.csv"
files = [file1, file2]

abstracts = []
sections2010 = {}
sections2011 = {}
sections2012 = {}
sections2013 = {}
sections2014 = {}
sections2015 = {}
sections2016 = {}

for f in files:

    inFile = open(f, "r")
    
    for line in inFile:
        
        parts = line.split(",")
        year = parts[0].strip()
        abstract = parts[1].strip()
        section = parts[2].strip()

        if ( abstract not in abstracts ):

            if ( year == "2010" ):
                updateDictionary( sections2010, section )
            if ( year == "2011" ):
                updateDictionary( sections2011, section )
            if ( year == "2012" ):
                updateDictionary( sections2012, section )
            if ( year == "2013" ):
                updateDictionary( sections2013, section )
            if ( year == "2014" ):
                updateDictionary( sections2014, section )
            if ( year == "2015" ):
                updateDictionary( sections2015, section )
            if ( year == "2016" ):
                updateDictionary( sections2016, section )

        abstracts.append(abstract)

print(" ")
print("2010")
for key, value in sections2010.iteritems():
    print("  ",key,value)
print("2011")
for key, value in sections2011.iteritems():
    print("  ",key,value)
print("2012")
for key, value in sections2012.iteritems():
    print("  ",key,value)
print("2013")
for key, value in sections2013.iteritems():
    print("  ",key,value)
print("2014")
for key, value in sections2014.iteritems():
    print("  ",key,value)
print("2015")
for key, value in sections2015.iteritems():
    print("  ",key,value)
print("2016")
for key, value in sections2016.iteritems():
    print("  ",key,value)
        
        

