# Creates graphs from the data and extract information about them

import igraph as ig 
from fonctionsutiles import edge_df
import matplotlib.pyplot as plt

print(edge_df)

network = ig.Graph.DataFrame(edges = edge_df, directed = True)

indegree_list = []
outdegree_list = []
for vertex in network.vs:
    indegree_list.append(vertex.indegree())
    outdegree_list.append(vertex.outdegree())
    dico = vertex.attributes()
    if outdegree_list[-1] == 199:
        print(len(vertex.all_edges()))
        print(vertex.indegree())
        print(vertex.outdegree())
        print(dico['name'])

        
        
    


indegree_list.sort()
print(indegree_list[-1])
outdegree_list.sort()
print(outdegree_list[-1])
