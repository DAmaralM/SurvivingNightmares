import pygame
import nivel
from funciones_spritesheet import SpriteSheet



class Jugador(pygame.sprite.Sprite):
    """Clase utilizada para desarrollar los jugadores del juego. """
    
    # -- Atributos
    mover_x = 0
    mover_y = 0

    # Estas listas definen todas las imagenes de nuestro jugador.
    jugador_frame_izq = []
    jugador_frame_der = []
    jugador_frame_up = []
    jugador_frame_down = []

    puntos_por_nivel = 0

    llave = False

    # Direccion en la que va el jugador.
    direccion = "R"

    # Lista de sprite con las cosas que nos podemos chocar.
    nivel = None
    vidas = 5
    puntos = 0
    # -- Metodos
    def __init__(self, jugador):
        """ __Funcion constructor__ 
            Aca en donde se debe cargar el sprite sheet del jugador.
            Se debe cargar los sprite con movimiento hacia la izquierda y hacia la derecha.
        """
        jugador_frame_izq = []
        jugador_frame_der = []
        jugador_frame_up = []
        jugador_frame_down = []
    
        pygame.sprite.Sprite.__init__(self)
        
        if jugador == 1:
            jugador_frame_izq = []
            jugador_frame_der = []
            jugador_frame_up = []
            jugador_frame_down = []
            
            sprite_sheet = SpriteSheet("imagenes/sun.png")
            imagen = sprite_sheet.obtener_imagen(271, 0, 77, 115)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(274, 138, 78, 114)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(274, 274, 85, 114)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(284, 399, 78, 113)
            self.jugador_frame_der.append(imagen)

            # # Carga de todos los sprite de la imagen hacia la izquierda.
            imagen = sprite_sheet.obtener_imagen(0, 0, 77, 115)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(0, 140, 70, 115)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(0, 273, 77, 115)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(0, 398, 77, 114)
            self.jugador_frame_izq.append(imagen)

            # Carga de todos los sprite de la imagen hacia la ARRIBA
            imagen = sprite_sheet.obtener_imagen(181, 0, 78, 115)
            self.jugador_frame_up.append(imagen)
            imagen = sprite_sheet.obtener_imagen(181, 136, 78, 115)
            self.jugador_frame_up.append(imagen)
            imagen = sprite_sheet.obtener_imagen(183, 268, 76, 115)
            self.jugador_frame_up.append(imagen)
        
            # Carga de todos los sprite de la imagen hacia la ABAJO
            imagen = sprite_sheet.obtener_imagen(81, 0, 81, 115)
            self.jugador_frame_down.append(imagen)
            imagen = sprite_sheet.obtener_imagen(81, 132, 76, 115)
            self.jugador_frame_down.append(imagen)
            imagen = sprite_sheet.obtener_imagen(83, 264, 76, 115)
            self.jugador_frame_down.append(imagen)
            

            
        elif jugador == 2:
            jugador_frame_izq = []
            jugador_frame_der = []
            jugador_frame_up = []
            jugador_frame_down = []
            sprite_sheet = SpriteSheet("imagenes/astro.png")
            imagen = sprite_sheet.obtener_imagen(0, 0, 74, 125)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(0, 145, 75, 130)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(0, 282, 74, 130)
            self.jugador_frame_der.append(imagen)
            imagen = sprite_sheet.obtener_imagen(0, 419, 73, 130)
            self.jugador_frame_der.append(imagen)

            # # Carga de todos los sprite de la imagen hacia la izquierda.
            imagen = sprite_sheet.obtener_imagen(329, 18, 72, 126)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(332, 146, 70, 126)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(331, 291, 70, 127)
            self.jugador_frame_izq.append(imagen)
            imagen = sprite_sheet.obtener_imagen(325, 424, 70, 128)
            self.jugador_frame_izq.append(imagen)

            # Carga de todos los sprite de la imagen hacia la ARRIBA
            imagen = sprite_sheet.obtener_imagen(213, 17, 77, 122)
            self.jugador_frame_up.append(imagen)
            imagen = sprite_sheet.obtener_imagen(209, 157, 76, 121)
            self.jugador_frame_up.append(imagen)
            imagen = sprite_sheet.obtener_imagen(210, 289, 76, 122)
            self.jugador_frame_up.append(imagen)
        
            # Carga de todos los sprite de la imagen hacia la ABAJO
            imagen = sprite_sheet.obtener_imagen(106, 11, 75, 122)
            self.jugador_frame_down.append(imagen)
            imagen = sprite_sheet.obtener_imagen(94, 154, 77, 122)
            self.jugador_frame_down.append(imagen)
            imagen = sprite_sheet.obtener_imagen(94, 284, 77, 123)
            self.jugador_frame_down.append(imagen)



        # Seteamos con que sprite comenzar
        """self.jugador_frame_izq.append(imagen)
        self.jugador_frame_up.append(imagen)
        self.jugador_frame_down.append(imagen)
        self.jugador_frame_izq1.append(imagen)
        self.jugador_frame_up1.append(imagen)
       self.jugador_frame_down1.append(imagen)"""
        
        self.imagen = self.jugador_frame_down[0]
        self.rect = self.imagen.get_rect()


    def update(self):
        """ Metodo que actualiza la posicion del jugador. """
        
        # Movimientos Izquierda/Derecha/ARRIBA/ABAJO
        
        if (self.rect.x + self.mover_x < self.nivel.limite_derecho) and (self.rect.x + self.mover_x > self.nivel.limite_izquierdo):
            self.rect.x += self.mover_x
        
        if (self.rect.y + self.mover_y > self.nivel.limite_superior) and (self.rect.y + self.mover_y < self.nivel.limite_inferior):
            self.rect.y += self.mover_y
        
        pos_x = self.rect.x
        pos_y = self.rect.y
        
        if self.direccion =="R":
            frame = (pos_x // 30) % len(self.jugador_frame_der)
            self.image = self.jugador_frame_der[frame]
        
        elif self.direccion == "L":
            frame = (pos_x // 30) % len(self.jugador_frame_izq)
            self.image = self.jugador_frame_izq[frame]
        
        elif self.direccion == "U":
            frame = (pos_y // 30) % len(self.jugador_frame_up)
            self.image = self.jugador_frame_up[frame]

        else: 
            frame = (pos_y // 30) % len(self.jugador_frame_down)
            self.image = self.jugador_frame_down[frame]

        # Verficiamos si colisionamos con algo mientras avanzamos
        lista_de_bloques_colisionados = pygame.sprite.spritecollide(self, self.nivel.lista_plataformas, False)
        
        for block in lista_de_bloques_colisionados:
             if self.mover_x > 0:
                 self.rect.right = block.rect.left
             elif self.mover_x < 0:
                 self.rect.left = block.rect.right
             elif (self.mover_y > 0):
                 self.rect.bottom = block.rect.top
             elif(self.mover_y < 0):
                 self.rect.top = block.rect.bottom

        lista_de_bloques_colisionados2 = pygame.sprite.spritecollide(self, self.nivel.lista_artefactos, False)
        
        for block in lista_de_bloques_colisionados2:
             if self.mover_x > 0:
                 self.rect.right = block.rect.left
             elif self.mover_x < 0:
                 self.rect.left = block.rect.right
             elif (self.mover_y > 0):
                 self.rect.bottom = block.rect.top
             elif(self.mover_y < 0):
                 self.rect.top = block.rect.bottom

        lista_puntos_a_obtener = pygame.sprite.spritecollide(self, self.nivel.lista_puntos, False)
        for una_comida in lista_puntos_a_obtener:
            una_comida.kill()
            self.puntos += 1
            una_comida.hacer_sonido()
            self.puntos_por_nivel += 1
         
        lista_enemigos_a_obtener = pygame.sprite.spritecollide(self, self.nivel.lista_enemigos, False)
        for un_enemigo in lista_enemigos_a_obtener:
            un_enemigo.kill()
            self.vidas -= 1
        
        puerta_para_cambiar_nivel = pygame.sprite.spritecollide(self, self.nivel.puerta, False)
        for a_puerta in puerta_para_cambiar_nivel:
            self.llave = True
            self.puntos_por_nivel = 0

    def izquierda(self):
        """ Se llama cuando movemos hacia la izq. """
        
        self.mover_x = -4
        self.direccion = "L"

    def derecha(self):
        """ Se llama cuando movemos hacia la der. """
        
        self.mover_x = 4
        self.direccion = "R"
        
    def arriba(self):
        """ se llama cuando movemos hacia arriba"""
        self.mover_y = -4
        self.direccion = "U"        

        
    def abajo(self):
        """ Se llama cuando movemos hacia abajo """
        
        self.mover_y = 4
        self.direccion = "D"

    def parar(self):
        """ Se llama cuando soltamos la tecla. """
        self.mover_x = 0
        self.mover_y = 0
