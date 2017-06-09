def coAuthorCounts( nameList ):

    names = nameList.split(",")
    result = dict( (x, names.count(x)) for x in set(names))
    return result
    
def keywordCount( files, abstracts ):

    keywords = []
    abstractsSeen = []
    for f in files:

        inFile = open(f, "r")
        for line in inFile:

            parts = line.split(",")
            year = parts[0].strip()
            abstract = parts[1].strip()
            k = parts[2].strip()

            if ( (abstract in abstracts) and (abstract not in abstractsSeen) ):
                keywords.append(k)
                abstractsSeen.append(abstract)

    counts = [0] * 97
    for keyword in keywords:
        p = keyword.split("/")
        l = len(p)
        k = int(p[l-1])
        # from http://abstractsearch.agu.org/keywords/
        if ( (k>=300) and (k<400) ):
            counts[0] = counts[0] + 1
        if ( (k>=400) and (k<500) ):
            counts[1] = counts[1] + 1
        if ( (k>=500) and (k<600) ):
            counts[2] = counts[2] + 1
        if ( (k>=600) and (k<700) ):
            counts[3] = counts[3] + 1
        if ( (k>=700) and (k<800) ):
            counts[4] = counts[4] + 1
        if ( (k>=800) and (k<900) ):
            counts[5] = counts[5] + 1
        if ( (k>=900) and (k<1000) ):
            counts[6] = counts[6] + 1
        if ( (k>=1000) and (k<1100) ):
            counts[7] = counts[7] + 1
        if ( (k>=1100) and (k<1200) ):
            counts[8] = counts[8] + 1
        if ( (k>=1200) and (k<1300) ):
            counts[9] = counts[9] + 1
        if ( (k>=1500) and (k<1600) ):
            counts[10] = counts[10] + 1
        if ( (k>=1600) and (k<1700) ):
            counts[11] = counts[11] + 1
        if ( (k>=1700) and (k<1800) ):
            counts[12] = counts[12] + 1
        if ( (k>=1800) and (k<1900) ):
            counts[13] = counts[13] + 1
            
        if ( k == 1902 ): # Community modeling frameworks
            counts[48] = counts[48] + 1
        if ( k == 1904 ): # Community standards 
            counts[49] = counts[49] + 1
        if ( k == 1906 ): # Computational models, algorithms
            counts[50] = counts[50] + 1
        if ( k == 1908 ): # Cyberinfrastructure 
            counts[51] = counts[51] + 1
        if ( k == 1910 ): # Data assimilation, integration and fusion
            counts[52] = counts[52] + 1
        if ( k == 1912 ): # Data management, preservation, rescue 
            counts[53] = counts[53] + 1
        if ( k == 1914 ): # Data mining
            counts[54] = counts[54] + 1
        if ( k == 1916 ): # Data and information discovery
            counts[55] = counts[55] + 1
        if ( k == 1918 ): # Decision analysis
            counts[56] = counts[56] + 1
        if ( k == 1920 ): # Emerging informatics technologies 
            counts[57] = counts[57] + 1
        if ( k == 1922 ): # Forecasting
            counts[58] = counts[58] + 1
        if ( k == 1924 ): # Formal logics and grammars 
            counts[59] = counts[59] + 1
        if ( k == 1926 ): # Geospatial 
            counts[60] = counts[60] + 1
        if ( k == 1928 ): # GIS science 
            counts[61] = counts[61] + 1
        if ( k == 1930 ): # Data and information governance
            counts[62] = counts[62] + 1
        if ( k == 1932 ): # High-performance computing 
            counts[63] = counts[63] + 1
        if ( k == 1934 ): # International collaboration  
            counts[64] = counts[64] + 1
        if ( k == 1936 ): # Interoperability
            counts[65] = counts[65] + 1
        if ( k == 1938 ): # Knowledge representation and knowledge bases 
            counts[66] = counts[66] + 1
        if ( k == 1940 ): # Machine-to-machine communication 
            counts[67] = counts[67] + 1
        if ( k == 1942 ): # Machine learning 
            counts[68] = counts[68] + 1
        if ( k == 1944 ): # Markup languages   
            counts[69] = counts[69] + 1
        if ( k == 1946 ): # Metadata 
            counts[70] = counts[70] + 1
        if ( k == 1948 ): # Metadata: Provenance  
            counts[71] = counts[71] + 1
        if ( k == 1950 ): # Metadata: Quality 
            counts[72] = counts[72] + 1
        if ( k == 1952 ): # Modeling  
            counts[73] = counts[73] + 1
        if ( k == 1954 ): # Natural language processing 
            counts[74] = counts[74] + 1
        if ( k == 1956 ): # Numerical algorithms
            counts[75] = counts[75] + 1
        if ( k == 1958 ): # Ontologies  
            counts[76] = counts[76] + 1
        if ( k == 1960 ): # Portals and user interfaces
            counts[77] = counts[77] + 1
        if ( k == 1962 ): # Query languages for science, markup languages, ontologies   
            counts[78] = counts[78] + 1
        if ( k == 1964 ): # Real-time and responsive information delivery 
            counts[79] = counts[79] + 1
        if ( k == 1966 ): # Rules and logic 
            counts[80] = counts[80] + 1
        if ( k == 1968 ): # Scientific reasoning/inference  
            counts[81] = counts[81] + 1
        if ( k == 1970 ): # Semantic web and semantic integration
            counts[82] = counts[82] + 1
        if ( k == 1972 ): # Sensor web   
            counts[83] = counts[83] + 1
        if ( k == 1974 ): # Social networks
            counts[84] = counts[84] + 1
        if ( k == 1976 ): # Software tools and services 
            counts[85] = counts[85] + 1
        if ( k == 1978 ): # Software re-use  
            counts[86] = counts[86] + 1
        if ( k == 1980 ): # Spatial analysis and representation 
            counts[87] = counts[87] + 1
        if ( k == 1982 ): # Standards    
            counts[88] = counts[88] + 1
        if ( k == 1984 ): # Statistical methods: Descriptive
            counts[89] = counts[89] + 1
        if ( k == 1986 ): # Statistical methods: Inferential  
            counts[90] = counts[90] + 1
        if ( k == 1988 ): # Temporal analysis and representation 
            counts[91] = counts[91] + 1
        if ( k == 1990 ): # Uncertainty 
            counts[92] = counts[92] + 1
        if ( k == 1992 ): # Virtual globes     
            counts[93] = counts[93] + 1
        if ( k == 1994 ): # Visualization and portrayal 
            counts[94] = counts[94] + 1
        if ( k == 1996 ): # Web Services 
            counts[95] = counts[95] + 1
        if ( k == 1998 ): # Workflow
            counts[96] = counts[96] + 1
            
        if ( (k>=2100) and (k<2200) ):
            counts[15] = counts[15] + 1
        if ( (k>=2400) and (k<2500) ):
            counts[16] = counts[16] + 1
        if ( (k>=2700) and (k<2800) ):
            counts[17] = counts[17] + 1
        if ( (k>=3000) and (k<3100) ):
            counts[18] = counts[18] + 1
        if ( (k>=3200) and (k<3300) ): # 20
            counts[19] = counts[19] + 1
        if ( (k>=3300) and (k<3400) ):
            counts[20] = counts[20] + 1
        if ( (k>=3600) and (k<3700) ):
            counts[21] = counts[21] + 1
        if ( (k>=3900) and (k<4000) ):
            counts[22] = counts[22] + 1
        if ( (k>=4200) and (k<4300) ):
            counts[23] = counts[23] + 1
        if ( (k>=4300) and (k<4400) ):
            counts[24] = counts[24] + 1
        if ( (k>=4400) and (k<4500) ):
            counts[25] = counts[25] + 1
        if ( (k>=4500) and (k<4600) ):
            counts[26] = counts[26] + 1
        if ( (k>=4800) and (k<4900) ):
            counts[27] = counts[27] + 1
        if ( (k>=4900) and (k<5000) ):
            counts[28] = counts[28] + 1
        if ( (k>=5100) and (k<5200) ): # 30
            counts[29] = counts[29] + 1
        if ( (k>=5200) and (k<5300) ):
            counts[30] = counts[30] + 1
        if ( (k>=5400) and (k<5500) ):
            counts[31] = counts[31] + 1
        if ( (k>=5700) and (k<5800) ):
            counts[32] = counts[32] + 1
        if ( (k>=6000) and (k<6100) ):
            counts[33] = counts[33] + 1
        if ( (k>=6200) and (k<6300) ):
            counts[34] = counts[34] + 1
        if ( (k>=6300) and (k<6400) ):
            counts[35] = counts[35] + 1
        if ( (k>=6600) and (k<6700) ):
            counts[36] = counts[36] + 1
        if ( (k>=6900) and (k<7000) ):
            counts[37] = counts[37] + 1
        if ( (k>=7200) and (k<7300) ):
            counts[38] = counts[38] + 1
        if ( (k>=7500) and (k<7600) ): # 40
            counts[39] = counts[39] + 1
        if ( (k>=7800) and (k<7900) ):
            counts[40] = counts[40] + 1
        if ( (k>=7900) and (k<8000) ):
            counts[41] = counts[41] + 1
        if ( (k>=8000) and (k<8100) ):
            counts[42] = counts[42] + 1
        if ( (k>=8100) and (k<8200) ):
            counts[43] = counts[43] + 1
        if ( (k>=8400) and (k<8500) ):
            counts[44] = counts[44] + 1
        if ( (k>=9300) and (k<9400) ):
            counts[45] = counts[45] + 1
        if ( (k>=9600) and (k<9700) ):
            counts[46] = counts[46] + 1
        if ( (k>=9800) and (k<9900) ): # 48
            counts[47] = counts[47] + 1
            
    max_value = max(counts)
    group = counts.index(max_value)    
    return group
    
def getAbstractsForEmail( files, email ):

    abstracts = []
    for f in files:

        inFile = open(f, "r")
        for line in inFile:

            parts = line.split(",")
            year = parts[0].strip()
            abstract = parts[1].strip()
            e1 = parts[2].strip()
            e2 = parts[3].strip()

            if ( (e1 == email) or (e2 == email) ):
                abstracts.append(abstract)

    return abstracts
    

def getFullName( dr, year, email ):

    result = ""
    y = int(year)
    
    while ( y >= 2010 ):

            attendence1 = dr + str(y) + "_Summer.csv"
            attendence2 = dr + str(y) + "_Winter.csv"

            f = open(attendence1, "r")
            for line in f:
                parts = line.split(",")
                fullName = parts[0].strip()
                emailAddress = parts[1].strip()
                if ( email.lower() == emailAddress.lower() ):
                    result = fullName
                    break
            f.close()
            
            if ( result == "" ):
                f = open(attendence2, "r")
                for line in f:
                    parts = line.split(",")
                    fullName = parts[0].strip()
                    emailAddress = parts[1].strip()
                if ( email.lower() == emailAddress.lower() ):
                    result = fullName
                    break
                f.close()

            y = y - 1
            if ( result != "" ):
                break

    return result

# create a dictionary of abstracts
abstracts = []
currentAbstracts = []

# create a dictionary of author-topic (color)
topics = {}

# create a dictionary of author-coauthors (comma seperated)
coauthors = {}
uniquePeople = []
trulyUniquePeople = []
personEmail = {}

# read the co-author files
dr = "/Users/narock/University/Projects/agu_analytics/esip_summer_2017/MeetingAttendeeData/csv/"
file1 = dr + "results/results_summer/coauthorResults.csv"
file2 = dr + "results/results_winter/coauthorResults.csv"
files = [file1, file2]
keyFile1 = dr + "results/results_summer/keywordResults.csv"
keyFile2 = dr + "results/results_winter/keywordResults.csv"
keyFiles = [keyFile1, keyFile2]

for f in files:

    inFile = open(f, "r")
    for line in inFile:

        parts = line.split(",")
        year = parts[0].strip()
        abstract = parts[1].strip()
        email = parts[2].strip()
        coauthorEmail = parts[3].strip()

        if ( year == "2011" ):

            # have we seen this abstract before, if so then we don't need to do this again
            if ( abstract not in abstracts ):

                # use the year to map from email address to name
                ##
                ## FROM THE CURRENT YEAR BACK
                ##
                person = getFullName( dr, year, email )
                coauthor = getFullName( dr, year, coauthorEmail )

                # update the list of unique people
                if ( (email not in uniquePeople) and (email != "") ):
                    uniquePeople.append(email)
                    personEmail[email] = person

                # fill in the author-coauthor dictionary
                # if coauthor equals "" then the coauthor didn't attend AGU
                # second check avoids self-reference in network map
                if ( coauthor != "" and (coauthorEmail != email.lower()) ): 
                    #if ( person in coauthors ):
                    if ( email in coauthors ):
                        #names = coauthors[person]
                        names = coauthors[email]
                        #names = names + "," + coauthor
                        names = names + "," + coauthorEmail
                        #coauthors[person] = names
                        coauthors[email] = names
                    else:
                        #coauthors[person] = coauthor
                        coauthors[email] = coauthorEmail
                    uniquePeople.append(coauthorEmail)
                    personEmail[coauthorEmail] = coauthor

            if ( abstract not in currentAbstracts ):
                currentAbstracts.append( abstract )

    inFile.close()            
    abstracts.extend( currentAbstracts )
    currentAbstracts = []

# JSON output
out = dr+"results/network_map.json"
outFile = open(out, "w")

json = "{\n" + "\"nodes\": [\n"
outFile.write(json)

# iterate over all the unique people
for p in uniquePeople:

    # deterime a topic color for this person
    #
    # find all the abstracts for this email address
    person = personEmail[p]
    ab = getAbstractsForEmail( files, p )
    # go to the keywords file and get all the keywords, the most often used one is our topic
    color = keywordCount( keyFiles, ab )

    # since we lack unique IDs like ORCID, we end up with the same name assigned to
    # multiple email addresses. e.g. Tom Narock to tnarock@marymount.edu and Thomas.W.Narock@nasa.gov
    # We want to keep the "links" for all these people, but don't list them in the "id"
    # more than once
    if ( p not in trulyUniquePeople ):
        outFile.write("     {\"id\": \"" + p + "\", \"group\": " + str(color) + "},\n")
        trulyUniquePeople.append(p)
        
outFile.write("],\n" + "\"links\": [\n")

# output people connection JSON
for key, value in coauthors.iteritems():
    counts = coAuthorCounts( value )
    for k, v in counts.iteritems():
        outFile.write("{\"source\": \"" + key + "\", \"target\": \"" + k + "\", \"value\":" + str(v) + "},\n")
        
outFile.write("]\n}")
outFile.close()


