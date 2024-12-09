import pygame
import os   #To manage wd

WIDTH = 800
HEIGHT = 800
bg_color = (255,255,255)
text_color = (0,0,0)

class Piece:
    def __init__(self, image, cords):
        self.image = image
        self.cords = cords

    def mover(self, comible:bool):
        #Evento para notar teclas

        pass

def get_elements():
    '''Gets all the elements we need in the correct format.'''
    carpeta = './our_cozy_games/static/src'
    background = pygame.image.load(os.path.join(carpeta, 'big_cheeckers (1).png')).convert()
    white_piece = pygame.image.load(os.path.join(carpeta, 'cheeckers_white_piece.png')).convert()
    black_piece = pygame.image.load(os.path.join(carpeta, 'cheeckers_black_piece.png')).convert()
    return background, white_piece, black_piece

def clicked_piece(objects, pos, turn):
    for o in objects[0]:    #Las blancas
            (x1, y1) = o.cords
            if pos >= o.cords and pos <= (x1 + 45, y1 + 45):
                if turn == 0:
                    return o
                else:
                    return None
    for o in objects[1]:    #Las negras
            (x1, y1) = o.cords
            if pos >= o.cords and pos <= (x1 + 45, y1 + 45):
                if turn == 1:
                    return o
                else:
                    return None
    else:
        return None
    
def comible(piece, objects):
    '''for list in objects:
        for o in list:
            if o.cords == piece.ords: #+- diferencia'''
    pass
    
#Screen settings
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()   #Needed for fps

#Get elements needed
background, white_piece, black_piece = get_elements()
black_pieces = []
white_pieces = []
for i in range(4): #12 piezas
    white_pieces.append(Piece(white_piece, (50, i*175+50))) 
    black_pieces.append(Piece(black_piece, (495, i*175+137.5)))
for i in range(4): #12 piezas
    white_pieces.append(Piece(white_piece, (140, i*175+137.5))) 
    black_pieces.append(Piece(black_piece, (585, i*175+50)))
for i in range(4): #12 piezas
    white_pieces.append(Piece(white_piece, (230, i*175+50)))
    black_pieces.append(Piece(black_piece, (675, i*175+137.5)))
objects = [white_pieces, black_pieces]
turn = 0


# Mantener la ventana abierta hasta que se cierre
running = True
while running:
    screen.blit(background, (0,0))
    for l in objects:
        for o in l:
            screen.blit(o.image, o.cords)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos() 
            piece = clicked_piece(objects, pos, turn)
            if piece:
                piece.move(comible(piece, objects))
            #if game_finished():
                #pass



pygame.quit()
