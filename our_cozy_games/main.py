import pygame
import sys  #To manage exit
import os   #To manage wd
import menu_maker
from messages import get_message, get_tittle

WIDTH = 1100
HEIGHT = 800

x, y = 350, 100 # Posición inicial del personaje
currentDir = 0
currentFrame = 0
frameDel = 100
lastUp = pygame.time.get_ticks()
speed = 5
COLS = 3
ROWS = 4

#Sound
pygame.mixer.init()
pygame.mixer.music.load("./static/src/mix/Hope.mp3")
pygame.mixer.music.play(-1)
stepsSound = pygame.mixer.Sound("./static/src/mix/Steps.mp3")

def prepare_char():
    global FRAME_WIDTH, FRAME_HEIGHT

    try:
        with open('selected_character.txt', 'r') as f:
            selected_character = f.read()
    except:
        selected_character = "brown_hair.png"

    print(selected_character)

    charTileset = pygame.image.load("./static/src/character/" + selected_character)

    FRAME_WIDTH = charTileset.get_width() // COLS
    FRAME_HEIGHT = charTileset.get_height() // ROWS

    charFrames = load_frames(charTileset, 4, 3, FRAME_WIDTH, FRAME_HEIGHT)
    return charFrames

def load_frames(tileset, rows, cols, FRAME_WIDTH, FRAME_HEIGHT):     
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


def set_rects_in_map():
    WALLWIDTH = 35
    walls = [(114, 128, WALLWIDTH, 576), (387, 303, WALLWIDTH, 110), (387, 492, WALLWIDTH, 214), (500, 8, WALLWIDTH, 210), (500, 303, WALLWIDTH, 110), (500, 490, WALLWIDTH, 214), (684, 303, WALLWIDTH, 400), (872, 8, WALLWIDTH, 318), (232, 8, 666, WALLWIDTH), (115, 303, 195, WALLWIDTH), (500, 303, 400, WALLWIDTH), (115, 666, 595, WALLWIDTH), (115, 85, 35, WALLWIDTH), (150, 50, 35, WALLWIDTH), (185, 20, 35, WALLWIDTH), (620, 100, 160, 140), (206, 396, 70, 215), (588, 422, 40, 190)]
    # left, top, width, length

    wallRects = []
    for left, top, width, length in walls:
        wallRect = pygame.Rect(left, top, width, length)
        wallRects.append(wallRect)

    games = [(206, 396, 70, 70),(206, 466, 70, 70), (620, 100, 60, 140)] #tictactoe, checkers and notebook

    games_rects = []
    for left, top, width, length in games:
        games_rect = pygame.Rect(left, top, width, length)
        games_rects.append(games_rect)

    notes = [(206, 576, 70, 30, "Cantidad de jugadores"),#No tocar estas tres
             (588, 500, 40, 40, "Huele de maravilla"),  #Luego se unen a los de
             (684, 500, 40, 40,"Que pena de vista"),    #los juegos por coordenadas
             (140, 40, 60, 60, "AUCHH"), #chimenea
             (140, 120, 60, 60, "AyAyayYy"), #botella_rota
             (140, 170, 50, 100, "El Principito – Capítulo 1"), #estantería 1
             (476, 38, 50, 100, get_tittle('name')),#estantería 2
              (535, 338, 400, 25, get_tittle('background'))] #botellas
    games_rects.append((206, 576, 70, 30)) #la botella de la mesa
    games_rects.append((588, 500, 40, 40))  #el desayuno
    games_rects.append((684, 500, 40, 40))  #la ventana
    counter = 0
    notes_rects = []
    all_rects = []
    for left, top, width, length, tittle in notes:
        note_rect = pygame.Rect(left, top, width, length)
        notes_rects.append({'id': counter, 'rect': note_rect, 'told': False, 'tittle': tittle, 'message': get_message(tittle)})
        all_rects.append(note_rect)#pygame.Rect(left, top, width, length)
        counter += 1

    bed_rect = pygame.Rect(276, 38, 100, 50) #Encontrar cama
    all_rects.append(bed_rect)

    return wallRects, games_rects, notes_rects, all_rects
wallRects, games_rects, notes_rects, all_rects = set_rects_in_map()

#Class that creates the main character
class Character:
    def __init__(self, images:list, cords, speed):
        self.speed = speed
        self.images = images
        self.image = images[3]
        self.cords = cords
        self.pos = images[3].get_rect().move(cords[0], cords[1])
        self.counter = 0
        self.lastUpdate = pygame.time.get_ticks()
        self.animDel = 200
        self.lastStep = pygame.time.get_ticks()
        self.stepDelay = 1200
    def change_image(self, direction):
        now = pygame.time.get_ticks()
        if now - self.lastUpdate > self.animDel:
            self.counter = ((self.counter + 1) % 3) + (direction * 3) # Cambiar entre 0, 1, 2
            self.lastUpdate = now
            self.image = self.images[self.counter]

    def move(self, dir):
        now = pygame.time.get_ticks()
        if now - self.lastStep > self.stepDelay:
            self.lastStep = now
            stepsSound.play()

        directionMap = {"up": 3, "down": 0, "left": 1, "right": 2}
        newPos = self.pos.copy()

        if checkCollision(newPos, all_rects):
            touched_special_object(newPos, all_rects, notes_rects)
        if dir == "up":
            if self.pos.top > 0 and not checkCollision(self.pos, wallRects,):
                newPos = self.pos.move(0, -self.speed)
            self.change_image(3)
        elif dir == "down":
            if self.pos.bottom < HEIGHT and not checkCollision(self.pos, wallRects):  # Asumiendo que la altura de la pantalla es 600
                newPos = self.pos.move(0, self.speed)
            self.change_image(0)
        elif dir == "left":
            if self.pos.left > 0 and not checkCollision(self.pos, wallRects):
                newPos = self.pos.move(-self.speed, 0)
            self.change_image(1)
        elif dir == "right":
            if self.pos.right < WIDTH and not checkCollision(self.pos, wallRects):  # Asumiendo que el ancho de la pantalla es 800
                newPos = self.pos.move(self.speed, 0)
            self.change_image(2)

        if not checkCollision(newPos, wallRects):
            self.pos = newPos
            self.change_image(directionMap[dir])
        elif checkCollision(newPos, games_rects):
            launch_game(newPos, games_rects, notes_rects, dir)              

def checkCollision(charRect, wallRects):

        for wallRect in wallRects:
            if charRect.colliderect(wallRect):
                return True
        return False

def forgot_notes():
    global notes_rects
    for note in notes_rects:
        note['told'] = False

def launch_game(charRect, game_rects, note_list, dir): 
        x,y,l,w = charRect
        if dir == "up":
            y += 5
        if dir == "down":
            y -= 5
        if dir == "left":
            x += 5
        if dir == "right":
            x -=5

        for i in range(3):
            note_dict = note_list[i]
            if charRect.colliderect(note_dict['rect']):
                menu_maker.story_page(note_dict['tittle'], note_dict['message'], (x,y), i)
                return True
        for i in range(len(game_rects)-2):
            if charRect.colliderect(game_rects[i]):
                forgot_notes()
                menu_maker.loading_page("Juego: ", i, (x,y))
                return True
        return False

def touched_special_object(charRect, simple, complex):
    x,y,l,w = charRect
    for i in range(len(simple)):
            if charRect.colliderect(simple[i]):
                if i == len(complex):
                    forgot_notes()
                    menu_maker.settings_page()
                else:
                    dict = complex[i]
                    if not dict['told']:
                        menu_maker.story_page(dict['tittle'], dict['message'], (x,y), i)
                

#Class that creates other objects
class Games:
    def __init__(self, image, cords, code):
        self.code = code
        self.image = image
        self.cords = cords
        self.pos = image.get_rect().move(cords[0], cords[1])    
    def go(self):
        match self.code:
            case 1: pass #Sitio para llamar a minijuegos
            
def run(char_cord = (350, 100), mensaje_leido = None):
    prepare_char()

    WIDTH = 1100
    HEIGHT = 800
    if mensaje_leido:
        global notes_rects
        notes_rects[mensaje_leido]['told'] = True

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
    notebook = pygame.image.load(os.path.join(carpeta, 'notebook.png')).convert_alpha()
    charFrames = prepare_char()


    #Arreglar desde aquí    
    screen.blit(background, (0, 0))
    pygame.display.flip()

    #See how to create player object 
    p = Character(charFrames, char_cord, 3)   #create the player object
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
            if event.type == pygame.KEYUP:
                stepsSound.stop()
            elif event.type == pygame.QUIT:
                sys.exit()
        screen.blit(p.image, p.pos)

        #Si varios ojetos -> Pasarlo a un jugador
        for o in objects:
            if isinstance(o, Character):
                o.move()
        pygame.display.update()
        clock.tick(60)

if __name__ == '__main__':
    run()
    pygame.quit()
