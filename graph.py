# Creates graphs from the data and extract information about them

import igraph as ig 
from data_analysis import * 
import matplotlib.pyplot as plt

# edge_df = 
network = ig.Graph.DataFrame



def communitie_gen(g):
    communities = g.community_edge_betweenness()
    communities = communities.as_clustering()
    num_communities = len(communities)
    palette = ig.RainbowPalette(n=num_communities)
    for i, community in enumerate(communities):
        g.vs[community]["color"] = i
        community_edges = g.es.select(_within=community)
        community_edges["color"] = i
    
    return communities


def community_display(communities):
    num_communities = len(communities)
    palette = ig.RainbowPalette(n=num_communities)
    fig, ax = plt.subplots()
    ig.plot(communities,palette=palette,edge_width=1,target=ax,vertex_size=0.3,)

    legend_handles = []
    for i in range(num_communities):
        handle = ax.scatter([], [],s=100,facecolor=palette.get(i),edgecolor="k",label=i)
        legend_handles.append(handle)
        
    ax.legend(handles=legend_handles,title='Community:',bbox_to_anchor=(0, 1.0),bbox_transform=ax.transAxes,)
    
    plt.show()
