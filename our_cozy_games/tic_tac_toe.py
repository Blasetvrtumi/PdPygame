import pygame
import os   #To manage wd

WIDTH = 600
HEIGHT = 800
bg_color = (255,255,255)
text_color = (0,0,0)

def get_elements():
    '''Gets all the elements we need in the correct format.'''
    carpeta = './our_cozy_games/static/src'
    background = pygame.image.load(os.path.join(carpeta, 'folio.jpeg')).convert()
    board = pygame.image.load(os.path.join(carpeta, 'big_tic_tac_toe.jpeg')).convert()
    cross = pygame.image.load(os.path.join(carpeta, 'cross.png')).convert()
    circle = pygame.image.load(os.path.join(carpeta, 'circle.png')).convert()
    big_font = pygame.font.Font('freesansbold.ttf', 42)
    text = big_font.render('Turno de', True, text_color, bg_color)
    small_font = pygame.font.Font('freesansbold.ttf', 32)
    instructions_1 = small_font.render('Clica en el cuadrado donde', True, text_color, bg_color)
    instructions_2 = small_font.render(' quieras poner la ficha.', True, text_color, bg_color)
    return background, board, cross, circle, text, instructions_1, instructions_2, small_font

def pos_element(pos):
    (x,y) = pos
    if (x < 150) or (y < 250):
        pass
    elif (x > 460) or (y > 560):
        pass
    elif x < 250:
        if y < 360:
            cord = (150, 250)
        elif y < 460:
            cord = (150, 360)
        else:
            cord = (150, 460)
    elif x < 360:
        if y < 360:
            cord = (250, 250)
        elif y < 460:
            cord = (250, 360)
        else:
            cord = (250, 460)
    else:
        if y < 360:
            cord = (360, 250)
        elif y < 460:
            cord = (360, 360)
        else:
            cord = (360, 460) 
    return cord

def es_fin_de_partida(espacios):
    bool = False
    ganador = None
    #Lleno el tablero
    if len(espacios) == 9:
        bool = True
        ganador = 'nadie. Empate.'
    #Filas iguales
    elif (150, 250) in espacios and (150, 360)in espacios and (150, 460) in espacios:
        if espacios[(150, 250)] == espacios[(150, 360)] == espacios[(150, 460)]:
            bool = True
            ganador = espacios[(150, 250)]
    elif (250, 250) in espacios and (250, 360)in espacios and (250, 460) in espacios:
        if espacios[(250, 250)] == espacios[(250, 360)] == espacios[(250, 460)]:
            bool = True
            ganador = espacios[(250, 460)]
    elif (360, 250) in espacios and (360, 360)in espacios and (360, 460) in espacios:
        if espacios[(360, 250)] == espacios[(360, 360)] == espacios[(360, 460)]:
            bool = True
            ganador = espacios[(360, 460)]
    #Columnas iguales
    elif (150, 250) in espacios and (250, 250)in espacios and (360, 250) in espacios:
        if espacios[(150, 250)] == espacios[(250, 250)] == espacios[(360, 250)]:
            bool = True
            ganador = espacios[(150, 250)]
    elif (150, 360) in espacios and (250, 360)in espacios and (360, 360) in espacios:
        if espacios[(150, 360)] == espacios[(250, 360)] == espacios[(360, 360)]:
            bool = True
            ganador = espacios[(250, 360)]
    elif (150, 460) in espacios and (250, 460)in espacios and (360, 460) in espacios:
        if espacios[(150, 460)] == espacios[(250, 460)] == espacios[(360, 460)]:
            bool = True
            ganador = espacios[(360, 460)]
    #Diagonales iguales
    elif (150, 250) in espacios and (250, 360)in espacios and (360, 460) in espacios:
        if espacios[(150, 250)] == espacios[(250, 360)] == espacios[(360, 460)]:
            bool = True
            ganador = espacios[(150, 250)]
    elif (150, 460) in espacios and (250, 360)in espacios and (360, 250) in espacios:
        if espacios[(150, 460)] == espacios[(250, 360)] == espacios[(360, 250)]:
            bool = True
            ganador = espacios[(360, 250)]
    
    return bool, ganador

#Screen settings
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
clock = pygame.time.Clock()   #Needed for fps

#Get elements needed
background, board, cross, circle, text, instructions_1, instructions_2, small_font = get_elements()
espacios = {}
turn = 0

#Show in screen before loop
screen.blit(background,(0,0))
screen.blit(board, (150,150))
screen.blit(text, (150, 100))
screen.blit(instructions_1, (75, 600))
screen.blit(instructions_2, (75, 650))
screen.blit(circle, (350, 85))
pygame.display.flip()


#Game loop
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos() 
            cord = pos_element(pos)
            if cord not in espacios.keys():
                if turn == 0:
                    screen.blit(circle, cord)
                    screen.blit(cross, (357, 85))
                    espacios[cord] = "el circulo"
                    turn = 1
                elif turn == 1:
                    screen.blit(cross, cord)
                    screen.blit(circle, (350, 85))
                    turn = 0
                    espacios[cord] = "la cruz"
                
            else:
                text = small_font.render('Donde no hay fichas.', True, text_color, bg_color)
                screen.blit(text, (75, 700))
                
            pygame.display.flip()

            bool, ganador = es_fin_de_partida(espacios)
            if bool:
                text = small_font.render('Ha ganado ' + ganador, True, text_color, bg_color)
                screen.blit(text, (75, 700))
                pygame.display.flip()

               

pygame.quit()