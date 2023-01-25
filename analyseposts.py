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
def exp(l,k):
    return 1400*np.exp(-l*k)

liste = []
for index, row in post_df.iterrows():
    id_account = row['id_user']
    followers = int(cleaned_account[cleaned_account['id_user']==id_account]['nb_followers'])
    likes = row['likes']
    liste.append(likes/followers)
   
#print(liste)
    
X = np.linspace(0,2,100)
Y = [exp(6,x) for x in X]
plt.hist(liste, bins = 20)
plt.plot(X,Y,color='r', label='lambda = 6')
plt.xlabel('ratio likes/followers')
plt.ylabel("nombre d'occurences")
plt.show()

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