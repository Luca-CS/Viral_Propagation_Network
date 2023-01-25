import igraph as ig
from fonctionsutiles import *
import matplotlib.pyplot as plt
import random

account = cleaned_account
posts = post_df
posts = posts.drop(index=1129)

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
                             'is_posting': 0,
                             'influenciabilty': 0  # needs to be changed based on network
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


# Number of people with a certain age who reposted
def age_posts():
    dico = dico_tot(100)
    age_post = []
    for row in dico:
        if dico[row]['repost'] != 0:
            age_post.append(int(dico[row]['age']))
    age_post.sort()

    liste_age = []
    for i in range(age_post[len(age_post)-1] + 1):
        liste_age.append(i)
    liste_nombre = (age_post[len(age_post)-1]+1)*[0]
    for x in age_post:
        liste_nombre[x] += 1
    return(liste_age, liste_nombre)


liste_age, liste_nombre = age_posts()
plt.plot(liste_age, liste_nombre)
plt.show()

# Number of reposts


def nbr_reposts():
    dico = dico_tot(100)
    repost = []
    for row in dico:
        if int(dico[row]['repost']) != 0:
            repost.append(int(dico[row]['repost']))
    repost.sort()
    print(repost)
    n = len(repost)
    max = repost[n-1]
    min = repost[0]
    if min == max:
        return([min], [len(repost)])
    else:
        nbr_people = [0]*(max)
        nbr_repost = []
        for i in range(1, max + 1):
            nbr_repost.append(i)
        for x in repost:
            nbr_people[x-1] += 1
        return(nbr_repost, nbr_people)


print(nbr_reposts())

nbr_repost, nbr_people = nbr_reposts()
plt.plot(nbr_repost, nbr_people)
plt.show()
