import random
import re
import time
from multiprocessing import Process

# base de données
liste_syllabes = ["es", "pu", "me","an"]
mots_passes = [] 
listePays = [""]


# demander un mot
def demander_un_mot(syllabe_en_jeu):
    mot_en_jeu = input(syllabe_en_jeu + " ")
    return mot_en_jeu
    

# changement de syllabe
def changement_syllabe(liste_syllabes):
    syllabe_en_jeu = random.choice(liste_syllabes)
    return syllabe_en_jeu


# évite la répitition
def repetition(mot_en_jeu,mots_passes):
    mots_passes.append(mot_en_jeu)


#cherche si la syllabe est bien dans le mot et si le mot a déjà été dit
def recherche(syllabe_en_jeu, mot_en_jeu, mots_passes):
    for elem in mots_passes:
        if mot_en_jeu == elem:
            return False
    for m in re.finditer(syllabe_en_jeu, mot_en_jeu):
        return True
    return False
    

#jouer
def jouer(mots_passes):
    vie = 3
    while vie != 0:
        syllabe_en_jeu = changement_syllabe(liste_syllabes)
        mot_en_jeu = demander_un_mot(syllabe_en_jeu)

        while recherche(syllabe_en_jeu,mot_en_jeu,mots_passes) == False :
            print("mauvaise réponse")
            mot_en_jeu = demander_un_mot(syllabe_en_jeu) 
            vie -= 1 
        
        if recherche(syllabe_en_jeu,mot_en_jeu,mots_passes):
            print("bonne réponse")
            

jouer(mots_passes)
