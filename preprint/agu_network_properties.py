import networkx as nx

def ccs(graph):
    
    gg = list(nx.connected_component_subgraphs(graph))
    numCCS = len(gg)
    smallest = 9999
    largest = 0
    numSingleNode = 0
    for z in gg:
        if (nx.number_of_nodes(z) < smallest): smallest = nx.number_of_nodes(z)
        if (nx.number_of_nodes(z) > largest): largest = nx.number_of_nodes(z)
        if (nx.number_of_nodes(z) == 1): numSingleNode += 1

    return numCCS, smallest, largest, numSingleNode 

              
def main():

    d_raw = "/data/directory/"
    d_dis = "/data/directory/disambiguated/"

    sections = ["A", "AE", "B", "C", "DI", "ED", "EP", "G", "GC", "GP", "H", "IN","MR",
                "NG","NH", "NS","OS", "P", "PA", "PP", "S", "SA", "SH","SM","T","U","V"]
    
    years = ["2017"] 
    #years = ["2000", "2001", "2002", "2003", "2004", "2005", "2006", "2007", "2008", 
    #         "2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017"]
    
    for section in sections:
        
        for year in years:

            G_raw = nx.Graph()
            G_dis = nx.Graph()

            try:
                # if the node file exists then the others should too, only need one try statement
                with open(d_raw + section + "/nodesFile_" + section + "_" + year, "r", encoding="utf8") as nodeFile1:
                    
                    nodeFile2 = open(d_dis + section + "/nodesFile_" + section + "_" + year, "r", encoding="utf8")
                    for line in nodeFile1:
                        parts = line.strip().split(":")
                        email = parts[0].strip()
                        G_raw.add_node( email )
                    for line in nodeFile2:
                        parts = line.strip().split(":")
                        email = parts[0].strip()
                        G_dis.add_node( email )

                    edgeFile1 = open(d_raw + section + "/edgesFile_" + section + "_" + year, "r", encoding="utf8")
                    edgeFile2 = open(d_dis + section + "/edgesFile_" + section + "_" + year, "r", encoding="utf8")
                    for line in edgeFile1:
                        parts = line.strip().split(":")
                        G_raw.add_edge( parts[0].strip(), parts[1].strip() )
                    for line in edgeFile2:
                        parts = line.strip().split(":")
                        G_dis.add_edge( parts[0].strip(), parts[1].strip() )
            
                    # Connected component subgraph
                    numCCS_raw, smallest_raw, largest_raw, numSingleNode_raw = ccs(G_raw)
                    numCCS_dis, smallest_dis, largest_dis, numSingleNode_dis = ccs(G_dis)

                    #print(nx.density(G_raw))
                    #print(nx.density(G_dis))
                    print(section, nx.number_of_nodes(G_dis), numCCS_dis, round((largest_dis/nx.number_of_nodes(G_dis))*100.,1), round((numSingleNode_dis/nx.number_of_nodes(G_dis))*100.,1))
                    #print(nx.average_clustering(G_dis, count_zeros=True))

                    nodeFile1.close()
                    edgeFile1.close()
                    nodeFile2.close()
                    edgeFile2.close()

            except IOError as e:
                print("NaN")
            
main()
