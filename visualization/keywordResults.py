def updateDictionary( dictionary, keyword ):
    p = keyword.split("/")
    l = len(p)
    k = int(p[l-1])
    # from http://abstractsearch.agu.org/keywords/
    if ( (k>=300) and (k<400) ):
        r = "300"
    if ( (k>=400) and (k<500) ):
        r = "400"
    if ( (k>=500) and (k<600) ):
        r = "500"
    if ( (k>=600) and (k<700) ):
        r = "600"
    if ( (k>=700) and (k<800) ):
        r = "700"
    if ( (k>=800) and (k<900) ):
        r = "800"
    if ( (k>=900) and (k<1000) ):
        r = "900"
    if ( (k>=1000) and (k<1100) ):
        r = "1000"
    if ( (k>=1100) and (k<1200) ):
        r = "1100"
    if ( (k>=1200) and (k<1300) ):
        r = "1200"
    if ( (k>=1500) and (k<1600) ):
        r = "1500"
    if ( (k>=1600) and (k<1700) ):
        r = "1600"
    if ( (k>=1700) and (k<1800) ):
        r = "1700"
    if ( (k>=1800) and (k<1900) ):
        r = "1800"
    if ( (k>=1900) and (k<2000) ):
        r = "1900"
    if ( (k>=2100) and (k<2200) ):
        r = "2100"
    if ( (k>=2400) and (k<2500) ):
        r = "2400"
    if ( (k>=2700) and (k<2800) ):
        r = "2700"
    if ( (k>=3000) and (k<3100) ):
        r = "3000"
    if ( (k>=3200) and (k<3300) ): # 20
        r = "3200"
    if ( (k>=3300) and (k<3400) ):
        r = "3300"
    if ( (k>=3600) and (k<3700) ):
        r = "3600"
    if ( (k>=3900) and (k<4000) ):
        r = "3900"
    if ( (k>=4200) and (k<4300) ):
        r = "4200"
    if ( (k>=4300) and (k<4400) ):
        r = "4300"
    if ( (k>=4400) and (k<4500) ):
        r = "4400"
    if ( (k>=4500) and (k<4600) ):
        r = "4500"
    if ( (k>=4800) and (k<4900) ):
        r = "4800"
    if ( (k>=4900) and (k<5000) ):
        r = "4900"
    if ( (k>=5100) and (k<5200) ): # 30
        r = "5100"
    if ( (k>=5200) and (k<5300) ):
        r = "5200"
    if ( (k>=5400) and (k<5500) ):
        r = "5400"
    if ( (k>=5700) and (k<5800) ):
        r = "5700"
    if ( (k>=6000) and (k<6100) ):
        r = "6000"
    if ( (k>=6200) and (k<6300) ):
        r = "6200"
    if ( (k>=6300) and (k<6400) ):
        r = "6300"
    if ( (k>=6600) and (k<6700) ):
        r = "6600"
    if ( (k>=6900) and (k<7000) ):
        r = "6900"
    if ( (k>=7200) and (k<7300) ):
        r = "7200"
    if ( (k>=7500) and (k<7600) ): # 40
        r = "7500"
    if ( (k>=7800) and (k<7900) ):
        r = "7800"
    if ( (k>=7900) and (k<8000) ):
        r = "7900"
    if ( (k>=8000) and (k<8100) ):
        r = "8000"
    if ( (k>=8100) and (k<8200) ):
        r = "8100"
    if ( (k>=8400) and (k<8500) ):
        r = "8400"
    if ( (k>=9300) and (k<9400) ):
        r = "9300"
    if ( (k>=9600) and (k<9700) ):
        r = "9600"
    if ( (k>=9800) and (k<9900) ): # 48
        r = "9800"

    if ( r in dictionary ):
        count = dictionary[r] + 1
        dictionary[r] = count
    else:
        dictionary[r] = 1
        
file1="/Users/narock/University/Projects/agu_analytics/esip_summer_2017/MeetingAttendeeData/csv/results/results_summer/keywordResults.csv"
file2="/Users/narock/University/Projects/agu_analytics/esip_summer_2017/MeetingAttendeeData/csv/results/results_winter/keywordResults.csv"
files = [file1, file2]

abstracts = []
keywords2010 = {}
keywords2011 = {}
keywords2012 = {}
keywords2013 = {}
keywords2014 = {}
keywords2015 = {}
keywords2016 = {}

for f in files:

    inFile = open(f, "r")
    
    for line in inFile:
        
        parts = line.split(",")
        year = parts[0].strip()
        abstract = parts[1].strip()
        keyword = parts[2].strip()

        if ( abstract not in abstracts ):

            if ( year == "2010" ):
                updateDictionary( keywords2010, keyword )
            if ( year == "2011" ):
                updateDictionary( keywords2011, keyword )
            if ( year == "2012" ):
                updateDictionary( keywords2012, keyword )
            if ( year == "2013" ):
                updateDictionary( keywords2013, keyword )
            if ( year == "2014" ):
                updateDictionary( keywords2014, keyword )
            if ( year == "2015" ):
                updateDictionary( keywords2015, keyword )
            if ( year == "2016" ):
                updateDictionary( keywords2016, keyword )

        abstracts.append(abstract)

print(" ")
print("2010")
for key, value in keywords2010.iteritems():
    print("  ",key,value)
print("2011")
for key, value in keywords2011.iteritems():
    print("  ",key,value)
print("2012")
for key, value in keywords2012.iteritems():
    print("  ",key,value)
print("2013")
for key, value in keywords2013.iteritems():
    print("  ",key,value)
print("2014")
for key, value in keywords2014.iteritems():
    print("  ",key,value)
print("2015")
for key, value in keywords2015.iteritems():
    print("  ",key,value)
print("2016")
for key, value in keywords2016.iteritems():
    print("  ",key,value)
        
        

