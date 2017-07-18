def updateDictionary( dictionary, k ):

    if ( k in dictionary ):
        count = dictionary[k] + 1
        dictionary[k] = count
    else:
        dictionary[k] = 1

def timeSeries ( topicStart, topicStop ):

    print("Topic: " + str(topicStart))
    
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

            if ( ( int(keyword) >= int(topicStart) ) and ( int(keyword) < int(topicStop) ) ):

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

    f = open("topic_level_timeseries_" + str(topicStart) + ".json", 'w')
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

timeSeries( 300, 400 )
timeSeries( 400, 500 )
timeSeries( 500, 600 )
timeSeries( 600, 700 )
timeSeries( 700, 800 )
timeSeries( 800, 900 )
timeSeries( 900, 1000 )
timeSeries( 1000, 1100 )
timeSeries( 1100, 1200 )
timeSeries( 1200, 1300 ) # 10
timeSeries( 1500, 1600 )
timeSeries( 1600, 1700 )
timeSeries( 1700, 1800 )
timeSeries( 1800, 1900 )
timeSeries( 1900, 2000 ) # 15
timeSeries( 2100, 2200 ) 
timeSeries( 2400, 2500 )
timeSeries( 2700, 2800 ) 
timeSeries( 3000, 3100 )
timeSeries( 3200, 3300 )
timeSeries( 3300, 3400 )
timeSeries( 3600, 3700 )
timeSeries( 3900, 4000 )
timeSeries( 4200, 4300 )
timeSeries( 4300, 4400 ) #25
timeSeries( 4400, 4500 )
timeSeries( 4500, 4600 )
timeSeries( 4800, 4900 )
timeSeries( 4900, 5000 )
timeSeries( 5100, 5200 )
timeSeries( 5200, 5300 )
timeSeries( 5400, 5500 )
timeSeries( 5700, 5800 )
timeSeries( 6000, 6100 )
timeSeries( 6200, 6300 ) # 35
timeSeries( 6300, 6400 )
timeSeries( 6600, 6700 )
timeSeries( 6900, 7000 )
timeSeries( 7200, 7300 )
timeSeries( 7500, 7600 )
timeSeries( 7800, 7900 )
timeSeries( 7900, 8000 )
timeSeries( 8000, 8100 )
timeSeries( 8100, 8200 )
timeSeries( 8400, 8500 ) # 45
timeSeries( 9300, 9400 )
timeSeries( 9600, 9700 )
timeSeries( 9800, 9900 )
