import pygame
import constantes
import platforma
import artefactos
import enemigos
from nivel import Level
from funciones_spritesheet import SpriteSheet
from puntos import Estrellas, ESTRELLA
from puerta import PUERTA, Puerta


class Habitacion_2(Level):
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
        imagen_2 = sprite_sheet_pantalla.obtener_imagen(1788,894, 896,894)
        self.fondo = imagen_2
        
        self.fondo.set_colorkey(constantes.BLANCO)
        self.limite_derecho = 740
        self.limite_izquierdo = 88
        self.limite_superior = -10
        self.limite_inferior = 686
        self.cambio_nivel_x = 92
        self.cambio_nivel_y = 388

        
        self.fondo.set_colorkey(constantes.BLANCO)

        # Lista con los bloques de plataformas, indicando la ubicacion x,y y el tipo 
        nivel = [ [platforma.STONE, 200 ,500],
                  [platforma.STONE, 250, 450 ],
                  [platforma.STONE, 300, 400 ],
                  [platforma.STONE, 350, 350 ],
                  [platforma.STONE, 400, 300 ],
                  [platforma.STONE, 450, 300 ],
                  [platforma.STONE, 500, 350 ],
                  [platforma.STONE, 550, 400 ],
                  [platforma.STONE, 600, 450 ],
                  [platforma.STONE, 650, 500 ],
                  [platforma.STONE, 150, 550 ],
                  [platforma.STONE, 100, 600 ]]                  


        # Se busca en la lista anterior creada y se le agregan las plataformas al nivel.
        for plataforma in nivel:
            bloque = platforma.Plataforma(plataforma[0])
            bloque.rect.x = plataforma[1]
            bloque.rect.y = plataforma[2]
            bloque.jugador = self.jugador
            self.lista_plataformas.add(bloque)
            
            
            
        nivel_artefacto = [ [artefactos.ESCALERA, 656, 97]
                 
                 ]

       

        for artefactos1 in nivel_artefacto:
            bloque_a = artefactos.Artefactos(artefactos1[0])
            bloque_a.rect.x = artefactos1[1]
            bloque_a.rect.y = artefactos1[2]
            bloque_a.jugador = self.jugador
            self.lista_artefactos.add(bloque_a)            
            
            
            
        #Puntos
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 100
        puntos.rect.y = 103
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
            

        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 200
        puntos.rect.y = 103
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        

        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 300
        puntos.rect.y = 103
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        

        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 400
        puntos.rect.y = 103
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        


        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 500
        puntos.rect.y = 103
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        

        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 600
        puntos.rect.y = 103
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        """
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 650
        puntos.rect.y = 153
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 700
        puntos.rect.y = 103
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 750
        puntos.rect.y = 153
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        """
        
        #Puntos de abajo
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 100
        puntos.rect.y = 720 
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 430
        puntos.rect.y = 380
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        puntos = Estrellas(ESTRELLA)
        puntos.rect.x = 750
        puntos.rect.y = 720
        puntos.limite_izquierdo = 1350
        puntos.limite_derecho = 1600
        puntos.mover_x = 1
        puntos.jugador = self.jugador
        puntos.nivel = self
        self.lista_puntos.add(puntos)
        
        #Enemigos
        ene = enemigos.MovingPlatform()
        ene.rect.x = 300
        ene.rect.y = 200
        ene.limite_izquierdo = -3
        ene.limite_derecho = 500
        ene.mover_x = 2
        ene.jugador = self.jugador
        ene.nivel = self
        self.lista_enemigos.add(ene)
        
        
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
        
                #puerta
        puerta = Puerta(PUERTA)
        puerta.rect.x = 80
        puerta.rect.y = 436
        self.puerta.add(puerta)