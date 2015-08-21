"""
Enemigos
"""
import pygame

from funciones_spritesheet import *
import jugador
from jugador import Player


class Enemigo(pygame.sprite.Sprite):


    jugador_frame_izq = []
    jugador_frame_der = []
    
    izquierda = True

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheetNotas("imagenes/astro.png")
            
        #Recorte
        image = sprite_sheet.get_image(0, 0, 49, 81)
        image = pygame.transform.flip(image, True, False)
        self.jugador_frame_der.append(image)
        image = sprite_sheet.get_image(48, 0, 49, 81)
        image = pygame.transform.flip(image, True, False)
        self.jugador_frame_der.append(image)
        image = sprite_sheet.get_image(98, 0, 49, 81)
        image = pygame.transform.flip(image, True, False)
        self.jugador_frame_der.append(image)
        image = sprite_sheet.get_image(149, 0, 49, 81)
        image = pygame.transform.flip(image, True, False)
        self.jugador_frame_der.append(image)
        image = sprite_sheet.get_image(199, 0, 49, 81)
        image = pygame.transform.flip(image, True, False)
        self.jugador_frame_der.append(image)
        
        #Rotacion 
        image = sprite_sheet.get_image(0, 0, 49, 81)

        self.jugador_frame_izq.append(image)
        image = sprite_sheet.get_image(49, 0, 49, 81)

        self.jugador_frame_izq.append(image)
        image = sprite_sheet.get_image(97, 0, 48, 81)

        self.jugador_frame_izq.append(image)
        image = sprite_sheet.get_image(149, 0, 49, 81)

        self.jugador_frame_izq.append(image)
        image = sprite_sheet.get_image(199, 0, 49, 81)


        
        self.image = self.jugador_frame_izq[0]
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

        self.calc_grav()

        #self.mover_x = -2

        # Move left/right
        self.rect.x += self.mover_x

        pos = self.rect.x

        if not(self.izquierda):
            frame = (pos // 30) % len(self.jugador_frame_der)
            self.image = self.jugador_frame_der[frame]
            
        else:
            frame = (pos // 30) % len(self.jugador_frame_izq)
            self.image = self.jugador_frame_izq[frame]

        #ACA ES CUANDO CHOCAMOS CON EL ENEMIGO. HACER LAS ACCIONES QUE SE QUIERAN.
        # Primera accion: Eliminar el enemigo
        # Segunda accion: Quitar puntos.
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            self.kill()
            self.player.vida -= 10


        # Verficiamos si colisionamos con alguna plataforma
        lista_de_bloques_colisionados = pygame.sprite.spritecollide(self, self.nivel.platform_list, False)
        for block in lista_de_bloques_colisionados:
            if self.mover_x > 0:
                self.rect.right = block.rect.left
            elif self.mover_x < 0:
                self.rect.left = block.rect.right
 
        self.rect.y += self.mover_y

        lista_de_bloques_colisionados = pygame.sprite.spritecollide(self, self.nivel.platform_list, False)
        for block in lista_de_bloques_colisionados:
            if self.mover_y > 0:
                self.rect.bottom = block.rect.top
            elif self.mover_y < 0:
                self.rect.top = block.rect.bottom

            self.mover_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.mover_x
                
        cur_pos = self.rect.x - self.nivel.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.mover_x *= -1
            self.izquierda = not (self.izquierda)
        
    def calc_grav(self):
        """ Calcula el efecto de la gravedad. """
        if self.mover_y == 0:
            self.mover_y = 2
        else:
            self.mover_y += .34

        # Verificamos si estamos en el suelo.
        if self.rect.y >= constantes.LARGO_PANTALLA - self.rect.height and self.mover_y >= 1:
            self.mover_y = 1
            self.rect.y = constantes.LARGO_PANTALLA - self.rect.height