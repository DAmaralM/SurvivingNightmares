import pygame

import constantes

class Level():
    """ Super-Clase generica usada para definir los niveles del juego. 
        Se debe crear una clase hija para cada nivel."""

    # Lista de todos los sprites utilizados en todos los niveles.  
    lista_plataformas = None
    lista_enemigos = None
    lista_puntos = None 
    puerta = None 
    
    
    # Imagen de fondo
    fondo = None
    # Valor numerico de que tan lejos avanzo nuestro jugador en el nivel
    posicion_jugador_nivel = 0
    limite_derecho = -1000
    limite_inferior = 1000 
    limite_superior = 1000
    limite_izquierdo = -1000
    cambio_nivel_x = 0
    cambio_nivel_y = 0

    def __init__(self, jugador):
        """ Constructor. Se le debe pasar al jugador para saber sobre que nivel esta. """
        self.lista_plataformas = pygame.sprite.Group()
        self.lista_enemigos = pygame.sprite.Group()
        self.lista_puntos = pygame.sprite.Group()
        self.jugador = jugador
        self.puerta = pygame.sprite.Group()

    def update(self):
        """ Actualizar todo sobre el nivel """
        self.lista_plataformas.update()
        self.lista_enemigos.update()
        self.lista_puntos.update()
        self.puerta.update() 
    
    
    def draw(self, pantalla):
        """ Dibujamos todo sobre el nivel. """

        # Se debe dibujar el fondo.
        pantalla.fill(constantes.NEGRO)
        pantalla.blit(self.fondo,(self.posicion_jugador_nivel // 3,0))

        # Se dibujan todos los sprite que se cargaron.
        self.lista_plataformas.draw(pantalla)
        self.lista_enemigos.draw(pantalla)
        self.lista_puntos.draw(pantalla)
        self.puerta.draw(pantalla)
 

    def avance_nivel(self, avance_x):
        """ Cuando el usuario se mueve de izquierda/derecha se debe mover el nivel """

        self.posicion_jugador_nivel += avance_x

        for plataforma in self.lista_plataformas:
            plataforma.rect.x += avance_x

        for enemigo in self.lista_enemigos:
            enemigo.rect.x += avance_x

        for comidas in self.lista_puntos:
            comidas.rect.x += avance_x 