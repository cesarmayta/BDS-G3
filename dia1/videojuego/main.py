import sys
import pygame

ANCHO = 640
ALTO = 480

color_fondo = (0,0,64)

### CLASES PARA LOS OBJETOS DEL JUEGO ###
class Bolita(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        #cargar la imagen
        self.image = pygame.image.load('imagenes/bolita.png')
        #obtener el rectangulo de la imagen
        self.rect = self.image.get_rect()
        # establecer la posición inicial de la bolita
        self.rect.centerx = ANCHO / 2
        self.rect.centery = ALTO / 2
        #establecer velocidad de la bolita
        self.speed = [3,3]
        
    def update(self):
        #evitamos que salga la bolita por debajo de la pantalla
        if self.rect.bottom >= ALTO or self.rect.top <= 0:
            self.speed[1] = -self.speed[1]
        elif self.rect.right >= ANCHO or self.rect.left <= 0:
            self.speed[0] = -self.speed[0]
                    
        self.rect.move_ip(self.speed)
      
#creamos un reloj
reloj = pygame.time.Clock()  
bolita = Bolita()
pantalla = pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("MI PRIMER VIDEOJUEGO")



while True:
    reloj.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sys.exit()
            
    #actualizamos la posición de la bolita
    bolita.update()
            
    #pintamos el fondo de la pantalla
    pantalla.fill(color_fondo)
    #dibujamos la bolita en la pantalla
    pantalla.blit(bolita.image,bolita.rect)
            
    pygame.display.flip()