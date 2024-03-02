

#############################################
#          PASAPALABRA-PYTHON*** v.0.0 : 2024-02-29           #
#         Copyright (c) 2024 Dan Gordillo, Daniel Ayerra           #
#                     GNU General Public License 3.0                            #
# This program comes with ABSOLUTELY NO WARRANTY #
# This is free software, and you are welcome to                    #
# redistribute it under certain conditions.                                #
###################################*#########

import os;
import random
import pygame;
import pygame_widgets;
from pygame_widgets.button import Button;
import debugpy

debugpy.listen(5678)
debugpy.wait_for_client() 

path_graficos="img/"
path_rosco_azul="img/rosco_azul/"
path_rosco_rojo="img/rosco_rojo/"
path_rosco_gris="img/rosco_gris"
path_sonido="sfx/"
path_sonido_win=path_sonido+"wins"
path_sonido_fail=path_sonido+"fails"
path_sonido_next=path_sonido+"next"
letras=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
puntos=0
began=False
ended=False

def leer_archivos_en_carpeta(path):
    lista_archivos = os.listdir(path)
    breakpoint()
    return lista_archivos

def elegir_cancion(lista):
    numero_cancion=random.randint(0,len(lista)-1)
    return lista[numero_cancion]

def play_song(path):
    pygame.mixer.music.unload()
    print(path)
    lista_canciones = leer_archivos_en_carpeta(path)
    cancion=os. path.join(path,elegir_cancion(lista_canciones))
    print(cancion)
    pygame.mixer.music.load(cancion)
    breakpoint()
    pygame.mixer.music.play()

def detect_quit_events(events):
    running=True
    for event in events:
        if event.type == pygame.QUIT:
            running=False
        if event.type == pygame.KEYDOWN:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                running = False
    return running


# define a main function
def main():
    
    # initialize the pygame module
    pygame.init()
    # Inicializamos sonido
    pygame.mixer.init()
    # load and set the logo
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    # pygame.display.set_caption("minimal program")
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((1024, 768))
    background = path_graficos+"fondo.png"
    bg = pygame.image.load(background)
    screen.fill((0,0,0))  
    screen.blit(bg,(0,0))
    pygame.display.flip()
    breakpoint()
    buttonwin = Button(screen, 20, 568, 300, 70, text='Random Win Melody', inactiveColour=(200, 50, 0), activeColour=(0,50,200), pressedColour=(0, 200, 20), radius=20, onClick=lambda:play_song(path_sonido_win))
    button_fail = Button(screen, 330, 568, 300, 70, text='Random Fail Melody', inactiveColour=(200, 50, 0), activeColour=(0,50,200), pressedColour=(0, 200, 20), radius=20, onClick=lambda:play_song(path_sonido_fail))
    button_next = Button(screen, 650, 568, 300, 70, text='Random Next Melody', inactiveColour=(200, 50, 0), activeColour=(0,50,200), pressedColour=(0, 200, 20), radius=20, onClick=lambda:play_song(path_sonido_next))
    # define a variable to control the main loop
    running = True
    # main loop
    while running:
        events = pygame.event.get()
        running = detect_quit_events(events)
        screen.fill((0,0,0))
        screen.blit(bg,(0,0))
        pygame_widgets.update(events)
        pygame.display.update()       
    pygame.quit()
    