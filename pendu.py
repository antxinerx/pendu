H
import pygame
import random 

# mots = open('mots.txt','r')
# f = mots.readlines()
# listevide = []
# for ligne in f :
#     listevide.append(ligne[:-1])
# print(listevide)

def mots_fichier():
    try :
        with open("mots.txt", 'r') as fichier:
            fichier = mots.read()
        if not fichier :
            mots_initiaux = ["balai","orage","clementine","ordinateur","logiciel","telephone","souris","aspirateur",
                "machine","projet","numerique","technologie","encodage","corde","bateau"]
    #     with open("mots.txt", "w") as fichier :
    #         fichier.write("\n".join(mots_initiaux))
    # except FileNotFoundError:
    #     mots_initiaux = ["balai","orage","clementine","ordinateur","logiciel","telephone","souris","aspirateur",
    #     "machine","projet","numerique","technologie","encodage","corde","bateau"]
    #     with open("mots.txt","w") as fichier :
    #         fichier.write("\n".join(mots_initiaux))# mots = open('mots.txt','r')


# f = mots.readlines()

# listevide = []
# for ligne in f :
#     listevide.append(ligne[:-1])

# print(listevide)

def add_words():
    mot =  input("Voulez vous ajouter un mot ? ")
    if mot :
        with open(mots, "a") as fichier :
            fichier.write(mot + "\n")
        print(f"Le mot{mot} a bien été ajouter au fichier texte")
    else : 
        print("Le mot ne peut pas être vide")

        

# mots = open('mots.txt','r')


# f = mots.readlines()

# listevide = []
# for ligne in f :
#     listevide.append(ligne[:-1])

# print(listevide)




