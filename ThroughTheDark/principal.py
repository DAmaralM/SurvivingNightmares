import pygame

import constantes
from habitacion1 import Habitacion_1
from habitacion2 import Habitacion_2

from jugador import Jugador
import enemigos


def main():
    """ Clase principal en el que se debe ejecutar el juego. """
    pygame.init()

    # Configuramos el alto y largo de la pantalla
    tamanio = [constantes.ANCHO_PANTALLA, constantes.LARGO_PANTALLA]
    pantalla = pygame.display.set_mode(tamanio)

    pygame.display.set_caption("Lost stars")
    sonido = pygame.mixer.Sound("sonidos/fondo-sonido.ogg")
    sonido.play()
    

    # Creamos al jugador con la imagen p1_walk.png
    jugador_principal = Jugador(1)

    letraParaPuntos = pygame.font.Font(None,64)
    letraParaVidas = pygame.font.Font(None,64)
    
    # Creamos todos los niveles del juego
    lista_niveles = []
    lista_niveles.append(Habitacion_1(jugador_principal))
    lista_niveles.append(Habitacion_2(jugador_principal))
  

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
                if evento.key == pygame.K_RIGHT:
                    jugador_principal.derecha()
                if evento.key == pygame.K_UP:
                    jugador_principal.arriba()
                if evento.key == pygame.K_DOWN:
                    jugador_principal.abajo()

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT and jugador_principal.mover_x < 0:
                    jugador_principal.parar()
                if evento.key == pygame.K_RIGHT and jugador_principal.mover_x > 0:
                    jugador_principal.parar()
                if evento.key == pygame.K_UP and jugador_principal.mover_y < 0:
                    jugador_principal.parar()
                if evento.key == pygame.K_DOWN and jugador_principal.mover_y > 0:
                    jugador_principal.parar()
                    
    




        # Actualiza todo el jugador
        lista_sprites_activos.update()


        # Actualiza los elementos del nivel
        nivel_actual.update()

        #Si el jugador se mueve hacia el fin del nivel cambia el jugador al siguiente nivel.
        if ((jugador_principal.rect.x >= nivel_actual.cambio_nivel_x-2 or jugador_principal.rect.x >= nivel_actual.cambio_nivel_x-2)  and jugador_principal.rect.y == nivel_actual.cambio_nivel_y):
            jugador_principal.rect.x = 120
            if numero_del_nivel_actual < len(lista_niveles)-1:
                numero_del_nivel_actual += 1
                nivel_actual = lista_niveles[numero_del_nivel_actual]
                jugador_principal.nivel = nivel_actual
                jugador_principal.rect.x = 400
                jugador_principal.rect.y = 600


        print "Posicion x", jugador_principal.rect.x, "Posicion y", jugador_principal.rect.y

        # TODO EL CODIGO PARA DIBUJAR DEBE IR DEBAJO DE ESTE COMENTARIO.
        nivel_actual.draw(pantalla)
        lista_sprites_activos.draw(pantalla)
        
        textoPuntos = letraParaPuntos.render("Puntos: "+str(jugador_principal.puntos),1,constantes.BLANCO)
        pantalla.blit(textoPuntos,(10,10))
        textoVidas = letraParaVidas.render("Vidas: "+str(jugador_principal.vidas),1,constantes.BLANCO)
        pantalla.blit(textoVidas,(700,10))        
        
        # TODO EL CODIGO PARA DIBUJAR DEBE IR POR ARRIBA DE ESTE COMENTARIO.

        clock.tick(60)

        pygame.display.flip()
        
            
        

    pygame.quit()

if __name__ == "__main__":
    main()
