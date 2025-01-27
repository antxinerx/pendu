import pygame
import random

pygame.init()

LARGEUR, HAUTEUR = 800, 600
FPS = 30
COULEUR_FOND = (255, 255, 255)
COULEUR_TEXTE = (0, 0, 0)

fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu du Pendu")
horloge = pygame.time.Clock()

def menu_principal():
    en_cours = True
    choix = 0
    options = ["Jouer","Ajouter des mots","Quitter"]

    while en_cours :
        fenetre.fill(COULEUR_FOND)

        font_titre = pygame.font.Font(None, 74)
        titre = font_titre.render("Jeu du Pendu", True, COULEUR_TEXTE)
        fenetre.blit(titre, (250,100))

        font_options = pygame.font.Font(None, 50)
        for i, option in enumerate(options):
            couleur = (0,0,255) if i == choix else COULEUR_TEXTE
            texte_option = font_options.render(option, True, couleur)
            fenetre.blit(texte_option, (350,250 + i * 50))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    choix = (choix + 1) % len(options)
                elif event.key == pygame.K_UP :
                    choix = (choix - 1)% len(options)
                elif event.key == pygame.K_RETURN:
                    if choix == 0:
                        jeu_du_pendu()
                    elif choix == 1:
                        ajouter_mot()
                    elif choix == 2:
                        pygame.quit()
                        exit()

def ajouter_mot():
    en_cours = True
    mot = ""
    while en_cours:
        fenetre.fill(COULEUR_FOND)
        font = pygame.font.Font(None, 50)
        texte = font.render ("Entrez un mot :",True, COULEUR_TEXTE)
        fenetre.blit(texte, (50, 100))
        mot_affiche = font.render(mot, True, (0, 0, 255))
        fenetre.blit(mot_affiche, (50, 200))
        pygame.display.flip()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if mot:
                        with open("mots.txt","a") as fichier : 
                            fichier.write(f"\n{mot.strip()}")
                        en_cours = False
                elif event.key == pygame.K_BACKSPACE:
                    mot = mot[:-1]
                elif pygame.K_a <= event.key <= pygame.K_z:
                    mot += event.unicode

def charger_mots():
    with open("mots.txt", "r") as fichier:
        mots = fichier.read().splitlines()
    return mots

def jeu_du_pendu():
    mots = charger_mots()
    mot_a_deviner = random.choice(mots).upper()
    lettres_trouvees = set()
    lettres_proposees = set()
    tentatives_restantes = 1

    en_cours = True
    while en_cours:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                en_cours = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    en_cours = False
                elif event.key >= pygame.K_a and event.key <= pygame.K_z:
                    lettre = chr(event.key).upper()
                    if lettre not in lettres_proposees:
                        lettres_proposees.add(lettre)
                        if lettre in mot_a_deviner:
                            lettres_trouvees.add(lettre)
                        else:
                            tentatives_restantes += 1

        fenetre.fill(COULEUR_FOND)

        mot_affiche = ""
        for lettre in mot_a_deviner:
            if lettre in lettres_trouvees:
                mot_affiche += lettre + " "
            else:
                mot_affiche += "_ "
        font = pygame.font.Font(None, 74)
        texte = font.render(mot_affiche, True, COULEUR_TEXTE)
        fenetre.blit(texte, (50, 50))

        lettres_proposees_affiche = "Lettres proposées : " + ", ".join(sorted(lettres_proposees))
        font = pygame.font.Font(None, 36)
        texte = font.render(lettres_proposees_affiche, True, COULEUR_TEXTE)
        fenetre.blit(texte, (50, 150))

        if tentatives_restantes > 1 :
            imp = pygame.image.load(f"step {tentatives_restantes}.png").convert()
            fenetre.blit(imp, (50, 200))

        if set(mot_a_deviner) <= lettres_trouvees:
            texte = font.render("Gagné !", True, (255, 0, 0))
            rejouer = font.render("Pour rejouer appuyez sur espace", True, (255, 0, 0))
            fenetre.blit(texte, (50, 300))
            fenetre.blit(rejouer, (50, 400))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jeu_du_pendu()

            
        elif tentatives_restantes >= 7:
            texte = font.render(f"Perdu ! Le mot était : {mot_a_deviner}", True, (255, 0, 0))
            rejouer = font.render("Pour rejouer appuyez sur espace", True, (255, 0, 0))
            fenetre.blit(texte, (50, 300))
            fenetre.blit(rejouer, (50, 400))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jeu_du_pendu()

        pygame.display.flip()
        horloge.tick(FPS)

    pygame.quit()
menu_principal()