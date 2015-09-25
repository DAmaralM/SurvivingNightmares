import pygame
import constantes
import platforma
from nivel import Level
from funciones_spritesheet import SpriteSheet
from puerta import PUERTA, Puerta

class Habitacion_4(Level):
    ''' Clase que define el primer nivel.
        Se debe definir el fondo, las plataformas y los enemigos que aparezcan. '''
    
    """ Definicion del nivel 1. """

    def __init__(self, jugador):
        """ Metodo que crea el nivel 1 """

        # Se llama al metodo del padre constructor.
        Level.__init__(self, jugador)

        #Cargamos la imagen de fondo.
        sprite_sheet_pantalla = SpriteSheet("imagenes/fondoactualizado.png")
        
        # Carga de todos los sprite de la imagen hacia la derecha.
        imagen_1 = sprite_sheet_pantalla.obtener_imagen(896,0, 896,894)
        self.fondo = imagen_1
        
        self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_derecho = 740
        self.limite_izquierdo = 88
        self.limite_superior = -10
        self.limite_inferior = 686
        self.cambio_nivel_x = 396
        self.cambio_nivel_y = -16
        
        self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_nivel = -2500

        # Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel = [ #[platforma.GRASS_LEFT, , 500],
                 ]

                #puerta
        puerta = Puerta(PUERTA)
        puerta.rect.x = 412
        puerta.rect.y = 500
        
        self.puerta.add(puerta)