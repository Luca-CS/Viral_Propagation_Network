from fonctionsutiles import *
import numpy as np
# This file (main?) will use the other ones to simulate the spreading process
# Here, we have access to a global dictionnary of vertex characteristics

from numpy.random import choice

# Global variables :

"""Dictionnaire des individus
    Paramètres de vue, like, comment, click, donate"""

dico = {}
for index, row in cleaned_account.iterrows():
        # initialisation of the dictionary with basics caracterisitcs
    dico[row.id_user] = {'total_views': 0,
                         'total_likes': 0,
                         'total_comments': 0,
                         'total_click': 0,
                         'total_donations': 0,
                         'posting': (0,0), # first number = is posting at this timestamp, second number = will post at the next timestamp)
                         'posted': 0, # 1 if the user already posted something, turns back to 0 after a while (so that the user can post again)
                         'iterations_since_post':0
                        }  # Parameters we consider have an impact on the post propagation





# Functions to use
    
        
            
def post(poster,network,scores,dico):
    # To do list : 
    # Likes, comments, site visits, donations, 
    # REPOST
    
    # Variables : vertex id, the graph, a score dictionnary
    
    action_dic = action_number(poster)
    rank_lst = post_rank(poster,network,scores)
    choice_dic= choose(action_dic, rank_lst)
    action_update(choice_dic)
    
    #For the reposts 
    
    
    return 

def action_number(poster,dico):
    # Returns a dictionnary of the number of persons doing each action
    action_dic = {'view': 0, 'like': 0, 'comment': 0, 'click': 0, 'donate':0}
    
    followers = int(cleaned_account[cleaned_account['id_user']==poster]['nb_followers'])
    nb_likes = followers*np.random.exponential(6, 1)[0]
    
    return action_dic
    

def score(network,dico):
    score_dic = {}
    # Donne le score global sans prendre en compte les follows
    for user in dico:
        s = 0
        user_d = dico[user]
        
        view = user_d['view'][0]
        likes = user_d['like'][0]
        comm = user_d['comment'][0]
        click = user_d['clicks'][0]
        donate = user_d['donation'][0]
        inf = user_d['influenciability'][0]
        
        s += view + 20*likes + 200*comm + 400*click + 4000 * donate + inf
        s *= (inf+1)/2
        
        score_dic[user] = s
    return score_dic
        

def post_rank(graph,poster,network,score_dic,dico):    
    # Ajoute le score propre à la relation de follow et trie la liste
    for key in score_dic:
        score = score_dic[key]
        if graph.are_connected(key,poster):
            score *= 2
        score_dic[key] = score
    return sorted(score_dic, key=score_dic.get, reverse=True)
    


def choose(action_dic,rank_lst,dico):
    # Outputs the choice dictionnary where a list reprensetns the user_ids that will do the actions
    #view_choice = choice(rank_lst, action_dic['view'],p = )
    choice_dic = {'view': [], 'like': [], 'comment': [], 'click': [], 'donate':[]}
    for key in choice_dic:
        choice_dic[key] = rank_lst[0:action_dic[key]]
    return choice_dic

def action_update(choice_dic,dico):
    
    #vues:
    for id in choice_dic['view']:
        dico[id]['total_views']+=1
    #like:
    for id in choice_dic['like']:
        dico[id]['total_likes']+=1
    #comment:
    for id in choice_dic['comment']:
        dico[id]['total_comments']+=1
    #click:
    for id in choice_dic['click']:
        dico[id]['total_click']+=1
    #dons:
    for id in choice_dic['donate']:
        dico[id]['total_donations']+=1
    # Updates the values of the dictionnary absed on the actions done (changes second value of tuple)
    # Returns nothing
    return dico

# Final function

def update(dico,g):
    #Prend en argument le dictionnaire de personnes à un instant et le réseau et fait le pas de temps suivant
    general_score = score(g,dico)
    for person in dico:
        if dico[person]['is_posting'][0] == 1:
            post(person,g,general_score,dico)
    