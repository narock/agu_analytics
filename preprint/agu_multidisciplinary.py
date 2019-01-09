def main():

    d_dis = "/data/directory/disambiguated/"

    #d_dis = "/Users/narock/Desktop/AGU_Graph/"

    sections = ["A", "AE", "B", "C", "DI", "ED", "EP", "G", "GC", "GP", "H", "IN", "MR",
                "NG", "NH", "NS", "OS", "P", "PA", "PP", "S", "SA", "SH", "SM", "T", "U", "V"]

    md = {}
    seen = []
    
    for section in sections:

        results = []

        for sec in sections:

            # We only want the comparison to be one way
            # e.g. if we've already compared A-AE then we don't want to compare AE-A
            label = section + "-" + sec
            reverseLabel = sec + "-" + section
            
            if ( sec != section and label not in seen and reverseLabel not in seen ):

                seen.append(label)
                #print("Comparing:",section,sec)
                
                file1 = []
                file2 = []

                nodeFile1 = open(d_dis + section + "/nodesFile_" + section + "_2017", "r", encoding="utf8")
                    
                for line1 in nodeFile1:
                    parts = line1.strip().split(":")
                    email1 = parts[0].lower().strip()
                    file1.append(email1)
                
                nodeFile1.close()

                nodeFile2 = open(d_dis + sec + "/nodesFile_" + sec + "_2017", "r", encoding="utf8")
                            
                for line2 in nodeFile2:
                    parts = line2.strip().split(":")
                    email2 = parts[0].lower().strip()
                    file2.append(email2)
                
                nodeFile2.close()

                matches = set(file1) & set(file2)
                n_matches = len(matches)
                if ( n_matches > 0 ):
                    size = len(list(set(file1+file2)))
                    results.append( round(n_matches/size,2) )

        print( results )
     
main()
