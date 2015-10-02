import pygame

from funciones_spritesheet import *

# Estas contantes definen el tipo de plataforma.
#   Nombre del archivo.
#   Posicion X del sprite
#   Posicion Y del sprite
#   Ancho del sprite
#   Alto del sprite

PUERTA = (20, 0, 16, 10)


class Puerta(pygame.sprite.Sprite):
    """ Clase que define las caracteristicas de la puerta de los niveles. """

    def __init__(self, sprite_sheet_data):
        """ puerta constructor."""
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheetNegro("imagenes/puerta.png")
        # Grab the image for this platform
        self.image = sprite_sheet.obtener_imagen(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()

