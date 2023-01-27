# Generation of all used graphs

from fonctionsutiles import *
from dico_individus import *
from kpi import *
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
import math as ma


'''
#reposts par rapport aux views

print(post_df)
plt.scatter(post_df['views'], post_df['reposts'], color = 'g')
plt.plot([0,400],[0,400], color='r')
plt.xlabel('views')
plt.ylabel('reposts')
plt.show()
'''

'''

dico = {'nb_views':[],'reposts_en_moyenne':[]}
for k in range (max(post_df['views'])):
    df = post_df[post_df['views']==k]
    
    if len(df.index)!=0:
        dico['nb_views'].append(k)
        dico['reposts_en_moyenne'].append(sum(df['reposts'])/len(df.index))

plt.scatter(dico['nb_views'], dico['reposts_en_moyenne'], color = 'g')
plt.xlabel('nombre de views')
plt.ylabel('reposts en moyenne')
plt.show()

'''
'''
listedico = []
for k in range(max(post_df['views'])):
    dico = {}
    df = post_df[post_df['views']==k]
    for i in df.index:
        nbreposts = post_df['reposts'][i]
        if nbreposts in dico:
            dico[nbreposts]+=1
        else:
            dico[nbreposts]=1
    listedico.append(dico)

for k in range(len(listedico)):
    if listedico[k]!={}:
        X = []
        Y = []
        for cle in listedico[k].keys(): 
            X.append(cle)
            Y.append(listedico[k][cle])
        plt.plot(X,Y)
        
plt.show()
    
'''
'''
dico = {}

for index, row in cleaned_account.iterrows():
    id_account = row['id_user']
    if id_account not in dico :
        followers = cleaned_account[cleaned_account['id_user']==id_account]['nb_followers']
        df = post_df[post_df['id_user']==id_account]        #dataframe avec que les posts de ce user
        if len(df.index) != 0:
            somme = 0
            for k in df.index:
                ratio = df['likes'][k]/followers
                somme+= ratio
            dico[id_account]=[followers,somme/len(df.index)]


X = []
Y = []

for cle in dico :
    X.append(dico[cle][0])
    Y.append(dico[cle][1])
                
plt.scatter(X,Y)
plt.xlabel('nombre de followers')
plt.ylabel('ratio (likes/followers) par post en moyenne')
plt.show()
        
'''
'''
def exp(l,k):
    return 1600*np.exp(-l*k)

liste = []
for index, row in post_df.iterrows():
    id_account = row['id_user']
    followers = int(cleaned_account[cleaned_account['id_user']==id_account]['nb_followers'])
    comments = row['comments']
    liste.append(comments/followers)
   
#print(liste)
    
X = np.linspace(0,0.30,100)
Y = [exp(30,x) for x in X]
plt.hist(liste, bins = 20)
plt.plot(X,Y,color='r', label='lambda = 30')
plt.xlabel('ratio comments/followers')
plt.ylabel("nombre d'occurences")
plt.legend()
plt.show()
'''
'''
dico = {}

for i in account_df.index:
    id_account = account_df['id_user'][i]
    if id_account not in dico :
        followers = account_df['nb_followers'][i]
        df = post_df[post_df['id_user']==id_account]        #dataframe avec que les posts de ce user
        if len(df.index) != 0:
            somme = 0
            for k in df.index:
                somme+= df['likes'][k]
            dico[id_account]=[followers,somme/len(df.index)]

X = []
Y = []

for cle in dico :
    X.append(dico[cle][0])
    Y.append(dico[cle][1])
                
plt.scatter(X,Y)
plt.xlabel('nombre de followers')
plt.ylabel('likes par post en moyenne')
plt.show()

'''
'''
def exp(l,k):
    return 1200*np.exp(-l*k)

X = [i for i in range(180)]
Y = [exp(0.05,x) for x in X]
plt.hist(post_df['likes'], bins = 20)
plt.plot(X,Y,color='r', label='lambda = 0.05')
plt.xlabel('nombre de likes')
plt.ylabel("nombre d'occurences")
plt.legend()
plt.show()

'''
'''
print(np.random.exponential(0.05, 10))
'''
'''
plt.hist(account_df['nb_followers'], bins = 20)
plt.show()
'''
'''
dico = {}

for i in account_df.index:
    id_account = account_df['id_user'][i]
    if id_account not in dico :
        followers = account_df['nb_followers'][i]
        df = post_df[post_df['id_user']==id_account]        #dataframe avec que les posts de ce user
        if len(df.index) != 0:
            somme = 0
            for k in df.index:
                somme+= df['views'][k]
            dico[id_account]=[followers,somme/len(df.index)]

X = []
Y = []

for cle in dico :
    X.append(dico[cle][0])
    Y.append(dico[cle][1])
                
plt.scatter(X,Y)
plt.xlabel('nombre de followers')
plt.ylabel('views par post en moyenne')
plt.show()
'''

'''
post_df2 = readcsv('data/instagram_posts_1211_1611.csv')

plt.hist(post_df['views'], bins = 100)
plt.xlabel('nombre de views')
plt.ylabel("nombre d'occurences")
plt.show()

'''
'''
dico = {}

for i in account_df.index:
    id_account = account_df['id_user'][i]
    if id_account not in dico :
        activite = account_df['nb_posts'][i]
        df = post_df[post_df['id_user']==id_account]        #dataframe avec que les posts de ce user
        if len(df.index) != 0:
            somme = 0
            for k in df.index:
                somme+= df['views'][k]
            dico[id_account]=[activite,somme/len(df.index)]

X = []
Y = []

for cle in dico :
    X.append(dico[cle][0])
    Y.append(dico[cle][1])
                
plt.scatter(X,Y)
plt.xlabel('nombre de posts sur le compte insta qui poste')
plt.ylabel('views par post en moyenne')
plt.show()
'''
'''
dico = {}

for i in account_df.index:
    id_account = account_df['id_user'][i]
    if id_account not in dico :
        followers = account_df['nb_followers'][i]
        df = post_df[post_df['id_user']==id_account]        #dataframe avec que les posts de ce user
        if len(df.index) != 0:
            somme = 0
            for k in df.index:
                somme+= df['reposts'][k]
            dico[id_account]=[followers,somme/len(df.index)]

X = []
Y = []

for cle in dico :
    X.append(dico[cle][0])
    Y.append(dico[cle][1])
                
plt.scatter(X,Y)
plt.xlabel('nombre de followers')
plt.ylabel('reposts par post en moyenne')
plt.show()
'''
'''
def normale(sigma,mu,k):
    return 1800*np.exp(-((k-mu)/sigma)**2/2)/(sigma*np.sqrt(2*np.pi))

X = [i for i in range(20)]
Y = [normale(2,1,x) for x in X]
plt.plot(X,Y,color='r', label='sigma = 2, mu = 1')

plt.hist(post_df['reposts'], bins = 20)
plt.xlabel('nombre de reposts')
plt.ylabel("nombre d'occurences")
plt.legend()
plt.show()
'''
'''
def exp(l,k):
    return 450*np.exp(-l*k)

X = [i for i in range(40)]
Y = [exp(0.2,x) for x in X]
plt.hist(post_df['comments'], bins = 20)
plt.plot(X,Y,color='r', label='lambda = 0.2')
plt.xlabel('nombre de comments')
plt.ylabel("nombre d'occurences")
plt.legend()
plt.show()
'''



"""l0 = [638779430]
l1 = [953043456]
l2 = [144265898]
l3 = [650889385]

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

kpi0 = kpi(l0)
kpi1 = kpi(l1)
kpi2 = kpi(l2)
kpi3 = kpi(l3)



p0 = int(post_df[post_df['id_post'] == l0[0]]['id_user'])
p1 = int(post_df[post_df['id_post'] == l1[0]]['id_user'])
p2 = int(post_df[post_df['id_post'] == l2[0]]['id_user'])
p3 = int(post_df[post_df['id_post'] == l3[0]]['id_user'])
print(p0)
personnes = [p0,p1,p2,p3]

genre = []


for p in personnes:
    genre.append(cleaned_account[cleaned_account['id_user']==p]['sex'])

print(genre)


activite = []

for p in personnes:
    activite.append(int(cleaned_account[cleaned_account['id_user']==p]['nb_posts']))
    
    
followers = []

for p in personnes:
    followers.append(int(cleaned_account[cleaned_account['id_user']==p]['nb_followers']))
    
age = []

for p in personnes:
    age.append(int(cleaned_account[cleaned_account['id_user']==p]['age']))

listekpi = [kpi0,kpi1,kpi2,kpi3]
#plt.scatter([1,2,3,4],listekpi)
#plt.scatter([1,2,3,4],activite)
#plt.scatter([1,2,3,4],followers)
#plt.scatter([1,2,3,4],age)
plt.xlabel('original poster')
plt.ylabel('total kpi')
plt.show()"""

'''
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
'''
# Génère des reposts:

'''
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
        id = row.id_user
        if id in dico :
            if dico[id]['gender'] == 'female':
                nbr_people_genre[1] += 1
                esperance_kpi[1] += get_kpi(int(row.id_post))
            else:
                nbr_people_genre[0] += 1
                esperance_kpi[0] += get_kpi(int(row.id_post))
    esperance_kpi[0] *= 1/nbr_people_genre[0]
    esperance_kpi[1] *= 1/nbr_people_genre[1]
    return esperance_kpi,nbr_people_genre
    
X,Y = influ_genre()
print(X)
print(Y)
plt.scatter(X,Y)
plt.show()
'''