import igraph as ig 
from fonctionsutiles import * 
import matplotlib.pyplot as plt
import random

account=account_df
posts=post_df


def dico_tot(p):
    dico={}
    for index, row in account.iterrows(): 
        #initialisation du dico avec les caractéristiques basiques
        birth_year=int(row.birth_date[-2:])
        if (birth_year>17):
            birth_year=1900+birth_year
        else:
            birth_year+=2000
        dico[row.id_user]={'gender': row.sex, 
                                   'age' : 2017-birth_year, 
                                   'followers' :  row.nb_followers,
                                   'followings': row.nb_following,
                                   'posts': row.nb_posts,
                                   'original': False,
                                   'repost': 0,
                                   'total_views': 0,
                                   'views_bf_post': 0,
                                   'id_followers': row.id_followers
            
        }
        
        
    for index, row in posts.iterrows():
        
        if row.id_post_origin==0:
            dico[row.id_user]['original']=True
        dico[row.id_user]['repost']+=1
        followers=list(dico[row.id_user]['id_followers'][1:-1].split(", "))
        n=round(len(followers)*p*0.01) #Nombre de personnes qui ont vu le post
        followers_saw_post=random.sample(followers,n)
        for id in followers_saw_post:
            dico[int(id)]['total_views']+=1
            if dico[int(id)]['repost']==0 :
                dico[int(id)]['views_bf_post']+=1
    return dico
    
    
    
    


def test(p):
    dico=dico_tot(p)
    rep=0
    for row in dico:
        rep+=dico[row]['repost']
    return rep
