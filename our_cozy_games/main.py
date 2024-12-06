import pygame
import sys

screen = pygame.display.set_mode((640, 480)) #(horizontal, vertical)
clock = pygame.time.Clock()            #needed to set fps

#Take images from static/src
player = pygame.image.load('player.bmp').convert()  
background = pygame.image.load('background.bmp').convert()

screen.blit(background, (0, 0))

#See how to create player object
p = GameObject(player, 10, 3)          #create the player object
for x in range(10):                    #create 10 objects</i>
    o = GameObject(entity, x*40, x)
    objects.append(o)

#Bucle a customizar
while True:
    screen.blit(background, p.pos, p.pos)
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p.move(up=True)
    if keys[pygame.K_DOWN]:
        p.move(down=True)
    if keys[pygame.K_LEFT]:
        p.move(left=True)
    if keys[pygame.K_RIGHT]:
        p.move(right=True)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    screen.blit(p.image, p.pos)

    #Si varios ojetos -> Pasarlo a un jugador
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)
    pygame.display.update()
    clock.tick(60)