def createPeopleKeywordQuery(year, offset):

	query1 = """
    	PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
		PREFIX agu: <http://abstractsearch.agu.org/ontology#>
		PREFIX swc: <http://data.semanticweb.org/ns/swc/ontology#>
		PREFIX swrc: <http://swrc.ontoware.org/ontology#>

		SELECT ?keyword ?name ?mbox """
    
	query2 = "FROM <http://abstractsearch.agu.org/graphs/2.0/" + year + "/FM>"

	query3 = """ WHERE {

		?abstract a agu:Abstract . 
  		?abstract swc:hasTopic ?keyword .
  		?abstract <http://tw.rpi.edu/schema/hasAgentWithRole> ?author .
  		?person <http://tw.rpi.edu/schema/hasRole> ?author .
  		?person <http://xmlns.com/foaf/0.1/name> ?name .
  		?person <http://xmlns.com/foaf/0.1/mbox> ?mbox .

 	} """

	query = query1 + query2 + query3 + " LIMIT 10000 OFFSET " + offset
	return query