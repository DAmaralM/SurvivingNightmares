import pygame

import constantes

from menu import cMenu, EVENT_CHANGE_STATE 


from habitacion1 import Habitacion_1
from habitacion2 import Habitacion_2
from habitacion3 import Habitacion_3
from habitacion4 import Habitacion_4
from habitacion5 import Habitacion_5

from jugador import Jugador
from time import time
import enemigos



def jugar(pygame, constantes, pantalla):
    
    
    tiempo_comienzo = time() + 5
    
    # Creamos al jugador con la imagen p1_walk.png
    jugador_principal = Jugador(1)
    letraParaPuntos = pygame.font.Font(None, 64)
    letraParaVidas = pygame.font.Font(None, 64)
    letraParaGameOver = pygame.font.Font(None, 45)
# Creamos todos los niveles del juego
    lista_niveles = []
    lista_niveles.append(Habitacion_1(jugador_principal))
    lista_niveles.append(Habitacion_2(jugador_principal))
    lista_niveles.append(Habitacion_3(jugador_principal))
    lista_niveles.append(Habitacion_4(jugador_principal))
    lista_niveles.append(Habitacion_5(jugador_principal))
# Seteamos cual es el primer nivel.
    numero_del_nivel_actual = 0
    nivel_actual = lista_niveles[numero_del_nivel_actual]
    lista_sprites_activos = pygame.sprite.Group()
    jugador_principal.nivel = nivel_actual
    jugador_principal.rect.x = 340
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
                if evento.key == pygame.K_LEFT:
                    jugador_principal.izquierda()
                elif evento.key == pygame.K_RIGHT:
                    jugador_principal.derecha()
                elif evento.key == pygame.K_UP:
                    jugador_principal.arriba()
                elif evento.key == pygame.K_DOWN:
                    jugador_principal.abajo()
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
        
        # Actualiza todo el jugador
        lista_sprites_activos.update()
        # Actualiza los elementos del nivel
        nivel_actual.update()
        if (jugador_principal.llave):
            if (numero_del_nivel_actual < len(lista_niveles) - 1):
                numero_del_nivel_actual += 1
                nivel_actual = lista_niveles[numero_del_nivel_actual]
                jugador_principal.nivel = nivel_actual
                jugador_principal.rect.x = 400
                jugador_principal.rect.y = 600
                jugador_principal.llave = False
        print "Posicion x", jugador_principal.rect.x, "Posicion y", jugador_principal.rect.y
        # TODO EL CODIGO PARA DIBUJAR DEBE IR DEBAJO DE ESTE COMENTARIO.
        nivel_actual.draw(pantalla)
        lista_sprites_activos.draw(pantalla)
        
        textoPuntos = letraParaPuntos.render("Puntos: " + str(jugador_principal.puntos), 1, constantes.BLANCO)
        pantalla.blit(textoPuntos, (10, 10))
        
        textoVidas = letraParaVidas.render("Vidas: " + str(jugador_principal.vidas), 1, constantes.BLANCO)
        pantalla.blit(textoVidas, (700, 10))
        
        tiempo_transcurrido = int(tiempo_comienzo - time())
        textoTiempo = letraParaPuntos.render("Tiempo: " + str(tiempo_transcurrido), 1, constantes.BLANCO)
        pantalla.blit(textoTiempo, (300, 10))
        
        
        # TODO EL CODIGO PARA DIBUJAR DEBE IR POR ARRIBA DE ESTE COMENTARIO.
        if jugador_principal.vidas == 0:
            pantalla.fill(constantes.NEGRO)
            texto_gameover1 = letraParaGameOver.render("PERDISTE GATOH", 1, constantes.ROJO)
            texto_gameover2 = letraParaGameOver.render("Presiona cualquier tecla para volver a jugar", 1, constantes.AZUL)
            pantalla.blit(texto_gameover1, [300, 250])
            pantalla.blit(texto_gameover2, [100, 310])
            pygame.display.flip()
            pygame.event.wait()
            salir = True
        
        if tiempo_transcurrido == 0:
            pantalla.fill(constantes.NEGRO)
            texto_gameover1 = letraParaGameOver.render("TE QUEDASTE SIN TIEMPO, PELOTUDO", 1, constantes.ROJO)
            texto_gameover2 = letraParaGameOver.render("Presiona cualquier tecla para volver a jugar", 1, constantes.ROJO)
            pantalla.blit(texto_gameover1, [150, 250])
            pantalla.blit(texto_gameover2, [125, 310])
            pygame.display.flip()
            pygame.event.wait()
            salir = True
        
        
        clock.tick(60)
        pygame.display.flip()
        
    #salgo del juego
    return True

def main():
    """ Clase principal en el que se debe ejecutar el juego. """
    pygame.init()

    # Configuramos el alto y largo de la pantalla
    tamanio = [constantes.ANCHO_PANTALLA, constantes.LARGO_PANTALLA]
    pantalla = pygame.display.set_mode(tamanio)

    pygame.display.set_caption("Lost stars")
    sonido = pygame.mixer.Sound("sonidos/fondo-sonido.ogg")
    sonido.play()
    
    menu_principal = cMenu(400,300,20,10,"vertical",3,pantalla,[("Jugar",1,None),("Creditos",2,None),("Salir",3,None)])

    estado = 0 
    estado_previo = 1
    opcion = []
    salir = False
    
    while (not salir): 
        e = pygame.event.wait()
        
        if estado != estado_previo:
            pygame.event.post(pygame.event.Event(EVENT_CHANGE_STATE, key = 0))
            estado_previo = estado
                       
        if e.type == pygame.KEYDOWN or e.type == EVENT_CHANGE_STATE:
            #Menu inicial
            if estado == 0:
                opcion, estado = menu_principal.update(e, estado)
            #Opcion jugar
            if estado == 1:
                salir = jugar(pygame, constantes, pantalla)
            if estado == 2:
                pantalla.fill(constantes.NEGRO)
                letraParaMarcador = pygame.font.Font(None, 36)
                text = letraParaMarcador.render("Creditos",1,constantes.BLANCO)
                pantalla.blit(text, (100,0))              
            if estado == 3:
                salir = True
            
        if e.type == pygame.QUIT:
            salir = True 

        pygame.display.flip()
        pygame.display.update(opcion)

        
    pygame.quit()

if __name__ == "__main__":
    main()
