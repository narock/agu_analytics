def main():

    d_dis = "/Users/narock/Desktop/AGU_Graph/"

    sections = ["A", "AE", "B", "C", "DI", "ED", "EP", "G", "GC", "GP", "H", "IN", "MR",
                "NG", "NH", "NS", "OS", "P", "PA", "PP", "S", "SA", "SH", "SM", "T", "U", "V"]

    md = {}
    seen = []
    
    for section in sections:

        for sec in sections:

            # We only want the comparison to be one way
            # e.g. if we've already compared A-AE then we don't want to compare AE-A
            label = section + "-" + sec
            reverseLabel = sec + "-" + section
            
            if ( sec != section and label not in seen and reverseLabel not in seen ):

                multi = 0
                matches = []
                seen.append(label)
                print("Comparing:",section,sec)
                
                try:
                    with open(d_dis + section + "/nodesFile_" + section + "_2017", "r", encoding="utf8") as nodeFile1:
                    
                        for line1 in nodeFile1:
                            parts = line1.strip().split(":")
                            email1 = parts[0].lower().strip()

                            nodeFile2 = open(d_dis + sec + "/nodesFile_" + sec + "_2017", "r", encoding="utf8")
                            for line2 in nodeFile2:
                                parts = line2.strip().split(":")
                                email2 = parts[0].lower().strip()
                                if (email1 == email2 and (email1 not in matches)): multi += 1
                            nodeFile2.close()

                        nodeFile1.close()

                        if (multi > 0): md[label] = multi
 
                except IOError as e:
                    print("IOError: ", d_dis + section + "/nodesFile_" + section + "_2017")

    for key, value in md.items(): print(key,value)
     
main()
