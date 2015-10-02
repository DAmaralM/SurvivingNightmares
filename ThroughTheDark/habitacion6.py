import pygame
import constantes
import platforma
from nivel import Level
from funciones_spritesheet import SpriteSheet
from puntos import Estrellas, ESTRELLA


class Habitacion_6(Level):
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
        imagen_1 = sprite_sheet_pantalla.obtener_imagen(0,1788, 896,894)
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
        nivel = [ [platforma.STONE, 250, 740],
                  [platforma.STONE, 250, 680],
                  [platforma.STONE, 250, 620],
                  [platforma.STONE, 250, 560],
                  [platforma.STONE, 250, 500],
                  [platforma.STONE, 250, 440],
                  [platforma.STONE, 250, 380],
                  [platforma.STONE, 250, 320],
                  [platforma.STONE, 310, 320],
                  [platforma.STONE, 370, 320],
                  [platforma.STONE, 430, 320],
                  [platforma.STONE, 490, 320],
                  [platforma.STONE, 550, 320],
                  [platforma.STONE, 610, 320],
                  [platforma.STONE, 610, 380],
                  [platforma.STONE, 610, 440],
                  [platforma.STONE, 610, 500],
                  [platforma.STONE, 610, 560],
                  [platforma.STONE, 610, 620],]
        
        #puntos
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 150
        puntos.rect.y = 700
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)   
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 320
        puntos.rect.y = 390
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 366
        puntos.rect.y = 390
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 412
        puntos.rect.y = 390
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 458
        puntos.rect.y = 390
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 504
        puntos.rect.y = 390
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 560
        puntos.rect.y = 390
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 320
        puntos.rect.y = 467
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 366
        puntos.rect.y = 467
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 412
        puntos.rect.y = 467
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 458
        puntos.rect.y = 467
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 504
        puntos.rect.y = 467
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 560
        puntos.rect.y = 467
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 320
        puntos.rect.y = 544
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 366
        puntos.rect.y = 544
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 412
        puntos.rect.y = 544
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 458
        puntos.rect.y = 544
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 504
        puntos.rect.y = 544
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 560
        puntos.rect.y = 544
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 320
        puntos.rect.y = 621
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 366
        puntos.rect.y = 621
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 412
        puntos.rect.y = 621
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 458
        puntos.rect.y = 621
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 504
        puntos.rect.y = 621
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 560
        puntos.rect.y = 621
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        
        
        

        # Se busca en la lista anterior creada y se le agregan las plataformas al nivel.
        for plataforma in nivel:
            bloque = platforma.Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)

