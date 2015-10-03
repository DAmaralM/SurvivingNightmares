import pygame
import constantes
import platforma
from nivel import Level
from funciones_spritesheet import SpriteSheet
from puerta import PUERTA, Puerta
from puntos import Estrellas, ESTRELLA
import enemigos

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
        

        # Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel = [
                 [platforma.STONE, 200, 200],
                 [platforma.STONE, 200, 320],
                 [platforma.STONE, 260, 260],
                 [platforma.STONE, 320, 320],
                 [platforma.STONE, 320, 200],
                 [platforma.STONE, 500, 200],
                 [platforma.STONE, 500, 320],
                 [platforma.STONE, 560, 260],
                 [platforma.STONE, 620, 320],
                 [platforma.STONE, 620, 200],  
                 [platforma.STONE, 200, 500],
                 [platforma.STONE, 200, 620],
                 [platforma.STONE, 260, 560],
                 [platforma.STONE, 320, 620],
                 [platforma.STONE, 320, 500],
                 [platforma.STONE, 500, 500],
                 [platforma.STONE, 500, 620],
                 [platforma.STONE, 560, 560],
                 [platforma.STONE, 620, 620],
                 [platforma.STONE, 620, 500], 
                                ]
        
        for plataforma in nivel:
            bloque = platforma.Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)
            
        #puntos
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 700
        puntos.rect.y = 700
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 120
        puntos.rect.y = 120
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)    
        
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 120
        puntos.rect.y = 700
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)        
        
                
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 700
        puntos.rect.y = 120
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)                


        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 420
        puntos.rect.y = 260
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)             


        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 420
        puntos.rect.y = 560
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)     
        
                #enemigos
        ene = enemigos.MovingPlatform()
        ene.rect.x = 500
        ene.rect.y = 400
        ene.limite_izquierdo = -280
        ene.limite_derecho = 280
        ene.mover_x = 2
        ene.jugador = self.jugador
        ene.nivel = self
        self.lista_enemigos.add(ene)                       
                
                
                
                #puerta
        puerta = Puerta(PUERTA)
        puerta.rect.x = 80
        puerta.rect.y = 440
        
        self.puerta.add(puerta)