

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

#paths
#letras
path_graficos="img"
path_rosco_azul=os.path.join(path_graficos,"rosco_azul")
path_rosco_rojo=os.path.join(path_graficos,"rosco_rojo")
path_rosco_verde=os.path.join(path_graficos,"rosco_verde")
#sonidos
path_sonido="sfx"
path_sonido_win=os.path.join(path_sonido,"wins")
path_sonido_fail=os.path.join(path_sonido,"fails")
path_sonido_next=os.path.join(path_sonido,"next")

#letras
letras=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
ROSCO_NOMBRE="rosco_"
ROSCO_EXTENSION=".png"

def initializer():
   # initialize the pygame module
    pygame.init()
    # Inicializamos sonido
    pygame.mixer.init()
    screen = pygame.display.set_mode((1024, 768))
    background = os.path.join(path_graficos,"fondo.png")
    bg = pygame.image.load(background)
    return screen, bg

def leer_archivos_en_carpeta(path):
    lista_archivos = os.listdir(path)
    return lista_archivos

def generar_diccionario_letra_imagen (path, lista_rosco_archivos):
    dict_rosco={}
    for letra in letras:
        if ROSCO_NOMBRE+letra+ROSCO_EXTENSION in lista_rosco_archivos:
            dict_rosco.update(dict([(letra, os.path.join(path, ROSCO_NOMBRE+letra+ROSCO_EXTENSION))]))
    return dict_rosco


def obtener_imagenes_rosco(path):
    lista_rosco_archivos=leer_archivos_en_carpeta(path)
    dict_rosco=generar_diccionario_letra_imagen(path,lista_rosco_archivos)
    return dict_rosco

def elegir_cancion(lista):
    numero_cancion=random.randint(0,len(lista)-1)
    return lista[numero_cancion]

def play_event_song(path):
    pygame.mixer.music.unload()
    lista_canciones = leer_archivos_en_carpeta(path)
    cancion=os. path.join(path,elegir_cancion(lista_canciones))
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play()

def cargar_rosco_inicial(rosco_azul, screen):
    for entrada in rosco_azul:
        letra = pygame.image.load(rosco_azul[entrada])
        screen.blit(letra, (180, 192))

def cambiar_letra(screen, events, rosco_azul, rosco_rojo, rosco_verde, contador):
    letra=None
    for event in events:
        if event.type==pygame.KEYDOWN:
            keys=pygame.key.get_pressed()
            if keys[pygame.K_1]:
                letra=pygame.image.load(rosco_verde[letras[contador]])
                play_event_song(path_sonido_win)
                screen.blit(letra, (180,192))
                contador+=1
            elif keys[pygame.K_2]:
                letra=pygame.image.load(rosco_rojo[letras[contador]])
                screen.blit(letra, (180,192))
                play_event_song(path_sonido_fail)
                contador+=1
            elif keys[pygame.K_3]:
                letra=pygame.image.load(rosco_azul[letras[contador]])
                screen.blit(letra, (180,192))
                play_event_song(path_sonido_next)
                contador+=1
        if contador>=len(letras):
            contador=0
    return contador
    

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

def main():
    screen, bg = initializer()
    rosco_rojo = obtener_imagenes_rosco(path_rosco_rojo)
    rosco_verde = obtener_imagenes_rosco(path_rosco_verde)
    rosco_azul = obtener_imagenes_rosco(path_rosco_azul)
    screen.fill((0,0,0))  
    screen.blit(bg,(0,0))
    cargar_rosco_inicial(rosco_azul, screen)
    pygame.display.flip()
    # define a variable to control the main loop
    running = True
    contador=0
    # main loop
    while running:
        events = pygame.event.get()
        running = detect_quit_events(events)
        contador=cambiar_letra(screen, events, rosco_azul, rosco_rojo, rosco_verde, contador)
        pygame_widgets.update(events)
        pygame.display.update()       
    pygame.quit()
    