# This file (main?) will use the other ones to simulate the spreading process
# Here, we have access to a global dictionnary of vertex characteristics

# Global variables :

"""Dictionnaire des individus
    Paramètres de vue, like, comment, click, donate"""





# Functions to use
    
        
            
def post(poster,network,scores):
    # To do list : 
    # Likes, comments, site visits, donations, 
    # REPOST
    
    # Variables : vertex id, the graph, a score dictionnary
    
    action_dic = action_number(poster)
    rank_lst = post_rank(poster,network,scores)
    choice_dic= choice(action_dic, rank_lst)
    action_update(choice_dic)
    
    #For the reposts 
    
    
    return 

def action_number(poster):
    # Returns a dictionnary of the number of persons doing each action
    action_dic = {'view': 0, 'like': 0, 'comment': 0, 'click': 0, 'donate':0}
    
    return action_dic
    

def score(network):
    score_dic = {}
    # Donne le score global sans prendre en compte les follows
    return score_dic

def post_rank(poster,network,score_dic):
    rank_lst = []
    # Ajoute le score propre à la relation de follow et trie la liste
    return rank_lst

def choice(action_dic,rank_lst):
    # Outputs the choice dictionnary where a list reprensetns the user_ids that will do the actions
    choice_dic = {'view': [], 'like': [], 'comment': [], 'click': [], 'donate':[]}
    return choice_dic

def action_update(choice_dic):
    # Updates the values of the dictionnary absed on the actions done (changes second value of tuple)
    # Returns nothing
    return 

# Final function

def update(dico,g):
    #Prend en argument le dictionnaire de personnes à un instant et le réseau et fait le pas de temps suivant
    general_score = score(g)
    for person in dico:
        if dico[person]['is_posting'] == 1:
            post(person,g,general_score)
    