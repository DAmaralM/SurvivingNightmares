import pygame
import constantes
import platforma
from nivel import Level
from funciones_spritesheet import SpriteSheet


class Habitacion_2(Level):
    ''' Clase que define el primer nivel.
        Se debe definir el fondo, las plataformas y los enemigos que aparezcan. '''
    
    """ Definicion del nivel 1. """

    def __init__(self, jugador):
        """ Metodo que crea el nivel 1 """

        # Se llama al metodo del padre constructor.
        Level.__init__(self, jugador)

        #Cargamos la imagen de fondo.
        sprite_sheet_pantalla = SpriteSheet("imagenes/fondoooo.png")
        
        # Carga de todos los sprite de la imagen hacia la derecha.
        imagen_2 = sprite_sheet_pantalla.obtener_imagen(1788,894, 896,894)
        self.fondo = imagen_2
        
        self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_derecho = 740
        self.limite_izquierdo = 88
        self.limite_superior = -20
        self.limite_inferior = 675
        self.cambio_nivel_x = 92
        self.cambio_nivel_y = 388

        
        self.fondo.set_colorkey(constantes.BLANCO)

        # Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel = [ #[platforma.GRASS_LEFT, , 500],
                 ]


        # Se busca en la lista anterior creada y se le agregan las plataformas al nivel.
        for plataforma in nivel:
            bloque = platforma.Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)

        # Se agrega una plataforma en movimiento.
        bloque = platforma.PlataformaConMovimiento(platforma.STONE)
        bloque.rect.x = 1350
        bloque.rect.y = 280
        bloque.limite_izquierdo = 1350
        bloque.limite_derecho = 1600
        bloque.mover_x = 1
        bloque.jugador = self.jugador
        bloque.nivel = self
        self.lista_plataformas.add(bloque)