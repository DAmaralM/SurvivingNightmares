import pygame

import constantes

from menu import cMenu, EVENT_CHANGE_STATE 
from pygame.locals import *

from habitacion1 import Habitacion_1
from habitacion2 import Habitacion_2
from habitacion3 import Habitacion_3
from habitacion4 import Habitacion_4
from habitacion5 import Habitacion_5
from habitacion6 import Habitacion_6

from jugador import Jugador
from time import time
from funciones_spritesheet import *

import enemigos



def jugar(pygame, constantes, pantalla,jugador):
    
    """ Clase principal en el que se debe ejecutar el juego. """
    
    tiempo_comienzo = time() + 200
    
    # Creamos al jugador con la imagen p1_walk.png
    jugador_principal = Jugador(jugador)
    letraParaPuntos = pygame.font.Font(None, 50)
    letraParaVidas = pygame.font.Font(None, 50)
    letraParaGameOver = pygame.font.Font(None, 45)
    relojmarcador = pygame.image.load("imagenes/relojmarcador.png")
    puntosmarcador = pygame.image.load("imagenes/llave.png")
    vidasmarcador = pygame.image.load("imagenes/vidas.png")
    gameovertime = pygame.image.load("imagenes/gameovertime.png")
    gameover = pygame.image.load("imagenes/gameover.png")
    

# Creamos todos los niveles del juego
    lista_niveles = []
    lista_niveles.append(Habitacion_1(jugador_principal))
    lista_niveles.append(Habitacion_2(jugador_principal))
    lista_niveles.append(Habitacion_3(jugador_principal))
    lista_niveles.append(Habitacion_4(jugador_principal))
    lista_niveles.append(Habitacion_5(jugador_principal))
    lista_niveles.append(Habitacion_6(jugador_principal))
# Seteamos cual es el primer nivel.
    numero_del_nivel_actual = 0
    nivel_actual = lista_niveles[numero_del_nivel_actual]
    lista_sprites_activos = pygame.sprite.Group()
    jugador_principal.nivel = nivel_actual
    jugador_principal.rect.x = 380
    jugador_principal.rect.y = 140
    lista_sprites_activos.add(jugador_principal)
#Variable booleano que nos avisa cuando el usuario aprieta el boton salir.
    salir = False
    clock = pygame.time.Clock()
# -------- Loop Princiapl -----------
    while not salir:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                salir = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    jugador_principal.arriba()
                elif (evento.key == pygame.K_DOWN):
                    jugador_principal.abajo()
                elif evento.key == pygame.K_LEFT:
                    jugador_principal.izquierda()
                elif evento.key == pygame.K_RIGHT:
                    jugador_principal.derecha()
                elif evento.key == pygame.K_ESCAPE:
                    salir = True
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and jugador_principal.mover_x < 0:
                    jugador_principal.parar()
                elif evento.key == pygame.K_RIGHT and jugador_principal.mover_x > 0:
                    jugador_principal.parar()
                elif evento.key == pygame.K_UP and jugador_principal.mover_y < 0:
                    jugador_principal.parar()
                elif evento.key == pygame.K_DOWN and jugador_principal.mover_y > 0:
                    jugador_principal.parar()
            #elif evento.type==VIDEORESIZE:
                #pantalla=pygame.display.set_mode(evento.dict['size'],HWSURFACE|DOUBLEBUF|RESIZABLE)
                #fondo_escala = pygame.transform.scale(nivel_actual.fondo,evento.dict['size'])
                #nivel_actual.fondo = fondo_escala
                #pantalla.blit(fondo_escala,(0,0))
                #pygame.display.flip()
        
        # Actualiza todo el jugador
        lista_sprites_activos.update()
        
        
        
        
        
        # Actualiza los elementos del nivel
        nivel_actual.update()
        if (jugador_principal.llave and jugador_principal.puntos_por_nivel == len(jugador_principal.nivel.lista_puntos)):
            if (numero_del_nivel_actual < len(lista_niveles) - 1):
                numero_del_nivel_actual += 1
                nivel_actual = lista_niveles[numero_del_nivel_actual]
                jugador_principal.nivel = nivel_actual
                jugador_principal.llave = False
            if numero_del_nivel_actual == 1 : 
                jugador_principal.rect.x = 400
                jugador_principal.rect.y = 600
            if numero_del_nivel_actual == 2 :
                jugador_principal.rect.x = 620
                jugador_principal.rect.y = 400
            if numero_del_nivel_actual == 3 :
                jugador_principal.rect.x = 419
                jugador_principal.rect.y = 677
            if numero_del_nivel_actual == 4 :
                jugador_principal.rect.x = 710
                jugador_principal.rect.y = 400
            if numero_del_nivel_actual == 5 :
                jugador_principal.rect.x = 436
                jugador_principal.rect.y = 100
                
        print "Posicion x", jugador_principal.rect.x, "Posicion y", jugador_principal.rect.y
        
        
        
        
        
        
        
        
        
        
        # TODO EL CODIGO PARA DIBUJAR DEBE IR DEBAJO DE ESTE COMENTARIO.
        nivel_actual.draw(pantalla)
        lista_sprites_activos.draw(pantalla)
        
        textoPuntos = letraParaPuntos.render("" + str(jugador_principal.puntos), 1, constantes.NEGRO)
        pantalla.blit(puntosmarcador, (70, 810))
        pantalla.blit(textoPuntos, (110, 820))
        
        textoVidas = letraParaVidas.render("" + str(jugador_principal.vidas), 1, constantes.ROJO)
        pantalla.blit(vidasmarcador, (280, 810))
        pantalla.blit(textoVidas, (325, 820))
        
        
        tiempo_transcurrido = int(tiempo_comienzo - time())
        textotiempo =letraParaPuntos.render("" + str(tiempo_transcurrido), 1, constantes.NEGRO)
        pantalla.blit(relojmarcador, (160, 820))
        pantalla.blit(textotiempo, (210, 820))

        
        
        # TODO EL CODIGO PARA DIBUJAR DEBE IR POR ARRIBA DE ESTE COMENTARIO.
        if jugador_principal.vidas == 0:
            pantalla.fill(constantes.NEGRO)
            pantalla.blit(gameover, [0,0])
            pygame.display.flip()
            pygame.event.wait()
            salir = True
            menuPrincipal(pygame, constantes, pantalla)
        
        if tiempo_transcurrido == 0:
            pantalla.fill(constantes.NEGRO)
            pantalla.blit(gameovertime,[0,0] )
            pygame.display.flip()
            pygame.event.wait()
            salir = True
            menuPrincipal(pygame, constantes, pantalla)
        
        
        clock.tick(60)
        pygame.display.flip()
        
    #salgo del juego
    return True


def menuPrincipal(pygame, constantes, pantalla):
    #imagenes menuPrincipal
    fondomenu = pygame.image.load("imagenes/menuimagenes/fondomenu.png")
    logo = pygame.image.load("imagenes/logosurvivingnightmares.png")
    jugarb = pygame.image.load("imagenes/menuimagenes/jugar.png")
    historia = pygame.image.load("imagenes/menuimagenes/historiaboton.png")
    creditos = pygame.image.load("imagenes/menuimagenes/creditosboton.png")
    volver = pygame.image.load("imagenes/menuimagenes/volver.png")
    salirboton = pygame.image.load("imagenes/menuimagenes/salir.png")
    sprite_sheeeet = SpriteSheetnocolor("imagenes/menuimagenes/historia.png")
    historiaimagen = sprite_sheeeet.obtener_imagen(165,0,894,896)
    seleccionpj = pygame.image.load("imagenes/menuimagenes/seleccionpj.png")
    
    
    
    
    astrofrente = pygame.image.load("imagenes/astrofrente.png")
    sprite_sheet = SpriteSheet("imagenes/sun.png")
    sunfrente = sprite_sheet.obtener_imagen(81, 0, 81, 115)
    
    pantalla.blit(fondomenu,(0,0))
    
    menu_principal = cMenu(400, 510, 20, 20, "vertical", 4, pantalla, [("", 1, jugarb), ("", 2, creditos),("", 3, historia), ("", 8 , salirboton)])
    pantalla.blit(seleccionpj, (0,0))
    menuJugador = cMenu(215, 620, 105, 55, "horizontal", 3, pantalla, [("", 5, sunfrente),("", 7, volver), ("", 6, astrofrente)])
    menuHistoria = cMenu(450, 700, 20, 10, "vertical", 1, pantalla, [("", 7, volver)])
   
    
    estado = 0
    estado_previo = 1
    jugador = 1
    opcion = []
    salir = False
    while not salir:
        e = pygame.event.wait()
        if estado != estado_previo:
            pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key=0))
            estado_previo = estado

            if estado == 0:
                pantalla.fill(constantes.NEGRO)
                pantalla.blit(fondomenu,(0,0))
                pantalla.blit(logo, (215,5))
                pygame.display.flip()
            elif estado == 1:
                pantalla.blit(seleccionpj,(0,0))
                pantalla.blit(logo, (215,40))
                pygame.display.flip()
            elif estado == 2:
                pantalla.fill(constantes.NEGRO)
                letraParaMarcador = pygame.font.Font(None, 36)
                text = letraParaMarcador.render("work in progress...", 1, constantes.BLANCO)
                pantalla.blit(text, (100, 0))
                pygame.display.flip()
            elif estado == 3:
                pantalla.fill(constantes.NEGRO)
                pantalla.blit(historiaimagen,(0,0))
            elif estado == 7:
                estado = 0
                pygame.display.flip()
            elif estado == 8:
                salir = True
        
        
        if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
    #Menu inicial
            if estado == 0:
                opcion, estado = menu_principal.update(e, estado)
            elif estado == 1:
                opcion, estado = menuJugador.update(e, estado)
            elif estado == 2:
                opcion, estado = menuHistoria.update(e, estado)
            elif estado == 3:
                opcion, estado = menuHistoria.update(e, estado)
            elif estado == 5:
                jugar(pygame, constantes, pantalla, 1)
            elif estado == 6:
                jugar(pygame, constantes, pantalla, 2)
            elif estado == 7:
                estado = 0
                pygame.display.flip()
            elif estado == 8:
                salir = True
                
            #Opcion jugar
        if e.type == pygame.QUIT:
            salir = True
        pygame.display.flip()
        pygame.display.update(opcion)






def main():

    pygame.init()

    # Configuramos el alto y largo de la pantalla
    tamanio = [constantes.ANCHO_PANTALLA, constantes.LARGO_PANTALLA]
    pantalla = pygame.display.set_mode(tamanio,HWSURFACE|DOUBLEBUF|RESIZABLE)


    pygame.display.set_caption("Surviving Nightmares")
    sonido = pygame.mixer.Sound("sonidos/fondo-sonido.ogg")
    sonido.play()
    
    menuPrincipal(pygame, constantes, pantalla)

        
    pygame.quit()

if __name__ == "__main__":
    main()
