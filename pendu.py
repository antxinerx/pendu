import pygame
import random 

def mots_fichier():
    try :
        with open("mots.txt", 'r') as file:
            contenu = file.read()
        if not contenu :
            raise FileNotFoundError
    except FileNotFoundError:
        initials_words = ["balai","orage","clementine","ordinateur","logiciel","telephone","souris","aspirateur",
        "machine","projet","numerique","technologie","encodage","corde","bateau"]
        with open("mots.txt","a") as file :
            file.write("\n".join(initials_words))

def add_words():
    word =  input("Which word do you wish to add at the file ? ")
    if word :
        with open("mots.txt", "a") as file :
            file.write(word + "\n")
        print(f"The word {word} has been added to the file")
    else : 
        print("Word can't be empty")

def play():
    f = open("mots.txt",'r')
    contenu = f.read().splitlines()
    f.close()
    word = random.choice(contenu)
    guessword = ["_"for i in word]
    print(guessword)

    attempts = 0
    max_attempts = 7

    while guessword.count("_") > 0:
        if attempts >= max_attempts : 
            print("You cannot continue, limit of attempts reach")
            print("The word was :" , word)
            break
        user_input = input("take a guess")
        index = 0
        correct_guess = False
        while index < len(word):
            if user_input == word[index]:
                guessword[index] = word[index]
                correct_guess = True
            index +=1
        if not correct_guess :
            attempts += 1
            print(f"Essais restants : {max_attempts - attempts}")
        print(guessword)

def menu():
    mots_fichier()
    while True : 
        print("= Menu =")
        print("1. Play to hangmen")
        print("2. Add a word to a file")
        print("3. Quit ")
        choix = input("Please enter your choice")

        if choix == "1":
            play()
        if choix =="2":
            add_words()
        if choix == "3":
            print("Bye !")
            break
menu()


        




