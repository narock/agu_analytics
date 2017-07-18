def updateDictionary( dictionary, keyword ):

    k = int(keyword)
    r = -1
    
    # from http://abstractsearch.agu.org/keywords/
    if ( (k>=300) and (k<400) ):
        r = 300
    if ( (k>=400) and (k<500) ):
        r = 400
    if ( (k>=500) and (k<600) ):
        r = 500
    if ( (k>=600) and (k<700) ):
        r = 600
    if ( (k>=700) and (k<800) ):
        r = 700
    if ( (k>=800) and (k<900) ):
        r = 800
    if ( (k>=900) and (k<1000) ):
        r = 900
    if ( (k>=1000) and (k<1100) ):
        r = 1000
    if ( (k>=1100) and (k<1200) ):
        r = 1100
    if ( (k>=1200) and (k<1300) ):
        r = 1200
    if ( (k>=1500) and (k<1600) ):
        r = 1500
    if ( (k>=1600) and (k<1700) ):
        r = 1600
    if ( (k>=1700) and (k<1800) ):
        r = 1700
    if ( (k>=1800) and (k<1900) ):
        r = 1800
    if ( (k>=1900) and (k<2000) ):
        r = 1900
    if ( (k>=2100) and (k<2200) ):
        r = 2100
    if ( (k>=2400) and (k<2500) ):
        r = 2400
    if ( (k>=2700) and (k<2800) ):
        r = 2700
    if ( (k>=3000) and (k<3100) ):
        r = 3000
    if ( (k>=3200) and (k<3300) ): # 20
        r = 3200
    if ( (k>=3300) and (k<3400) ):
        r = 3300
    if ( (k>=3600) and (k<3700) ):
        r = 3600
    if ( (k>=3900) and (k<4000) ):
        r = 3900
    if ( (k>=4200) and (k<4300) ):
        r = 4200
    if ( (k>=4300) and (k<4400) ):
        r = 4300
    if ( (k>=4400) and (k<4500) ):
        r = 4400
    if ( (k>=4500) and (k<4600) ):
        r = 4500
    if ( (k>=4800) and (k<4900) ):
        r = 4800
    if ( (k>=4900) and (k<5000) ):
        r = 4900
    if ( (k>=5100) and (k<5200) ): # 30
        r = 5100
    if ( (k>=5200) and (k<5300) ):
        r = 5200
    if ( (k>=5400) and (k<5500) ):
        r = 5400
    if ( (k>=5700) and (k<5800) ):
        r = 5700
    if ( (k>=6000) and (k<6100) ):
        r = 6000
    if ( (k>=6200) and (k<6300) ):
        r = 6200
    if ( (k>=6300) and (k<6400) ):
        r = 6300
    if ( (k>=6600) and (k<6700) ):
        r = 6600
    if ( (k>=6900) and (k<7000) ):
        r = 6900
    if ( (k>=7200) and (k<7300) ):
        r = 7200
    if ( (k>=7500) and (k<7600) ): # 40
        r = 7500
    if ( (k>=7800) and (k<7900) ):
        r = 7800
    if ( (k>=7900) and (k<8000) ):
        r = 7900
    if ( (k>=8000) and (k<8100) ):
        r = 8000
    if ( (k>=8100) and (k<8200) ):
        r = 8100
    if ( (k>=8400) and (k<8500) ):
        r = 8400
    if ( (k>=9300) and (k<9400) ):
        r = 9300
    if ( (k>=9600) and (k<9700) ):
        r = 9600
    if ( (k>=9800) and (k<9900) ): # 48
        r = 9800

    if ( r != -1 ):
        if ( r in dictionary ):
            count = dictionary[r] + 1
            dictionary[r] = count
        else:
            dictionary[r] = 1
        
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

sections = {"A":"Atmospheric Sciences", "AE":"Atmospheric and Space Electricity", "B":"Biogeosciences", "C":"Cryosphere",
            "DI":"Study of the Earth's Deep Interior","ED":"Education and Human Resources",
            "EP":"Earth and Planetary Surface Processes", "G":"Geodesy", "GC":"Global Environment Change",
            "GP":"Geomagnetism and Paleomagnetism", "H":"Hydrology", "IN":"Earth and Space Science Informatics",
            "MR":"Mineral and Rock Physics", "NG":"Nonlinear Geophysics", "NH":"Natural Hazards",
            "NS":"Near Surface Geophysics", "OS":"Ocean Sciences", "P":"Planetary Sciences", "PA":"Public Affairs",
            "PP":"Paleoceanography and Paleoclimatology", "S":"Seismology", "SA":"SPA-Aeronomy",
            "SH":"SPA-Solar and Heliospheric Physics", "SM":"SPA-Magnetospheric Physics", "T":"Tectonophysics",
            "U":"Union", "V":"Volcanology Geochemistry Petrology"}

for key, value in sections.iteritems():

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

    print("Working on " + key)

    for f in files:

        inFile = open(f, "r")

        parts = f.split("/")
        n = len(parts)-1
        fname = parts[n]
        year = fname[0:4]

        for line in inFile:
        
            parts = line.split(",")
            keyword = parts[0].strip()
            section = parts[1].strip()

            if ( section == key ):
                
                if ( year == "2000" ):
                    updateDictionary( keywords2000, keyword )
                if ( year == "2001" ):
                    updateDictionary( keywords2001, keyword )
                if ( year == "2002" ):
                    updateDictionary( keywords2002, keyword )
                if ( year == "2003" ):
                    updateDictionary( keywords2003, keyword )
                if ( year == "2004" ):
                    updateDictionary( keywords2004, keyword )
                if ( year == "2005" ):
                    updateDictionary( keywords2005, keyword )
                if ( year == "2006" ):
                    updateDictionary( keywords2006, keyword )
                if ( year == "2007" ):
                    updateDictionary( keywords2007, keyword )
                if ( year == "2008" ):
                    updateDictionary( keywords2008, keyword )
                if ( year == "2009" ):
                    updateDictionary( keywords2009, keyword )               
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

    keys = [300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1500, 1600, 1700, 1800, 1900, 2100, 2400,
        2700, 3000, 3200, 3300, 3600, 3900, 4200, 4300, 4400, 4500, 4800, 4900, 5100, 5200, 5400, 5700,
        6000, 6200, 6300, 6600, 6900, 7200, 7500, 7800, 7900, 8000, 8100, 8400, 9300, 9600, 9800]

    f = open("section_level_heatmap_" + key + ".tsv", 'w')
    f.write("day\thour\tvalue\n")
    row = 1
    column = 1

    for key in keys:
        for d in allDicts:
            if (key in d.keys() ):
                f.write(str(row) + "\t" + str(column) + "\t" + str(d[key]) + "\n" )
            else:
                f.write(str(row) + "\t" + str(column) + "\t" + "0\n" )
            column = column + 1
        row = row + 1
        column = 1
        
    f.close()

        
        

