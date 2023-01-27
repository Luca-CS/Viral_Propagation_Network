# Creates graphs from the data and extract information about them

# Import des fonctions utiles

import igraph as ig 
from fonctionsutiles import edge_df
import matplotlib.pyplot as plt

# Cree un dictionnaire qui associe les id_user (à 6 chiffres) à des identifiants uniques allant de 0 -> 3500

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


# Genère la matrice d'adjacence du graphe des follow


vertex_num = len(name_dic)
adja = []

for i in range(vertex_num):
    line = [0 for i in range(vertex_num)]
    adja.append(line)

for index,row in edge_df.iterrows():
    id = name_dic[row['id']]
    follow = name_dic[row['follow']]
    adja[id][follow] = 1
    
# Genere le graphe à partir de la matrice

network = ig.Graph.Adjacency(adja) 

