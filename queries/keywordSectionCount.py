from SPARQLWrapper import SPARQLWrapper, JSON

def keywordSectionCount(year):

    queryPart1 = """PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX agu: <http://abstractsearch.agu.org/ontology#>
        PREFIX swc: <http://data.semanticweb.org/ns/swc/ontology#>
        PREFIX swrc: <http://swrc.ontoware.org/ontology#>

        SELECT (count(?keyword) as ?count)
        FROM <http://abstractsearch.agu.org/graphs/2.0/""" 

    queryPart2 = """/FM>
        WHERE {

          ?abstract a agu:Abstract . 
          ?abstract swc:hasTopic ?keyword .
          ?abstract swc:relatedToEvent ?event .
          ?event agu:section ?section .

        }

    """
    sparql = SPARQLWrapper("http://abstractsearch.agu.org:8890/sparql")
    sparql.setQuery(queryPart1 + year + queryPart2)
        
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        count = result["count"]["value"]
    return count