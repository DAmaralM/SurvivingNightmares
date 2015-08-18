import pygame

import constantes

class SpriteSheet(object):
    """ Clase utilizada para obtener las imagenes de la hoja de sprite.
        Contien funciones para convertir sprite de un sprite sheet y obtener imagenes individuales
     """
    # Este atributo hace referencia al sprite sheet.
    sprite_sheet = None

    def __init__(self, file_name):
        """ Constructor de la clase. Se debe pasar la ruta del la hoja del sprite """

        # Carga el sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()

    def obtener_imagen(self, x, y, width, height):
        """ Obtiene una sola imagen del spritesheet. 
            Se pasa la x,y como ubicacion de la sprite
            y el ancho y largo del sprite. """

        imagen = pygame.Surface([width, height]).convert()

        imagen.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Asumimos que tiene un fondo negro y lo queremos hacer transparente. 
        imagen.set_colorkey(constantes.BLANCO)

        return imagen
