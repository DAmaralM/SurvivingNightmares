import pygame
import constantes
import platforma
import enemigos

from nivel import Level
from funciones_spritesheet import SpriteSheet
from puerta import PUERTA, Puerta
from puntos import Estrellas, ESTRELLA


class Habitacion_5(Level):
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
        imagen_1 = sprite_sheet_pantalla.obtener_imagen(0,894, 896,894)
        self.fondo = imagen_1
       
      
        self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_derecho = 740
        self.limite_izquierdo = 88
        self.limite_superior = -10
        self.limite_inferior = 686
        self.cambio_nivel_x = 396
        self.cambio_nivel_y = -16

        # Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel = [[platforma.STONE, 420, 360],
                 [platforma.STONE, 480, 360],
                 [platforma.STONE, 480, 420],
                 [platforma.STONE, 360, 360],
                 [platforma.STONE, 480, 480],
                 [platforma.STONE, 120, 360],
                 [platforma.STONE, 180, 360],
                 [platforma.STONE, 240, 360],
                 [platforma.STONE, 240, 300],
                 [platforma.STONE, 240, 240],
                 [platforma.STONE, 120, 720],
                 [platforma.STONE, 180, 720],
                 [platforma.STONE, 240, 720],
                 [platforma.STONE, 240, 660],
                 [platforma.STONE, 240, 600],]

        # Se busca en la lista anterior creada y se le agregan las plataformas al nivel.
        for plataforma in nivel:
            bloque = platforma.Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)
            
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 420
        puntos.rect.y = 420
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)     
 
 
            
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 170
        puntos.rect.y = 270
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)      
        
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 170
        puntos.rect.y = 630
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)         
 
        

                #puerta
        puerta = Puerta(PUERTA)
        puerta.rect.x = 450
        puerta.rect.y = 790
        
        self.puerta.add(puerta)

