import pygame
import os

pygame.init()

os.environ['SDL_VIDEO_WINDOW_POS'] = "350,100"

fenetre = pygame.display.set_mode((500, 500))

from Constantes import *
from Classes import *

pygame.display.set_caption(titre_fenetre)

#Création des objets grâce aux classes
carre_1 = Curseur()
carre_2 = Curseur()
carre_3 = Curseur()

#Initialisation des joysticks
nb_joysticks = pygame.joystick.get_count()
print("Il y a", nb_joysticks, "joystick(s) branché(s)")
if nb_joysticks > 0:
    joystick_1 = pygame.joystick.Joystick(0)
    joystick_2 = pygame.joystick.Joystick(1)
    joystick_1.init()
    joystick_2.init()
'''''print("Axes :", joystick_2.get_numaxes())
print("Boutons :", joystick_2.get_numbuttons())
print("Trackballs :", joystick_2.get_numballs())
print("Hats :", joystick_2.get_numhats())
#Vérification des joysticks
if event.type == pygame.JOYBUTTONDOWN:
print(event.button)'''''

while continuer_selec:
    #Affichage de l'écran de sélection
    fenetre.blit(Fond_2, (0, 0))
    fenetre.blit(Toads, (0, 325))
    fenetre.blit(Retour, (0, 0))
    fenetre.blit(J1, (60, 0))
    fenetre.blit(J2, (260, 0))
    fenetre.blit(J3, (150, 75))
    fenetre.blit(Donkey_Kong, (50, 175))
    fenetre.blit(Kirby, (135, 175))
    fenetre.blit(Link, (220, 175))
    fenetre.blit(Mario, (305, 175))
    fenetre.blit(Mega_Man, (390, 175))
    fenetre.blit(Pacman, (50, 243))
    fenetre.blit(Pikachu, (135, 243))
    fenetre.blit(Pit, (220, 243))
    fenetre.blit(Samus, (305, 243))
    fenetre.blit(Shovel_Knight, (390, 243))
    fenetre.blit(Sonic, (177, 311))
    fenetre.blit(Yoshi, (262, 311))
    fenetre.blit(Curseur_3, (carre_3.x, carre_3.y))
    fenetre.blit(carre_1.perso, (192, 13))
    fenetre.blit(Curseur_2, (carre_2.x, carre_2.y))
    fenetre.blit(carre_2.perso, (392, 13))
    fenetre.blit(Curseur_1, (carre_1.x, carre_1.y))
    fenetre.blit(carre_3.perso, (282, 88))

    #Rafraîchissement
    pygame.display.flip()

    pygame.time.Clock().tick(30)

    for event in pygame.event.get():
        #Vérification de fermeture de la fenêtre activée ou non
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and\
         event.key == pygame.K_ESCAPE:
            continuer_selec = 0
        #Vérification d'un clic
        elif event.type == pygame.KEYDOWN:
            #Déplacement du curseur 1
            if event.key == pygame.K_UP:
                carre_1.deplacer('haut')
            elif event.key == pygame.K_DOWN:
                carre_1.deplacer('bas')
            elif event.key == pygame.K_LEFT:
                carre_1.deplacer('gauche')
            elif event.key == pygame.K_RIGHT:
                carre_1.deplacer('droite')
            carre_1.placer()
        #Déplacement des curseurs par les joysticks
        elif event.type == pygame.JOYAXISMOTION:
            #Déplacement du curseur 2
            if event.joy == 0:
                if event.axis == 0 and event.value > 0.5:
                    carre_2.deplacer('droite')
                elif event.axis == 0 and event.value < - 0.5:
                    carre_2.deplacer('gauche')
                elif event.axis == 1 and event.value > 0.5:
                    carre_2.deplacer('bas')
                elif event.axis == 1 and event.value < - 0.5:
                    carre_2.deplacer('haut')
                carre_2.placer()
            #Déplacement du curseur 3
            elif event.joy == 1:
                if event.axis == 0 and event.value > 0.5:
                    carre_3.deplacer('droite')
                elif event.axis == 0 and event.value < - 0.5:
                    carre_3.deplacer('gauche')
                elif event.axis == 1 and event.value > 0.5:
                    carre_3.deplacer('bas')
                elif event.axis == 1 and event.value < - 0.5:
                    carre_3.deplacer('haut')
                carre_3.placer()
