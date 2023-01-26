import igraph as ig
from fonctionsutiles import *
import matplotlib.pyplot as plt
import random

account = cleaned_account
posts = post_df
# print(posts)
#print(time(posts.loc[1]))
# print(posts.loc[1147])

# def arbre():
#     tree={}
#     emplacement
#     for index, row in posts:
#         if row['id_post_origin']==0:
#             tree{row['id_post']}={'donnees': row, 'fils': {}}
#         else:
#             for origin in range(tree):
#                 if origin==row['id_post_origin']:
#                     tree[origin]['fils'][row['id_post']]={'donnees': row, 'fils': {}}
#                 else:
#                     for 
# tree={}                   
# def arbre_rec(row):
#     if row['id_post_origin']==0:
#             tree{row['id_post']}={'donnees': row, 'fils': {}}
#         else:
#             for origin in range(tree):
#                 if origin==row['id_post_origin']:
#                     tree[origin]['fils'][row['id_post']]={'donnees': row, 'fils': {}}
#                 else:
#                     for 
     

# def true_repostheure(n):
#     structure={'id_post':[],'id_user':[],'reposts':[], 'likes':[], 'views':[], 'time':[]}
#     pas=int(11520/n)
#     count=0
#     for index,row in posts.iterrows():
#         count+=1
#         t=time(row)
#         structure['id_post'].append(row['id_post'])
#         structure['id_user'].append(row['id_user'])
#         structure['reposts'].append(row['reposts'])
#         structure['likes'].append(row['likes'])
#         structure['views'].append(row['views'])
#         structure['time'].append(t//pas)
#     df = pd.DataFrame(data=structure)
#     print(count)
#     return df

# def hyp_repostheure(n):
#     structure={'id_post':[],'id_user':[],'reposts':[], 'likes':[], 'views':[], 'time':[]}
#     pas=int(11520/n)
#     count=0
#     for index,row in posts.iterrows():
#         count+=1
#         t=time(row)
#         dt=True
#         rep=0
#         ind=index+1
#         while dt and ind<(len(posts)-1):
#             if ind!=1146 and ind!=2796:
#                 t2=time(posts.loc[ind])
#                 #print(t2)
#                 if t2-t<=60*5:
#                     #print(t,t2)
#                     if posts.loc[ind]['id_post_origin']==row['id_post']:
#                         rep+=1
#                         #print(rep)
#                     ind+=1
#                 else:
#                     dt=False
#             else: ind+=1
#         structure['id_post'].append(row['id_post'])
#         structure['id_user'].append(row['id_user'])
#         structure['reposts'].append(rep)
#         structure['likes'].append(row['likes'])
#         structure['views'].append(row['views'])
#         structure['time'].append(t//pas)
#     df = pd.DataFrame(data=structure)
#     print(count)
#     return df

# # df=hyp_repostheure(32)
# # plt.scatter(df['time'], df['reposts'], color = 'g')
# # plt.xlabel('time')
# # plt.ylabel('reposts')
# # plt.show()   


# def moy_repostheure(n):
#     structure={'id_post':[],'id_user':[],'reposts':[], 'likes':[], 'views':[], 'time':[]}
#     moyennes={'moy': [0 for k in range(n)] ,'nombre':[0 for k in range(n)]}
#     pas=int(11520/n)
#     count=0
#     for index,row in posts.iterrows():
#         t=time(row)
#         dt=True
#         rep=0
#         ind=index+1
#         while dt and ind<(len(posts)):
#             if ind!=1146 and ind!=2796:
#                 t2=time(posts.loc[ind])
#                 #print(t2)
#                 if t2-t<=60*6:
#                     #print(t,t2)
#                     if posts.loc[ind]['id_post_origin']==row['id_post']:
#                         rep+=1
#                         #print(rep)
#                     ind+=1
#                 else:
#                     dt=False
#             else: ind+=1
#         moyennes['moy'][t//pas]+=rep
#         moyennes['nombre'][t//pas]+=1
#     for k in range(n):
#         if moyennes['nombre'][k]!=0:
#             moyennes['moy'][k]/=moyennes['nombre'][k]
#         else:
#             moyennes['moy'][k]=-1
#     return moyennes

# plt.plot([k for k in range(32)],moy_repostheure(32)['moy'])
# plt.show()

def moy_sansjour_repostheure(n):
    
    """fonction qui sur l'ensemble des posts renvoie, pour chaque tranche de la journée (ici une journée est divisée en n tranches)
    une moyenne, sur le nombre de posts de la tranche, du nombre de reposts dans les 4 heures qui suivent le post original.

    """
    moyennes={'moy': [0 for k in range(n)] ,'nombre':[0 for k in range(n)]}
    pas=int(1440/n)
    
    for index,row in posts.iterrows():
        t=time(row)
        dt=True
        rep=0
        ind=index+1
        while dt and ind<(len(posts)): #itération sur les posts qui suivent dans les 4 heures suivantes
            if ind!=1146 and ind!=2796:
                t2=time(posts.loc[ind])
                
                if t2-t<=60*4:
                    
                    if posts.loc[ind]['id_post_origin']==row['id_post']:
                        rep+=1
                        
                    ind+=1
                else:
                    dt=False
            else: ind+=1
        moyennes['moy'][(t%1440)//pas]+=rep
        moyennes['nombre'][(t%1440)//pas]+=1
    for k in range(n):
        if moyennes['nombre'][k]!=0:
            moyennes['moy'][k]/=moyennes['nombre'][k]
        else:
            moyennes['moy'][k]=-1
    return moyennes

plt.plot([2*k for k in range(12)],moy_sansjour_repostheure(12)['moy'])
plt.title('Nombre de reposts, dans les 4 heures qui succèdent au post, en fonction du temps')
plt.xlabel('temps')
plt.ylabel('reposts en moyenne')
plt.show()
