import pygame
import random 

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

WHITE = (255,255,255)
BLACK = (0,0,0)
PINK = (255,153,204)
ORANGE = (255,128,0)

FONT = pygame.font.SysFont("arial",40)

def load_words():
    with open("mots.txt","r") as f :
        return f.read().splitlines()


# def add_words():
#     word =  input("Which word do you wish to add at the file ? ")
#     if word :
#         with open("mots.txt", "a") as file :
#             file.write(word + "\n")
#         print(f"The word {word} has been added to the file")
#     else : 
#         print("Word can't be empty")

def play():
    with open("mots.txt","r") as f :
        contenu = f.read().splitlines()
    word = random.choice(contenu)
    guessword = ["_"] * len(word)
    attempts = 0
    max_attempts = 7
    running = True
    font = pygame.font.Font(None, 50)
    other_font = pygame.font.Font(None, 30)


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
        