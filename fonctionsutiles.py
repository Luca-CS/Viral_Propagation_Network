import pandas as pd


def readcsv(fichier):
    
    # Lit un fichier CSV 
    
    file = pd.read_csv(fichier)
    return file


post_df = readcsv('data/instagram_posts_0911_1111.csv')
account_df = readcsv('data/instagram_accounts.csv')



def find_doublon(fichier):
    """
    Trouve les doublons d'identifiant 
    Entrée 
        - Chemin du fichier
    Sortie 
        - Liste des doublons
    """
    
    file = readcsv(fichier)
    lst_double = []
    dico = {}
    for index, row in file.iterrows(): 
        id = row['id_user']
        if id in dico:
            lst_double.append(id)
        else:
            dico[id] = 1
    
    return lst_double
    
def clean_dataframe(fichier):
    """
    Nettoie les donnes et donne un tableau exploitable en sortie
    Entrée 
        - Chemin du fichier
    Sortie 
        - Dataframe exploitable"""

    file  = readcsv(fichier)
    lst = find_doublon(fichier)
    dico = {'id': [], 'follow': []}
    
    simple_file = file[['id_user', 'id_followers', 'nb_followers','nb_following','nb_posts','sex','birth_date']]
    
    clean_dic = {'id_user' : [], 'nb_followers' : [], 'nb_following' : [], 'nb_posts' : [], 'sex' : [], 'age' : [], 'id_followers' : [], 'id_following' : []}
    
    clean_file = pd.DataFrame(clean_dic)
    
    
    for index, row in simple_file.iterrows():
        listefollowers = row['id_followers']
        rowid = row['id_user']
        string = listefollowers[1:-1]
        for follower in list(string.split(', ')):
            if not(int(follower) in lst) and not(int(rowid) in lst):
                dico['id'].append(int(follower))
                dico['follow'].append(int(rowid))
    
    dico_follower_ing = {}
    lst_source = dico['id']
    lst_target = dico['follow']
    
    for i in range(len(lst_source)):
        follower = lst_source[i]
        followed = lst_target[i]
        
        if follower not in dico_follower_ing:
            dico_follower_ing[follower] = {'id_followers' : [], 'id_following' : []}
        if followed not in dico_follower_ing:
            dico_follower_ing[followed] = {'id_followers' : [], 'id_following' : []}
        
        dico_follower_ing[follower]['id_following'].append(followed)
        dico_follower_ing[followed]['id_followers'].append(follower)
        
        
    for index,row in simple_file.iterrows():
        if not(row['id_user']) in lst:
            id = int(row['id_user'])
            sex = row['sex']
            nb_post = int(row['nb_posts'])
            
            followers_lst = dico_follower_ing[int(id)]['id_followers']
            following_lst = dico_follower_ing[int(id)]['id_following']

            
            birth_str = row['birth_date']
            birth_list = list(birth_str.split('/'))
            year = int(birth_list[-1])
            if year > 1000:
                age = 2017 - year
            elif year < 20:
                age = 17 - year
            else:
                age = 17 + 100 - year
            age = int(age)
                
            new_row = pd.DataFrame({'id_user' : [id], 'nb_followers' : [int(len(followers_lst))], 'nb_following' : [int(len(following_lst))], 'nb_posts' : [nb_post], 'sex' :[sex], 'age' : [age], 'id_followers' : [followers_lst], 'id_following' : [following_lst]})
            
            clean_file = pd.concat([clean_file,new_row])
    
    return(clean_file)

cleaned_account = clean_dataframe('data/instagram_accounts.csv')

def dataframegraph(dataframe):
    newfile = dataframe[['id_user', 'id_followers']]
    dico = {'id': [], 'follow': []}
    for index, row in newfile.iterrows():
        listefollowers = row['id_followers']
        rowid = row['id_user']
        for follower in listefollowers:
            dico['id'].append(int(follower))
            dico['follow'].append(rowid)
    newnewfile = pd.DataFrame(dico)
    return newnewfile

edge_df = dataframegraph(cleaned_account)

def arborescence():
    father_df = post_df[['id_post', 'id_post_origin']]
    print(father_df)
    id_list = []
    for index, row in father_df.iterrows():
        id_list.append(row['id_post'])

    father_dic = {}
    for index, row in father_df.iterrows():
        father = row['id_post_origin']
        if father == 0:
            father_dic[row['id_post']] = 0
        else:
            father_dic[row['id_post']] = 1 + father_dic[father]

    return father_dic


# The following code allowed to check various things,, it has useful bits to copy and paste

""" 
followers_df = account_df[['id_user','nb_followers','id_followers']]

max = 0
for index, row in followers_df.iterrows():
    listefollowers = row['id_followers']
    rowid = row['id_user']
    nb = row['nb_followers']
    string = listefollowers[1:-1]
    lst = list(string.split(', '))
    if len(lst) != nb:
        print('AAAAAAA')
    if max < nb:
        max = nb

print(max)
"""

""" 
account_df = readcsv('data/instagram_accounts.csv')

print(account_df)

dico = {}
for index, row in account_df.iterrows():
    id = row['id_user']
    if id in dico:
        dico[id] += 1
    else:
        dico[id] = 1
    if dico[id] > 1:
        print((id,dico[id]))
        """



"""dico_test = {}
for index, row in edge_df.iterrows():
    id = row['id']
    follow = row['follow']
    if id in dico_test:
        dico_test[id] += 1
    else :
        dico_test[id] = 1

print(dico_test)"""
