from AguAuthor import AguAuthor

def exactMatchFor(email, authors):

    found = False
    primaryEmail = ""
    for key, emails in authors.items():
        if email in emails:
            found = True
            primaryEmail = key
            break

    return found, primaryEmail

def main():

    inDir = "/Users/narock/Desktop/AGU_Graph/"
    outDir = "/Users/narock/Desktop/AGU_Graph/disambiguated/"
    
    sections = ["A", "AE", "B", "C", "DI", "ED", "EP", "G", "GC", "GP", "H", "IN","MR",
                "NG","NH", "NS","OS", "P", "PA", "PP", "S", "SA", "SH","SM","T","U","V"]
     
    years = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", 
             "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"]

    for section in sections:

        # Status update
        print("Working on", section)
        
        # Read the exact matches file
        authors = {}
        matchFile = open(inDir + section + "/exactMatches_" + section, "r", encoding="utf8")
        for line in matchFile:
            emails = []
            parts = line.strip().split(",")
            lastName = parts[0].strip()
            initials = parts[1].strip()
            primaryEmail = parts[2].strip()
            secondaryEmail = []
            for i in range(3, len(parts)): secondaryEmail.append( parts[i].strip() )
            authors[primaryEmail] = secondaryEmail
        matchFile.close()

        for year in years:

            edges = []
            nodes = []

            print("   year:", year)

            # Read all the edges and nodes for this year
            # If there's an edge file then there's a node file so we only need to check once
            try:
                with open(inDir + section + "/edgesFile_" + section + "_" + year, "r", encoding="utf8") as edgeFile:
    
                    for edge in edgeFile:
                        parts = edge.split(":")
                        n1 = parts[0].strip()
                        n2 = parts[1].strip()
                        found, primaryEmail = exactMatchFor(n1, authors)
                        if found: n1 = primaryEmail
                        found, primaryEmail = exactMatchFor(n2, authors)
                        if found: n2 = primaryEmail
                        e = n1 + ":" + n2
                        if (e not in edges): edges.append(e)
                    edgeFile.close()
                
                    nodeFile = open(inDir + section + "/nodesFile_" + section + "_" + year, "r", encoding="utf8")
                    for node in nodeFile:
                        parts = node.split(":")
                        e = parts[0].strip() # email
                        n = parts[1].strip() # name
                        found, primaryEmail = exactMatchFor(e, authors)
                        if found: e = primaryEmail
                        no = e + ":" + n
                        if (no not in nodes): nodes.append(no)
                    nodeFile.close()

                    # Write the cleaned up data
                    outEdgeFile = open(outDir + section + "/edgesFile_" + section + "_" + year, "w", encoding="utf8")
                    for edge in edges: outEdgeFile.write(edge + "\n")
                    outNodeFile = open(outDir + section + "/nodesFile_" + section + "_" + year, "w", encoding="utf8")
                    for node in nodes: outNodeFile.write(node + "\n")
                    outEdgeFile.close()
                    outNodeFile.close()

            except IOError as e:
                pass # don't need to do anything, just skip this year since it doesn't exist
                                    
main()
