import math as ma
import numpy as np
from fonctionsutiles import *
import matplotlib.pyplot as plt
from dico_individus import *
from kpi import *

l0 = [638779430]
l1 = [953043456]
l2 = [650889385]
l3 = [144265898]

for index, row in post_df.iterrows():
    if row.id_post_origin in l0:
        l0.append(row.id_post)
    if row.id_post_origin in l1:
        l1.append(row.id_post)
    if row.id_post_origin in l2:
        l2.append(row.id_post)
    if row.id_post_origin in l3:
        l3.append(row.id_post)

# calcul du kpi par post originel


def kpi(liste):
    kpi, views, likes, comments, reposts, clicks, donations = 0, 0, 0, 0, 0, 0, 0

    for id in liste:
        row = post_df[post_df['id_post'] == id]
        views += int(row['views'])
        likes += int(row['likes'])
        comments += int(row['comments'])
        reposts += int(row['reposts'])
        clicks += int(row['link_clicks'])
        if str(row['donation_tag']) == 'TRUE':
            donations += 1

    kpi = views/251167 + likes/68109 + comments / \
        12730 + reposts/3043 + clicks/320 + donations/31
    return kpi


X = [0, 1, 2, 3]
Y = [kpi(l0), kpi(l1), kpi(l2), kpi(l3)]
print(Y)
plt.scatter(X, Y)
plt.show()


# import exponential

# Using exponential() method
gfg = 100*np.random.exponential(1/6, 10000)

count, bins, ignored = plt.hist(gfg, 14, density=True)
plt.show()

# Génère des reposts:


def influ_repost():
    dico = dico_tot(100)
    age = []
    nbr_people_age = 43*[0]
    esperance_kpi = 43*[0]
    for n in range(13, 57):
        age.append(n)
    for index, row in post_df.iterrows():
        id = row.user_id
        user_age = dico[id][age]
        nbr_people_age[user_age - 13] += 1
        esperance_kpi[user_age - 13] += get_kpi(int(row.post_id))
    for x in range(43):
        esperance_kpi[x] = esperance_kpi[x]/nbr_people_age[x]
    plt.scatter(age, esperance_kpi)
    plt.show


def influ_genre():
    dico = dico_tot(100)
    genre = [1, 2]
    nbr_people_genre = [0, 0]
    esperance_kpi = [0, 0]
    for index, row in post_df.iterrows():
        id = row.user_id
        if dico[id]['genre'] == 'female':
            nbr_people_genre[1] += 1
            esperance_kpi[1] += get_kpi(int(row.post_id))
        else:
            nbr_people_genre[0] += 1
            esperance_kpi[0] += get_kpi(int(row.post_id))
    esperance_kpi[0] *= 1/nbr_people_genre[0]
    esperance_kpi[1] *= 1/nbr_people_genre[1]
    plt.scatter
