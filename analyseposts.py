from fonctionsutiles import *
import matplotlib.pyplot as plt
import numpy as np

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

for i in account_df.index:
    id_account = account_df['id_user'][i]
    if id_account not in dico :
        followers = account_df['nb_followers'][i]
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
    return 440*np.exp(-l*k)

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
plt.hist(post_df['views'], bins = 20)
plt.xlabel('nombre de views')
plt.ylabel("nombre d'occurences")
plt.show()
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

