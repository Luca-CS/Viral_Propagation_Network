import pandas as pd


def readcsv(fichier):
    """
    Lit un fichier CSV 
    """
    file = pd.read_csv(fichier)
    return file

# Useful functions to clean the dataframes 


# Useful functions on account dataframes

def find_doublon(fichier):
    """_summary_

    Args:
        fichier (chemin): Chemin vers le ficier de la DF

    Returns:
        lst: liste des indices en double
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


#print("Les doublons sont :", find_doublon('data/instagram_accounts.csv'))



def clean_dataframe(fichier):
    """
    Nettoie les donnes et donne un tableau exploitable en sortie
    Entrée 
        - Chemin du fichier
    Sortie 
        - Dataframe exploitable
    """

    file = readcsv(fichier)
    lst = find_doublon(fichier)
    dico = {'id': [], 'follow': []}

    simple_file = file[['id_user', 'id_followers', 'nb_followers',
                        'nb_following', 'nb_posts', 'sex', 'birth_date']]

    clean_dic = {'id_user': [], 'nb_followers': [], 'nb_following': [], 'nb_posts': [
    ], 'sex': [], 'age': [], 'id_followers': [], 'id_following': []}

    clean_file = pd.DataFrame(clean_dic)

    for index, row in simple_file.iterrows():
        listefollowers = row['id_followers']
        rowid = row['id_user']
        string = listefollowers[1:-1]
        for follower in list(string.split(', ')):
            if not (int(follower) in lst) and not (int(rowid) in lst):
                dico['id'].append(int(follower))
                dico['follow'].append(int(rowid))

    dico_follower_ing = {}
    lst_source = dico['id']
    lst_target = dico['follow']

    for i in range(len(lst_source)):
        follower = lst_source[i]
        followed = lst_target[i]

        if follower not in dico_follower_ing:
            dico_follower_ing[follower] = {
                'id_followers': [], 'id_following': []}
        if followed not in dico_follower_ing:
            dico_follower_ing[followed] = {
                'id_followers': [], 'id_following': []}

        dico_follower_ing[follower]['id_following'].append(followed)
        dico_follower_ing[followed]['id_followers'].append(follower)

    for index, row in simple_file.iterrows():
        if not (row['id_user']) in lst:
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

            new_row = pd.DataFrame({'id_user': [id], 'nb_followers': [int(len(followers_lst))], 'nb_following': [int(len(following_lst))], 'nb_posts': [
                                   nb_post], 'sex': [sex], 'age': [age], 'id_followers': [followers_lst], 'id_following': [following_lst]})

            clean_file = pd.concat([clean_file, new_row])

    return (clean_file)


def clean_posts():
    lst  = find_doublon('data/instagram_accounts.csv')
    post_df = readcsv('data/instagram_posts_0911_1111.csv')
    
    for index_row,row in post_df.iterrows():
        if row.id_user in lst:
            post_df.drop(index = index_row, inplace=True)

    return(post_df)
    
            
        

def dataframegraph(dataframe):
    """_summary_

    Args:
        dataframe (DF): La dataframe nettoyée

    Returns:
        newnewfile (): la Dataframe des arrètes
    """
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


# Useful dataframes


account_df = readcsv('data/instagram_accounts.csv')
cleaned_account = clean_dataframe('data/instagram_accounts.csv')
edge_df = dataframegraph(cleaned_account)
post_df = clean_posts()






# Useful functions about account dataframe


def arborescence():
    """_summary_

    Returns:
        dictionnaire: dictionnaire disant le combientième repost est chaque post (0 -> original)
    """
    father_df = post_df[['id_post', 'id_post_origin']]
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


def repost_num():
    """_summary_

    Returns:
        dictionnaire: Dictionnaire donnant combiend de fois un post est reposté
    """
    dico = {}
    father_df = post_df[['id_post', 'id_post_origin']]

    for index, row in father_df.iterrows():
        father = row['id_post_origin']
        if father in dico:
            dico[father] += 1
        else:
            dico[father] = 1

    return dico


def time(row):
    """_summary_

    Args:
        row (Row of a DF): A row on the post DF

    Returns:
        t (int): Time since 09/11/2017 at 00:00 am
    """
    date = row['date']
    hour = row['time']
    half = row['half_day']

    t = 0

    date = date.split('/')
    hour = hour.split(':')

    if half == 'pm':
        t += 12 * 60

    day = date[0]
    if day == '10':
        t += 24 * 60
    elif day == '11':
        t += 48 * 60

    t += int(hour[0]) * 60 + int(hour[1])

    return t


def time_of_posts():
    dic = {}

    for index, row in post_df.iterrows():
        t = time(row)
        dic[int(row['id_post'])] = t

    return dic


def post_num():
    dic = {}
    for index, row in post_df.iterrows():
        id = row.id_user
        if id in dic:
            dic[id] += 1
        else:
            dic[id] = 1
    return dic

#print(post_num())    
    
    
# The following code allowed to check various things, it has useful bits to copy and paste

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
