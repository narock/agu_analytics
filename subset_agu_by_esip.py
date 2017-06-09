from agu_queries import *
from SPARQLWrapper import SPARQLWrapper, JSON
 
dir = "/Users/narock/University/Projects/agu_analytics/esip_summer_2017/"
dir = dir + "MeetingAttendeeData/csv/"
files = ["2010_Winter.csv", "2011_Winter.csv", "2012_Winter.csv",
         "2013_Winter.csv", "2014_Winter.csv", "2015_Winter.csv","2016_Winter.csv"]
#files = ["2010_Summer.csv", "2011_Summer.csv", "2012_Summer.csv",
#         "2013_Summer.csv", "2014_Summer.csv", "2015_Summer.csv","2016_Summer.csv"]

# output files we will use
sectionOutput = dir + "sectionResults.csv"
keywordOutput = dir + "keywordResults.csv"
coauthorOutput = dir + "coauthorResults.csv"

# open the output files
sOut = open(sectionOutput, "a")
kOut = open(keywordOutput, "a")
cOut = open(coauthorOutput, "a")

# establish the SPARQL connection to AGU
sparql = SPARQLWrapper("http://abstractsearch.agu.org:8890/sparql")
sparql.setReturnFormat(JSON)

# loop over all the ESIP attendance files
for f in files:

    # get the year from the filename
    year = f[0:4]

    # open the current file for reading
    inFile = open(dir+f, "r")
    print("Working on " + f + " ...")

    # reset attendance numbers and list of abstracst we've seen
    attendees = 0
    aguAttendees = 0
    abstractUris = []

    # loop over all the lines in the file
    for line in inFile:

        # get the name and email address
        parts = line.split(",")
        name = parts[0].strip()
        email = parts[1].strip()
        attendees = attendees + 1
        
        # check for abstract URIs based on email address
        abstractQuery = createAbstractUriQuery(year, email)
        sparql.setQuery(abstractQuery)
        results = sparql.query().convert()
        notUpdatedAgu = True
        for result in results["results"]["bindings"]:
            abstract = result["abstract"]["value"]
            section = result["section"]["value"]
            if ( notUpdatedAgu ):
                aguAttendees = aguAttendees + 1
                notUpdatedAgu = False
            # abstracts can have more than one author
            # we may have seen this abstract before when querying for another person
            # if so, then we can ignore it now, don't need to output multiple times
            if ( abstract.strip() not in abstractUris ):
                sOut.write(year + "," + abstract.strip() + "," + section.strip() + "\n")
            
            # if found, get set of keywords for this person
            #
            # same as above, we don't want to output the abstract multiple times
            if ( abstract.strip() not in abstractUris ):
                keyQuery = createKeywordsQuery(year, abstract)
                sparql.setQuery(keyQuery)
                results = sparql.query().convert()
                for result in results["results"]["bindings"]:
                    keyword = result["keyword"]["value"]
                    kOut.write(year + "," + abstract.strip() + "," + keyword.strip() + "\n")
            
            # if found, then get list of co-authors
            #
            # same as above, we don't want to output the abstract multiple times
            if ( abstract.strip() not in abstractUris ):
                coauthorQuery = createCoAuthorQuery(year, abstract)
                sparql.setQuery(coauthorQuery)
                results = sparql.query().convert()
                emailList = []
                # the AGU data has some quality control issues, we try to account for that here
                # for instance, in one case we get "stevea@ssec.wisc.edu" and "SteveA@ssec.wisc.edu"
                # as two authors on the same presentation, which is clearly the same person
                # here, we try to account for this
                for result in results["results"]["bindings"]:
                    coemail = result["email"]["value"]
                    coemail = coemail.strip()
                    coemail = coemail.lower()
                    if ( coemail not in emailList ):
                        emailList.append( coemail )
                for em in emailList:
                    # avoid self-reference
                    test = email.lower()
                    test = email.strip()
                    if ( test != em ):
                        cOut.write(year + "," + abstract.strip() + "," + email.strip() + "," + em + "\n")

            # add the abstract to our list so we know we've already seen it
            abstractUris.append(abstract.strip())

    print("Attendees (" + year + ")", attendees)
    print("Found at AGU: (" + year + ")", aguAttendees)

# close the output files
sOut.close()
kOut.close()
cOut.close()
