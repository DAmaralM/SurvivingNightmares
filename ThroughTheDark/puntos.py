import pygame

from funciones_spritesheet import *

# Estas contantes definen el tipo de plataforma.
#   Nombre del archivo.
#   Posicion X del sprite
#   Posicion Y del sprite
#   Ancho del sprite
#   Alto del sprite

ESTRELLA          = (0, 0, 34, 32)

#Hoy hicimos los sonidos y los puntos

class Estrellas(pygame.sprite.Sprite):
    """ Clase que define las caracteristicas de la plataforma del juego. """

    def __init__(self, sprite_sheet_data):
        """ Plataforma constructor."""
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("imagenes/puntos.png")
        self.sonido_comida = pygame.mixer.Sound("sonidos/puntos.ogg")
        
        # Grab the image for this platform
        self.image = sprite_sheet.obtener_imagen(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()
    def hacer_sonido(self):
        self.sonido_comida.play()
        


