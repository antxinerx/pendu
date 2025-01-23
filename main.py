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

def charger_mots():
    with open("mots.txt", "r") as fichier:
        mots = fichier.read().splitlines()
    return mots

def jeu_du_pendu():
    mots = charger_mots()
    mot_a_deviner = random.choice(mots).upper()
    lettres_trouvees = set()
    lettres_proposees = set()
    tentatives_restantes = 6

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
                            tentatives_restantes -= 1

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

        tentatives_affiche = f"Tentatives restantes : {tentatives_restantes}"
        texte = font.render(tentatives_affiche, True, COULEUR_TEXTE)
        fenetre.blit(texte, (50, 200))

        if set(mot_a_deviner) <= lettres_trouvees:
            texte = font.render("Gagné !", True, (0, 255, 0))
            fenetre.blit(texte, (50, 300))
            en_cours = False
        elif tentatives_restantes <= 0:
            texte = font.render(f"Perdu ! Le mot était : {mot_a_deviner}", True, (255, 0, 0))
            fenetre.blit(texte, (50, 300))
            en_cours = False

        pygame.display.flip()
        horloge.tick(FPS)

    pygame.quit()