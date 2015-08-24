"""
Enemigos
"""
import pygame

from funciones_spritesheet import *
import jugador
from jugador import Jugador


class Enemigo(pygame.sprite.Sprite):

    izquierda = True
    jugador_frame_izq = []
    jugador_frame_der = []
    jugador_frame_up = []    
    jugador_frame_down = []
    
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("imagenes/slime.png")
            
        #Recorte Derecha
        imagen = sprite_sheet.obtener_imagen(0, 12, 84, 84)
        self.jugador_frame_der.append(imagen)
        imagen = sprite_sheet.obtener_imagen(102, 0, 92, 93)
        self.jugador_frame_der.append(imagen)

        #Recorte izquierda
        image = sprite_sheet.obtener_imagen(0, 12, 84, 84)
        self.jugador_frame_izq.append(image)
        image = sprite_sheet.obtener_imagen(102, 0, 92, 93)
        self.jugador_frame_izq.append(image)


        self.image = self.jugador_frame_der[0]
        self.rect = self.image.get_rect()



class MovingPlatform(Enemigo):
    """ This is a fancier platform that can actually move. """
    mover_x = 0
    mover_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    nivel = None
    player = None

    def update(self):
        """ Move the platform.
            If the jugador is in the way, it will shove the jugador
            out of the way. This does NOT handle what happens if a
            platform shoves a jugador into another object. Make sure
            moving platforms have clearance to push the jugador around
            or add code to handle what happens if they don't. """


        # Move left/right
        self.rect.x += self.mover_x

        pos = self.rect.x
        
        if not(self.izquierda):
            frame = (pos // 30) % len(self.jugador_frame_der)
            self.image = self.jugador_frame_der[frame]
            
        else:
            frame = (pos // 30) % len(self.jugador_frame_izq)
            self.image = self.jugador_frame_izq[frame]
            
        # Verficiamos si colisionamos con alguna plataforma
        lista_de_bloques_colisionados = pygame.sprite.spritecollide(self, self.nivel.lista_plataformas, False)
        for block in lista_de_bloques_colisionados:
            if self.mover_x > 0:
                self.rect.right = block.rect.left
            elif self.mover_x < 0:
                self.rect.left = block.rect.right
 
        self.rect.y += self.mover_y

        lista_de_bloques_colisionados = pygame.sprite.spritecollide(self, self.nivel.lista_plataformas, False)
        for block in lista_de_bloques_colisionados:
            if self.mover_y > 0:
                self.rect.bottom = block.rect.top
            elif self.mover_y < 0:
                self.rect.top = block.rect.bottom

            self.mover_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.mover_x
                
        cur_pos = self.rect.x - self.nivel.limite_derecho
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.mover_x *= -1
            self.izquierda = not (self.izquierda)
            




                
