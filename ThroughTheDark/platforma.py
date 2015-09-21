import pygame

from funciones_spritesheet import *

# Estas contantes definen el tipo de plataforma.
#   Nombre del archivo.
#   Posicion X del sprite
#   Posicion Y del sprite
#   Ancho del sprite
#   Alto del sprite

STONE            = (0, 0, 60, 60)


class Plataforma(pygame.sprite.Sprite):
    """ Clase que define las caracteristicas de la plataforma del juego. """

    def __init__(self, sprite_sheet_data):
        """ Plataforma constructor."""
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheetNegro("imagenes/piedra.png")
        # Grab the image for this platform
        self.image = sprite_sheet.obtener_imagen(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()


class PlataformaConMovimiento(Plataforma):
    """ Clase que define las caracteristicas de una plataforma con movimiento """
    mover_x = 0
    mover_y = 0

    limite_superior = 0
    limite_inferior = 0
    limite_izquierdo = 0
    limite_derecho = 0

    nivel = None
    jugador = None

    def update(self):
        """ Metodo que actualiza la posicion de la plataforma
            Si el jugador esta en el camino, mueve al jugador con la plataforma."""
           

        # Movimiento izquierda/derecha
        self.rect.x += self.mover_x

        # Se verifica si la plataforma colisiona con el jugador
        hit = pygame.sprite.collide_rect(self, self.jugador)
        if hit:
            # Si entramos es porque la plataforma colisiono con el jugador.

            # Si nos movemos hacia la derecha dejamos la plataforma a la derecha del jugador lo mismo si nos movemos a la izquierda
            if self.mover_x < 0:
                self.jugador.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.jugador.rect.left = self.rect.right

        # Movimiento sube/baja
        self.rect.y += self.mover_y

        # Verificamos si chocamos con el jugador.
        hit = pygame.sprite.collide_rect(self, self.jugador)
        if hit:
            # We did hit the jugador. Shove the jugador around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.mover_y < 0:
                self.jugador.rect.bottom = self.rect.top
            else:
                self.jugador.rect.top = self.rect.bottom

        # Verificamos los limietes definidos en la plataforma y vemos si tenemos que pegar la vuelta.

        if self.rect.bottom > self.limite_inferior or self.rect.top < self.limite_superior:
            self.mover_y *= -1

        cur_pos = self.rect.x - self.nivel.cambio_nivel_x
        if cur_pos < self.limite_izquierdo or cur_pos > self.limite_derecho:
            self.mover_x *= -1
