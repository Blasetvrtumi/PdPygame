import pygame
import os

WIDTH = 1200
HEIGHT = 800
bg_color = (255,255,255)
text_color = (0,0,0)

def get_elements():
    '''Gets all the elements we need in the correct format.'''
    carpeta = './static/src'
    background = pygame.image.load(os.path.join(carpeta, 'libreta_abierta.jpeg')).convert()
    board = pygame.image.load(os.path.join(carpeta, 'nonograma_1.jpeg')).convert() #De 400px de ancho
    black_space = pygame.image.load(os.path.join(carpeta, 'black_space.png')).convert()
    big_font = pygame.font.Font('freesansbold.ttf', 42)
    text = big_font.render('Nonograma', True, text_color, )
    small_font = pygame.font.Font('freesansbold.ttf', 32)
    instructions_1 = small_font.render('Clica en el cuadrado que ', True, text_color,) 
    instructions_2 = small_font.render('quieras rellenar. ', True, text_color, )
    instructions_3 = small_font.render('Los numeros indican la ', True, text_color, )
    instructions_4 = small_font.render('cantidad de cuadrados ', True, text_color, )
    instructions_5 = small_font.render('a rellenar por fila.', True, text_color, )
    completed = 0
    return background, board, black_space, completed, text, instructions_1, instructions_2, instructions_3, instructions_4, instructions_5

def run():
    #Screen settings
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()   #Needed for fps

    #Get elements needed
    background, board, black_space, completed,text, instructions_1, instructions_2, instructions_3, instructions_4, instructions_5 = get_elements()
    

    #Show in screen before loop
    screen.blit(background,(0,0))
    screen.blit(board, (125,175))
    #screen.blit(black_space, (50,50))
    screen.blit(text, (700, 150))
    screen.blit(instructions_1, (650, 290))
    screen.blit(instructions_2, (650, 325))
    screen.blit(instructions_3, (650, 460))
    screen.blit(instructions_4, (650, 495))
    screen.blit(instructions_5, (650, 525))
    pygame.display.flip()

    #Game loop
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == '__main__':
    run()
