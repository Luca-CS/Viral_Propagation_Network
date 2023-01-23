import pandas as pd

def readcsv(fichier):
    
    file = pd.read_csv(fichier)
    return file

def dataframegraph(fichier):
    file = readcsv(fichier)
    newfile = file[['id_user','id_followers']]

    dico = {'id': [], 'follow': []}
    for index, row in newfile.iterrows():
        listefollowers = row['id_followers']
        rowid = row['id_user']
        string = listefollowers[1:-1]
        for follower in list(string.split(', ')):    
            dico['id'].append(rowid)
            dico['follow'].append(int(follower))        
    newnewfile = pd.DataFrame(dico) 
    
    return newnewfile
    
edge_df = dataframegraph('data/instagram_accounts.csv')
    

