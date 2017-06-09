def createAbstractUriQuery(year, email):

        query1 = """
        prefix p1: <http://abstractsearch.agu.org/ontology#> 
        prefix p2: <http://data.semanticweb.org/ns/swc/ontology#> 
        prefix p3: <http://tw.rpi.edu/schema/> 
        prefix p4: <http://xmlns.com/foaf/0.1/> 

        SELECT DISTINCT ?abstract ?section WHERE { 

          ?abstract a p1:Abstract .  
          ?abstract p2:hasTopic ?keyword . """

        query2 = "?session p2:isSubEventOf <http://abstractsearch.agu.org/meetings/" + year + "/FM> . "
          
        query3 = """
          ?abstract p2:relatedToEvent ?session .
          ?session p1:section ?section .
          ?abstract p3:hasAgentWithRole ?author . 
          ?person p3:hasRole ?author . 
          ?person p4:name ?name . 
          ?person p4:mbox """

        query3 = query3 + "\"" + email + "\"^^<http://www.w3.org/2001/XMLSchema#string> . }" 

        query = query1 + query2 + query3
        return query

def createKeywordsQuery(year, abstract):

        query1 = """
        prefix p1: <http://abstractsearch.agu.org/ontology#> 
        prefix p2: <http://data.semanticweb.org/ns/swc/ontology#> 
        prefix p3: <http://tw.rpi.edu/schema/> 
        prefix p4: <http://xmlns.com/foaf/0.1/> 

        SELECT DISTINCT ?keyword WHERE { """

        query2 = "<" + abstract + "> p2:hasTopic ?keyword . "

        query3 = "?session p2:isSubEventOf <http://abstractsearch.agu.org/meetings/" + year + "/FM> . "
          
        query4 = "<" + abstract + "> p2:relatedToEvent ?session . }"

        query = query1 + query2 + query3 + query4
        return query

def createCoAuthorQuery(year, abstract):

        query1 = """
        prefix p1: <http://abstractsearch.agu.org/ontology#> 
        prefix p2: <http://data.semanticweb.org/ns/swc/ontology#> 
        prefix p3: <http://tw.rpi.edu/schema/> 
        prefix p4: <http://xmlns.com/foaf/0.1/> 

        SELECT DISTINCT ?email WHERE { """

        query2 = "<" + abstract + "> p3:hasAgentWithRole ?author . "

        query3 = """
          ?person p3:hasRole ?author . 
          ?person p4:mbox ?email . } """

        query = query1 + query2 + query3
        return query
