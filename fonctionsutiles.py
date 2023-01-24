import pandas as pd


def readcsv(fichier):
    file = pd.read_csv(fichier)
    return file


post_df = readcsv('data/instagram_posts_0911_1111.csv')
account_df = readcsv('data/instagram_accounts.csv')


def dataframegraph(fichier):
    file = readcsv(fichier)
    newfile = file[['id_user', 'id_followers', 'nb_followers']]
    dico = {'id': [], 'follow': []}
    for index, row in newfile.iterrows():
        listefollowers = row['id_followers']
        rowid = row['id_user']
        string = listefollowers[1:-1]
        for follower in list(string.split(', ')):
            dico['id'].append(int(follower))
            dico['follow'].append(rowid)
    newnewfile = pd.DataFrame(dico)
    return newnewfile


edge_df = dataframegraph('data/instagram_accounts.csv')


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


# The following code allowed to check that the followers list and numbers of followers where consistent
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