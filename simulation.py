# This file (main?) will use the other ones to simulate the spreading process

def update(dico,g):
    #Prend en argument le dictionnaire de personnes à un instant et le réseau et fait le aps de temps suivant
    for person in dico:
        if dico[person]['is_posting'] == 1:
            post(person,g)
    
        
            
def post(person,network):
    