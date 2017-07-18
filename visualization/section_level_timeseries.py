def updateDictionary( dictionary, k ):

    if ( k in dictionary ):
        count = dictionary[k] + 1
        dictionary[k] = count
    else:
        dictionary[k] = 1

def timeSeries ( topicStart, topicStop, sectionID ):

    print("Topic: " + str(topicStart) + " for " + sectionID)
    
    d="/Users/narock/University/Projects/agu_analytics/data_keywords_section/"
    f01 = d + "2000keyword.csv"
    f02 = d + "2001keyword.csv"
    f03 = d + "2002keyword.csv"
    f04 = d + "2003keyword.csv"
    f05 = d + "2004keyword.csv"
    f06 = d + "2005keyword.csv"
    f07 = d + "2006keyword.csv"
    f08 = d + "2007keyword.csv"
    f09 = d + "2008keyword.csv"
    f10 = d + "2009keyword.csv"
    f11 = d + "2010keyword.csv"
    f12 = d + "2011keyword.csv"
    f13 = d + "2012keyword.csv"
    f14 = d + "2013keyword.csv"
    f15 = d + "2014keyword.csv"
    f16 = d + "2015keyword.csv"
    f17 = d + "2016keyword.csv"
    files = [f01, f02, f03, f04, f05, f06, f07, f08, f09, f10, f11, f12, f13, f14, f15, f16, f17]

    keywords2000 = {}
    keywords2001 = {}
    keywords2002 = {}
    keywords2003 = {}
    keywords2004 = {}
    keywords2005 = {}
    keywords2006 = {}
    keywords2007 = {}
    keywords2008 = {}
    keywords2009 = {}
    keywords2010 = {}
    keywords2011 = {}
    keywords2012 = {}
    keywords2013 = {}
    keywords2014 = {}
    keywords2015 = {}
    keywords2016 = {}
    allDicts = [keywords2000, keywords2001, keywords2002, keywords2003, keywords2004, keywords2005, keywords2006,
            keywords2007, keywords2008, keywords2009, keywords2010, keywords2011, keywords2012, keywords2013,
            keywords2014, keywords2015, keywords2016]
    
    for f in files:

        print("  Working on " + f)
        inFile = open(f, "r")

        parts = f.split("/")
        n = len(parts)-1
        fname = parts[n]
        year = fname[0:4]

        for line in inFile:
        
            parts = line.split(",")
            keyword = parts[0].strip()
            section = parts[1].strip()

            if ( ( int(keyword) >= int(topicStart) ) and ( int(keyword) < int(topicStop) ) and (section == sectionID) ):

                # find the keyword in the keywords file
                keywordName = ""
                keyfile = open("../agu_data/all_agu_keywords.csv", "r")
                for l in keyfile:
                    p = l.split(",")
                    keyNumber = p[1].strip()
                    keyName = p[2].strip()
                    if ( int(keyNumber) == int(keyword) ):
                        keywordName = keyName
                        break
                keyfile.close()
                        
                if ( year == "2000" ):
                    updateDictionary( keywords2000, keywordName )
                if ( year == "2001" ):
                    updateDictionary( keywords2001, keywordName )
                if ( year == "2002" ):
                    updateDictionary( keywords2002, keywordName )
                if ( year == "2003" ):
                    updateDictionary( keywords2003, keywordName )
                if ( year == "2004" ):
                    updateDictionary( keywords2004, keywordName )
                if ( year == "2005" ):
                    updateDictionary( keywords2005, keywordName )
                if ( year == "2006" ):
                    updateDictionary( keywords2006, keywordName )
                if ( year == "2007" ):
                    updateDictionary( keywords2007, keywordName )
                if ( year == "2008" ):
                    updateDictionary( keywords2008, keywordName )
                if ( year == "2009" ):
                    updateDictionary( keywords2009, keywordName )               
                if ( year == "2010" ):
                    updateDictionary( keywords2010, keywordName )
                if ( year == "2011" ):
                    updateDictionary( keywords2011, keywordName )
                if ( year == "2012" ):
                    updateDictionary( keywords2012, keywordName )
                if ( year == "2013" ):
                    updateDictionary( keywords2013, keywordName )
                if ( year == "2014" ):
                    updateDictionary( keywords2014, keywordName )
                if ( year == "2015" ):
                    updateDictionary( keywords2015, keywordName )
                if ( year == "2016" ):
                    updateDictionary( keywords2016, keywordName )

    f = open("section_level_timeseries_" + str(sectionID) + "_" + str(topicStart) + ".json", 'w')
    f.write("{\n")

    outString = ""
    keyfile = open("../agu_data/all_agu_keywords.csv", "r")
    for l in keyfile:
        p = l.split(",")
        keyNumber = p[1].strip()
        keyName = p[2].strip()
        if ( ( int(keyNumber) >= int(topicStart) ) and ( int(keyNumber) < int(topicStop) ) ):
            outString = outString + "\"" + keyName + "\": ["
            count = 0
            length = len(allDicts)
            for d in allDicts:
                if (keyName in d.keys() ):
                    outString = outString + str(d[keyName])
                else:
                    outString = outString + "0" 
                if ( count < length-1 ):
                    outString = outString + ","
                count = count + 1
            outString = outString + "],\n"

    outString = outString[:-2]
    f.write(outString+"\n")
    f.write("}\n")
    f.close()
    keyfile.close()

sections = {"A":"Atmospheric Sciences", "AE":"Atmospheric and Space Electricity", "B":"Biogeosciences", "C":"Cryosphere",
            "DI":"Study of the Earth's Deep Interior","ED":"Education and Human Resources",
            "EP":"Earth and Planetary Surface Processes", "G":"Geodesy", "GC":"Global Environment Change",
            "GP":"Geomagnetism and Paleomagnetism", "H":"Hydrology", "IN":"Earth and Space Science Informatics",
            "MR":"Mineral and Rock Physics", "NG":"Nonlinear Geophysics", "NH":"Natural Hazards",
            "NS":"Near Surface Geophysics", "OS":"Ocean Sciences", "P":"Planetary Sciences", "PA":"Public Affairs",
            "PP":"Paleoceanography and Paleoclimatology", "S":"Seismology", "SA":"SPA-Aeronomy",
            "SH":"SPA-Solar and Heliospheric Physics", "SM":"SPA-Magnetospheric Physics", "T":"Tectonophysics",
            "U":"Union", "V":"Volcanology Geochemistry Petrology"}

for sectionID, sectionName in sections.iteritems():
    timeSeries( 300, 400, sectionID )
    timeSeries( 400, 500, sectionID )
    timeSeries( 500, 600, sectionID )
    timeSeries( 600, 700, sectionID )
    timeSeries( 700, 800, sectionID )
    timeSeries( 800, 900, sectionID )
    timeSeries( 900, 1000, sectionID )
    timeSeries( 1000, 1100, sectionID )
    timeSeries( 1100, 1200, sectionID )
    timeSeries( 1200, 1300, sectionID ) # 10
    timeSeries( 1500, 1600, sectionID ) 
    timeSeries( 1600, 1700, sectionID )
    timeSeries( 1700, 1800, sectionID )
    timeSeries( 1800, 1900, sectionID )
    timeSeries( 1900, 2000, sectionID ) # 15
    timeSeries( 2100, 2200, sectionID ) 
    timeSeries( 2400, 2500, sectionID )
    timeSeries( 2700, 2800, sectionID ) 
    timeSeries( 3000, 3100, sectionID )
    timeSeries( 3200, 3300, sectionID )
    timeSeries( 3300, 3400, sectionID )
    timeSeries( 3600, 3700, sectionID )
    timeSeries( 3900, 4000, sectionID )
    timeSeries( 4200, 4300, sectionID )
    timeSeries( 4300, 4400, sectionID ) #25
    timeSeries( 4400, 4500, sectionID )
    timeSeries( 4500, 4600, sectionID )
    timeSeries( 4800, 4900, sectionID )
    timeSeries( 4900, 5000, sectionID )
    timeSeries( 5100, 5200, sectionID )
    timeSeries( 5200, 5300, sectionID )
    timeSeries( 5400, 5500, sectionID )
    timeSeries( 5700, 5800, sectionID )
    timeSeries( 6000, 6100, sectionID )
    timeSeries( 6200, 6300, sectionID ) # 35
    timeSeries( 6300, 6400, sectionID )
    timeSeries( 6600, 6700, sectionID )
    timeSeries( 6900, 7000, sectionID )
    timeSeries( 7200, 7300, sectionID )
    timeSeries( 7500, 7600, sectionID )
    timeSeries( 7800, 7900, sectionID )
    timeSeries( 7900, 8000, sectionID )
    timeSeries( 8000, 8100, sectionID )
    timeSeries( 8100, 8200, sectionID )
    timeSeries( 8400, 8500, sectionID ) # 45
    timeSeries( 9300, 9400, sectionID )
    timeSeries( 9600, 9700, sectionID )
    timeSeries( 9800, 9900, sectionID )
