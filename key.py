

import math, sys
from SPARQLWrapper import SPARQLWrapper, JSON
from queries.keywordSectionCount import keywordSectionCount
from queries.createKeywordSectionQuery import createKeywordSectionQuery

# get the year to query from the user
year = input("Enter year to query: ")
year = str(year)

## when making name file, change to + "names.csv"

filename = year + "keyword.csv"

# there are too many results to get all at once
# here we ask the database how many results there 
# are for the year we are interested in. Given that
# we can get 10,000 results per query, we do a little
# math to compute how many times we need to query the database 
# to get all the results
offset = 0
limit = float(keywordSectionCount(year))
numQueries = math.ceil(limit/10000)

# setting up the query 
# specifying the web address of the database
# setting the return format to JSON - JavaScript Object Notation
sparql = SPARQLWrapper("http://abstractsearch.agu.org:8890/sparql")
sparql.setReturnFormat(JSON)

# keep looping and querying until we get all the results

import csv
with open(filename, 'wb') as csvfile:
    resultwriter = csv.writer(csvfile, delimiter= ',' ,
                              quoting=csv.QUOTE_MINIMAL)

#keyword = []
#name = []

    while (numQueries > 0):
            query = createKeywordSectionQuery(year,str(offset))
            sparql.setQuery(query)
            offset = offset + 10000

            results = sparql.query().convert()

            # Save all keywords into array
            ## pass array into import csv program
            ## we can loop program and write rows one at a time          

            
            for result in results["results"]["bindings"]:
                    keywordURL = result["keyword"]["value"]
                # If there is no keyword, don't run, go to next value
                    if keywordURL != "None":
                            keyCode = keywordURL.split("keywords/")
                            sectionURL = result["section"]["value"]
                            sectionCode = sectionURL.split("sections/")    
                            
                            resultwriter.writerow([keyCode[1], sectionCode[1]])  
            numQueries = numQueries - 1


    # set delimeter to comma - separates into different columns
    
            
