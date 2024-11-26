import pygame
import Window

from globals import all, gestionMenu
 

ROUGE = (255,0,0)
NOIR = (0, 0, 0)
SILVER = (192,192,192)

BOUTON_RETOUR_LARGEUR = 50
BOUTON_RETOUR_HAUTEUR = 40
 
BOUTON_LARGEUR = 300
BOUTON_HAUTEUR = 40
BOUTON_ESPACE = 1




bouton_back = (((0 + 5), (0 + 10)), (BOUTON_RETOUR_LARGEUR, BOUTON_RETOUR_HAUTEUR))

def bouton_retour():
    pygame.draw.rect(Window.inst, ROUGE, (((0 + 5), (0 + 10)), (BOUTON_RETOUR_LARGEUR, BOUTON_RETOUR_HAUTEUR)))
    bouton_reglage_texte = all.font2.render("RETOUR", True, NOIR) 
    Window.inst.blit(bouton_reglage_texte, (((Window.half_resolution[0] - 2) - 4), ((Window.half_resolution[1] + 2)) + 5))
    




def gestion_settings():
    bouton_azerty()
    bouton_qwerty()



def bouton_azerty():
    pygame.draw.rect(Window.inst, SILVER, (((Window.half_resolution[0] - 150), (Window.half_resolution[1] + 50)), (BOUTON_LARGEUR, BOUTON_HAUTEUR)))
    bouton_reglage_texte = all.font2.render("AZERY", True, NOIR)
    Window.inst.blit(bouton_reglage_texte, (((Window.half_resolution[0] - 150) + 120), ((Window.half_resolution[1] + 50)) + 5))



def bouton_qwerty():
    pygame.draw.rect(Window.inst, SILVER, (((Window.half_resolution[0] - 150), (Window.half_resolution[1] + 130)), (BOUTON_LARGEUR, BOUTON_HAUTEUR)))
    bouton_play_texte = all.font2.render("QWERTY", True, NOIR)
    Window.inst.blit(bouton_play_texte, (((Window.half_resolution[0] - 150) + 140), ((Window.half_resolution[1] + 130)) + 5))


    

