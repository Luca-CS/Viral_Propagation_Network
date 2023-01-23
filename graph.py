# Creates graphs from the data and extract information about them

import igraph as ig 
from fonctionsutiles import edge_df
import matplotlib.pyplot as plt

print(edge_df)

network = ig.Graph.DataFrame(edge_df, directed = True)

indegree_list = []
outdegree_list = []
for vertex in network.vs:
    indegree_list.append(vertex.indegree())
    outdegree_list.append(vertex.outdegree())


indegree_list.sort()
print(indegree_list[-1])
outdegree_list.sort()
print(outdegree_list[-1])
