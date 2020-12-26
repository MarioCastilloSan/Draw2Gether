import pygame
#Variables para la ventana de pygame
width=500
height=500
window= pygame.display.set_mode((width,height))
pygame.display.set_caption("Cliente")

NumeroCliente=0

class Player():
    def __init__(self,x,y,width,height,color):
        self.x=x
        self.y=y
        self.width=width
        self.heigth=height
        self.color=color
        self.rect=(x,y,width,height)
        self.vel=3
    def draw(self,window):
        pygame.draw.rect(window,self.color,self.rect)
    def move(self):
        keys =pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= self.vel
        if keys[pygame.K_RIGHT]:
            self.x += self.vel
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel
        self.rect = (self.x, self.y, self.width, self.heigth)
#Funcion para redibujar la ventana
def FRedrawWindow(window,player):
    window.fill((255,255,255))
    player.draw(window)
    pygame.display.update()



#Loop principal que mantiene la ventana  en marcha
def FMainLOOP():
    run=True
    player = Player(50, 50, 100, 100, (0, 0, 255))
    tiempo = pygame.time.Clock()
    while  run:
        tiempo.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        player.move()
        FRedrawWindow(window,player)

FMainLOOP()