import pygame
import sys  #To manage exit
import os   #To manage wd

WIDTH = 1100
HEIGHT = 800

x, y = 350, 100 # Posición inicial del personaje
currentDir = 0
currentFrame = 0
frameDel = 100
lastUp = pygame.time.get_ticks()
speed = 5

try:
    with open('selected_character.txt', 'r') as f:
        selected_character = f.read()
except:
    selected_character = "brunette_tileset.png"

charTileset = pygame.image.load("./static/src/character/" + selected_character)
COLS = 3
ROWS = 4
FRAME_WIDTH = charTileset.get_width() // COLS
FRAME_HEIGHT = charTileset.get_height() // ROWS

def load_frames(tileset, rows, cols):
    frames = []
    for row in range(rows):
        for col in range(cols):

            frame = tileset.subsurface(pygame.Rect(
                col * FRAME_WIDTH,
                row * FRAME_HEIGHT,
                FRAME_WIDTH,
                FRAME_HEIGHT
            ))
            frames.append(frame)
    return frames


charFrames = load_frames(charTileset, 4, 3)

#Class that creates the main character
class Character:
    def __init__(self, images:list, cords, speed):
        self.speed = speed
        self.images = images
        self.image = images[3]
        self.cords = cords
        self.pos = images[3].get_rect().move(0, cords[1])
        print(self.pos)
        self.counter = 0
        self.lastUpdate = pygame.time.get_ticks()
        self.animDel = 200
    def change_image(self, direction):
        now = pygame.time.get_ticks()
        if now - self.lastUpdate > self.animDel:
            self.counter = ((self.counter + 1) % 3) + (direction * 3) # Cambiar entre 0, 1, 2
            self.lastUpdate = now
            self.image = self.images[self.counter]

    def move(self, dir):
        if dir == "up":
            if self.pos.top > 0:
                self.pos = self.pos.move(0, -self.speed)
            self.change_image(3)
        elif dir == "down":
            if self.pos.bottom < HEIGHT:  # Asumiendo que la altura de la pantalla es 600
                self.pos = self.pos.move(0, self.speed)
            self.change_image(0)
        elif dir == "left":
            if self.pos.left > 0:
                self.pos = self.pos.move(-self.speed, 0)
            self.change_image(1)
        elif dir == "right":
            if self.pos.right < WIDTH:  # Asumiendo que el ancho de la pantalla es 800
                self.pos = self.pos.move(self.speed, 0)
            self.change_image(2)

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
def run():
    WIDTH = 1100
    HEIGHT = 800

    pygame.init()

    screen = pygame.display.set_mode((WIDTH,HEIGHT)) #(horizontal, vertical)
    clock = pygame.time.Clock()            #needed to set fps

    #Take images from static/src
    carpeta = '../our_cozy_games/static/src/character'#For character
    carpeta = '../our_cozy_games/static/src'#Others
    try:
        with open('selected_background.txt', 'r') as f:
            selected_background = f.read()
    except:
        selected_background = 'background_2.jpg'

    background = pygame.image.load(os.path.join(carpeta, selected_background)).convert()
    WIDTH = background.get_width()
    HEIGHT = background.get_height()
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) #(horizontal, vertical)
    cheeckers = pygame.image.load(os.path.join(carpeta, 'cheeckers_1.png')).convert()
    tic_tac_toe = pygame.image.load(os.path.join(carpeta, 'tic_tac_toe_1.png')).convert()
    notebook = pygame.image.load(os.path.join(carpeta, 'notebook_1.png')).convert()


    #Arreglar desde aquí    
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #See how to create player object 
    p = Character(charFrames, (350, 100), 3)   #create the player object
    tictactoe = Games(tic_tac_toe, (215, 400), None) #Conectar con módulo
    checkers = Games(cheeckers, (215, 500), None) #Conectar con módulo
    notebook = Games(notebook, (640, 150), None) #Conectar con módulo
    objects = [tictactoe, checkers, notebook] #Nos servirá para regular el movimiento

    #Bucle a customizar 
    while True:
        screen.blit(background, p.pos, p.pos)
        for o in objects:
            screen.blit(o.image, o.cords)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            p.move("up")
        if keys[pygame.K_DOWN]:
            p.move("down")
        if keys[pygame.K_LEFT]:
            p.move("left")
        if keys[pygame.K_RIGHT]:
            p.move("right")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(p.image, p.pos)

        #Si varios ojetos -> Pasarlo a un jugador
        for o in objects:
            if isinstance(o, Character):
                o.move()
        #screen.blit(o.image, o.pos)
        pygame.display.update()
        clock.tick(60)

    # Mantener la ventana abierta hasta que se cierre
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == '__main__':
    run()
