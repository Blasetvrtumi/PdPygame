import pygame
import sys  #To manage exit
import os   #To manage wd

#Class that creates the main character
class Character:
    def __init__(self, images:dict, cords, speed):
        self.speed = speed
        self.images = images
        self.image = images['front'][2]
        self.cords = cords
        self.pos = images['front'][2].get_rect().move(0, cords[1])
        self.counter = 2
    def change_image(self, position):
        self.counter += 1
        if self.counter >= 4:
            self.counter = 0
        self.pos = self.images[position][self.counter].get_rect().move(0, self.height)
        self.image = self.images[position][self.counter]
    def move(self):
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right > 600:
            self.pos.left = 0

#Class that creates other objects
class Games:
    def __init__(self, image, cords, code):
        self.code = code
        self.image = image
        self.cords = cords
        self.pos = image.get_rect().move(0, cords[1])    
    def go(self):
        match self.code:
            case 1: pass #Sitio para llamar a minijuegos

pygame.init()

screen = pygame.display.set_mode((1100,800)) #(horizontal, vertical)
clock = pygame.time.Clock()            #needed to set fps

#Take images from static/src
carpeta = '.\our_cozy_games\static\src\character'#For character
player = {}
player['front'] = [
    pygame.image.load(os.path.join(carpeta, 'brunette_front_1.png')).convert(),
    pygame.image.load(os.path.join(carpeta, 'brunette_front_2.png')).convert(),
    pygame.image.load(os.path.join(carpeta, 'brunette_front_3.png')).convert()]
player['left'] = [
    pygame.image.load(os.path.join(carpeta, 'brunette_left_1.png')).convert(), 
    pygame.image.load(os.path.join(carpeta, 'brunette_left_2.png')).convert(), 
    pygame.image.load(os.path.join(carpeta, 'brunette_left_3.png')).convert()]
player['right'] = [
    pygame.image.load(os.path.join(carpeta, 'brunette_right_1.png')).convert(),
    pygame.image.load(os.path.join(carpeta, 'brunette_right_2.png')).convert(),
    pygame.image.load(os.path.join(carpeta, 'brunette_right_3.png')).convert()]
player['back'] = [
    pygame.image.load(os.path.join(carpeta, 'brunette_back_1.png')).convert(),
    pygame.image.load(os.path.join(carpeta, 'brunette_back_2.png')).convert(),
    pygame.image.load(os.path.join(carpeta, 'brunette_back_3.png')).convert()]
carpeta = '.\our_cozy_games\static\src'#Others
background = pygame.image.load(os.path.join(carpeta, 'background_2.jpg')).convert()
cheeckers = pygame.image.load(os.path.join(carpeta, 'cheeckers_1.png')).convert()
tic_tac_toe = pygame.image.load(os.path.join(carpeta, 'tic_tac_toe_1.png')).convert()
notebook = pygame.image.load(os.path.join(carpeta, 'notebook_1.png')).convert()


#Arreglar desde aquí    
screen.blit(background, (20, 0))
pygame.display.flip()

#See how to create player object 
p = Character(player, (350, 100), 3)   #create the player object
tictactoe = Games(tic_tac_toe, (225, 400), None) #Conectar con módulo
checkers = Games(cheeckers, (225, 500), None) #Conectar con módulo
notebook = Games(notebook, (650, 150), None) #Conectar con módulo
objects = [tictactoe.cords, checkers.cords, notebook.cords] #Nos servirá para regular el movimiento

screen.blit(p.image, p.cords)
screen.blit(tictactoe.image, tictactoe.cords)
screen.blit(checkers.image, checkers.cords)
screen.blit(notebook.image, notebook.cords)
pygame.display.flip()

"""#Bucle a customizar 
while True:
    screen.blit(background, p.pos, p.pos)
    for o in objects:
        screen.blit(o.image, o.pos)
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
    clock.tick(60)"""

# Mantener la ventana abierta hasta que se cierre
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
