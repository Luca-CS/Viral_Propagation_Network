# Creates graphs from the data and extract information about them

import igraph as ig 
from fonctionsutiles import edge_df
import matplotlib.pyplot as plt
edge_df.reset_index(drop=True)

name_dic = {}
num = 0
for index,row in edge_df.iterrows():
    id = row['id']
    follow = row['follow']
    if not id in name_dic:
        name_dic[id] = num
        num += 1
    if not follow in name_dic:
        name_dic[follow] = num
        num += 1

print(len(name_dic))



vertex_num = len(name_dic)
adja = []

for i in range(vertex_num):
    line = [0 for i in range(vertex_num)]
    adja.append(line)

for index,row in edge_df.iterrows():
    id = name_dic[row['id']]
    follow = name_dic[row['follow']]
    adja[id][follow] = 1

network = ig.Graph.Adjacency(adja) 

print(network.vcount())
print(network.ecount())




"""network = ig.Graph.DataFrame(edges = edge_df, directed = True)

indegree_list = []
outdegree_list = []
for vertex in network.vs:
    indegree_list.append(vertex.indegree())
    outdegree_list.append(vertex.outdegree())
    dico = vertex.attributes()
"""
