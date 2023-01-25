import igraph as ig
from fonctionsutiles import *
import matplotlib.pyplot as plt
import random

account = cleaned_account
posts = post_df

# Creation of a dictionary with each user id and information of the user


def dico_tot(p):  # p : percentage of followers who saw the post
    dico = {}
    for index, row in account.iterrows():
        # initialisation of the dictionary with basics caracterisitcs
        dico[row.id_user] = {'gender': row.sex,
                             'age': row.age,
                             'followers':  row.nb_followers,
                             'followings': row.nb_following,
                             'posts': row.nb_posts,
                             'original': False,
                             'repost': 0,
                             'total_views': 0,
                             'views_bf_post': 0,
                             'id_followers': row.id_followers,
                             'id_following': row.id_following,
                             'is_posting' : 0,
                             'influenciabilty': 0 #needs to be changed based on network
                             }  # Parameters we consider have an impact on the post propagation

    for index, row in posts.iterrows():

        if row.id_post_origin == 0:
            dico[row.id_user]['original'] = True
        
        dico[row.id_user]['repost'] += 1
        followers = dico[row.id_user]['id_followers']
        n = round(len(followers)*p*0.01)  # Number of people who saw the post
        followers_saw_post = random.sample(followers, n)
        for id in followers_saw_post:
            dico[int(id)]['total_views'] += 1
            if dico[int(id)]['repost'] == 0:
                dico[int(id)]['views_bf_post'] += 1
    return dico


def test(p):
    dico = dico_tot(p)
    rep = 0
    for row in dico:
        rep += dico[row]['repost']
    return rep

