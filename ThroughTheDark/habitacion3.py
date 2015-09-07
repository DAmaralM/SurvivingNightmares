import pygame
import constantes
import platforma
from nivel import Level
from funciones_spritesheet import SpriteSheet
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
        sprite_sheet_pantalla = SpriteSheet("imagenes/fondoooo.png")
        
        # Carga de todos los sprite de la imagen hacia la derecha.
        imagen_1 = sprite_sheet_pantalla.obtener_imagen(896,896, 896,894)
        self.fondo = imagen_1
        
        self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_derecho = 740
        self.limite_izquierdo = 88
        self.limite_superior = -20
        self.limite_inferior = 675
        self.cambio_nivel_x = 396
        self.cambio_nivel_y = -16

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
        
                #enemigos
        ene = enemigos.MovingPlatform()
        ene.rect.x = 200
        ene.rect.y = 200
        ene.limite_izquierdo = -200
        ene.limite_derecho = 150
        ene.mover_x = 2
        ene.jugador = self.jugador
        ene.nivel = self
        self.lista_enemigos.add(ene)
        
        #enemigos
        ene = enemigos.MovingPlatform()
        ene.rect.x = 200
        ene.rect.y = 600
        ene.limite_izquierdo = -200
        ene.limite_derecho = 150
        ene.mover_x = 2
        ene.jugador = self.jugador
        ene.nivel = self
        self.lista_enemigos.add(ene)
        
                        #puerta
        puerta = Puerta(PUERTA)
        puerta.rect.x = 404
        puerta.rect.y = -16
        self.puerta.add(puerta)
