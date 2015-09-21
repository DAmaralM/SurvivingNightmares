import pygame
import constantes
import platforma
from nivel import Level
from funciones_spritesheet import SpriteSheet
import enemigos
from puntos import Estrellas, ESTRELLA 
from puerta import PUERTA, Puerta


class Habitacion_1(Level):
    ''' Clase que define el primer nivel.
        Se debe definir el fondo, las plataformas y los enemigos que aparezcan. '''
    
    """ Definicion del nivel 1. """

    def __init__(self, jugador):
        """ Metodo que crea el nivel 1 """

        # Se llama al metodo del padre constructor.
        Level.__init__(self, jugador)

        #Cargamos la imagen de fondo.
        sprite_sheet_pantalla = SpriteSheet("imagenes/fondo.png")
        
        # Carga de todos los sprite de la imagen hacia la derecha.
        imagen_1 = sprite_sheet_pantalla.obtener_imagen(1788,1788, 896,894)
        self.fondo = imagen_1

        self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_derecho = 740
        self.limite_izquierdo = 88
        self.limite_superior = -10
        self.limite_inferior = 686
        self.cambio_nivel_x = 396
        self.cambio_nivel_y = -16


        # Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel = [ [platforma.STONE, 300, 300],
                  [platforma.STONE, 300, 600],
                  [platforma.STONE, 600, 300],
                  [platforma.STONE, 600, 600],
                 ]

       
        # Se busca en la lista anterior creada y se le agregan las plataformas al nivel.
        for plataforma in nivel:
            bloque = platforma.Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)
        
            
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 700
        puntos.rect.y = 200
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 700
        puntos.rect.y = 400
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)        
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 700
        puntos.rect.y = 600
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 160
        puntos.rect.y = 400
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 160 
        puntos.rect.y = 600
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        
        # Se agrega una plataforma en movimiento.
        bloque = platforma.PlataformaConMovimiento(platforma.STONE)
        bloque.rect.x = 1350
        bloque.rect.y = 280
        bloque.limite_izquierdo = 1350
        bloque.limite_derecho = 1600
        bloque.mover_x = 2
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)
        
        #enemigos
        ene = enemigos.MovingPlatform()
        ene.rect.x = 410
        ene.rect.y = 400
        ene.limite_izquierdo = -200
        ene.limite_derecho = 150
        ene.mover_x = 2
        ene.jugador = self.jugador
        ene.nivel = self
        self.lista_enemigos.add(ene)
        
                #puerta
        puerta = Puerta(PUERTA)
        puerta.rect.x = 450
        puerta.rect.y = 45
        self.puerta.add(puerta)