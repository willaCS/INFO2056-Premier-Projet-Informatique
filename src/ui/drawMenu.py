import pygame
import Window
from globals import all

JAUNE = (255,255,0)
NOIR = (0, 0, 0)

BOUTON_LARGEUR = 300
BOUTON_HAUTEUR = 40
BOUTON_ESPACE = 1




def bouton_reglage():
    pygame.draw.rect(Window.inst, JAUNE, (((Window.half_resolution[0] - 150), (Window.half_resolution[1] + 50)), (BOUTON_LARGEUR, BOUTON_HAUTEUR)))
    bouton_reglage_texte = all.font2.render("Reglages", True, NOIR)
    Window.inst.blit(bouton_reglage_texte, (((Window.half_resolution[0] - 150) + 120), ((Window.half_resolution[1] + 50)) + 5))







def bouton_play():
    pygame.draw.rect(Window.inst, JAUNE, (((Window.half_resolution[0] - 150), (Window.half_resolution[1] + 130)), (BOUTON_LARGEUR, BOUTON_HAUTEUR)))
    bouton_play_texte = all.font2.render("PLAY", True, NOIR)
    Window.inst.blit(bouton_play_texte, (((Window.half_resolution[0] - 150) + 140), ((Window.half_resolution[1] + 130)) + 5))