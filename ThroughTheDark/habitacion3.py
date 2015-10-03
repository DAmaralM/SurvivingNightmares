import pygame
import constantes
import platforma
from nivel import Level
from funciones_spritesheet import SpriteSheet
from puntos import Estrellas, ESTRELLA
import enemigos
from puerta import PUERTA, Puerta

class Habitacion_3(Level):
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
        imagen_1 = sprite_sheet_pantalla.obtener_imagen(896,896, 896,894)
        self.fondo = imagen_1
        
        self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_derecho = 740
        self.limite_izquierdo = 88
        self.limite_superior = -10
        self.limite_inferior = 690
        self.cambio_nivel_x = 396
        self.cambio_nivel_y = -16

        # Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel = [
                 [platforma.STONE,735 , 325],
                 [platforma.STONE,675 , 325],
                 [platforma.STONE,615 , 325],
                 [platforma.STONE,555 , 325],
                 [platforma.STONE,495 , 325],
                 [platforma.STONE,495 , 385],
                 [platforma.STONE,495 , 445],
                 [platforma.STONE,495 , 505],
                 [platforma.STONE,495 , 565],
                 [platforma.STONE,495 , 625],
                 
                 [platforma.STONE,90  , 325],
                 [platforma.STONE,150 , 325],
                 [platforma.STONE,210 , 325],
                 [platforma.STONE,270 , 325],
                 [platforma.STONE,330 , 325],
                 [platforma.STONE,330 , 385],
                 [platforma.STONE,330 , 445],
                 [platforma.STONE,330 , 505],
                 [platforma.STONE,330 , 565],
                 [platforma.STONE,330 , 625],

                 ]

        # Se busca en la lista anterior creada y se le agregan las plataformas al nivel.
        for plataforma in nivel:
            bloque = platforma.Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)
            
            
        #Puntos
        
        #Izquierda
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 100
        puntos.rect.y = 400
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)

        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 280
        puntos.rect.y = 400
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)

        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 195
        puntos.rect.y = 400
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 100
        puntos.rect.y = 500
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)

        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 280
        puntos.rect.y = 500
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)

        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 100
        puntos.rect.y = 600
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)

        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 280
        puntos.rect.y = 600
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        #Derecha
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 720
        puntos.rect.y = 420
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)

        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 580
        puntos.rect.y = 420
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 580
        puntos.rect.y = 520
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)

        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 580
        puntos.rect.y = 620
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        #Pasillo
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 740
        puntos.rect.y = 740
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 110
        puntos.rect.y = 740
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        #Arriba
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 110
        puntos.rect.y = 120
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 110
        puntos.rect.y = 250
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 740
        puntos.rect.y = 120
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 740
        puntos.rect.y = 250
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        
        
        
        
        
        
        
        
        
        # Se agrega una plataforma en movimiento.
        
                #enemigos
        ene = enemigos.MovingPlatform()
        ene.rect.x = 200
        ene.rect.y = 230
        ene.limite_izquierdo = -200
        ene.limite_derecho = 150
        ene.mover_x = 2
        ene.jugador = self.jugador
        ene.nivel = self
        self.lista_enemigos.add(ene)
        
        #enemigos
        ene = enemigos.MovingPlatform()
        ene.rect.x = 200
        ene.rect.y = 700
        ene.limite_izquierdo = -200
        ene.limite_derecho = 150
        ene.mover_x = 2
        ene.jugador = self.jugador
        ene.nivel = self
        self.lista_enemigos.add(ene)
        
        ene = enemigos.MovingPlatform()
        ene.rect.x = 200
        ene.rect.y = 700
        ene.limite_izquierdo = -200
        ene.limite_derecho = 150
        ene.mover_x = 2
        ene.jugador = self.jugador
        ene.nivel = self
        self.lista_enemigos.add(ene)
        
                        #puerta
        puerta = Puerta(PUERTA)
        puerta.rect.x = 450
        puerta.rect.y = 50
        self.puerta.add(puerta)
