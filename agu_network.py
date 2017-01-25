def print_centrality(results, n):

	# results is node:centrality list
	# reverse the list to be centrality, node
	items = [ (b,a) for (a,b) in results.iteritems()]

	# use python sorter
	items.sort()

	# sorter sorts lowest to highest, reverse so we have highest to lowest
	items.reverse()

	# print the top n
	for i in range(n):
		print(items[i])

import sys, csv
import networkx as nx

# top n to print 
n_to_print = 5

# command line inputs
nodeFile=sys.argv[1]
edgeFile=sys.argv[2]

# create an empty (undirected) Graph
G = nx.Graph()

# read and create the nodes
with open(nodeFile, 'rU') as csvfile:
    r = csv.reader(csvfile)
    for fields in r:
        n=fields[0]
        G.add_node(n) 

# read and create the edges
with open(edgeFile, 'rU') as csvfile:
    r = csv.reader(csvfile)
    for fields in r:
        e1=fields[0]
        e2=fields[1]
        G.add_edge(e1,e2)

# degree centrality
print("Computing degree centrality...")
degree = nx.degree_centrality(G)
print_centrality(degree,n_to_print)
print()

# eigenvalue centrality
print("Computing eigenvalue centrality...")
eigenvalue = nx.eigenvector_centrality_numpy(G)
print_centrality(eigenvalue,n_to_print)
print()

# pagerank centrality
print("Computing pagerank centrality...")
pagerank = nx.pagerank(G)
print_centrality(pagerank,n_to_print)
print()

# closeness centrality
print("Computing closeness centrality...")
closeness = nx.closeness_centrality(G)
print_centrality(closeness,n_to_print)
print()

# betweenness centrality
print("Computing betweenness centrality...")
betweenness = nx.betweenness_centrality(G)
print_centrality(betweenness,n_to_print)
print()

# community determination - Louvain method