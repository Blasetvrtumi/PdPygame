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
    finished = pygame.image.load(os.path.join(carpeta, 'nonograma_1_completed.png')).convert()
    black_space = pygame.image.load(os.path.join(carpeta, 'black_space.png')).convert()
    big_font = pygame.font.Font('freesansbold.ttf', 42)
    text = big_font.render('Nonograma', True, text_color, )
    small_font = pygame.font.Font('freesansbold.ttf', 32)
    instructions_1 = small_font.render('Clica en el cuadrado que ', True, text_color,) 
    instructions_2 = small_font.render('quieras rellenar. ', True, text_color, )
    instructions_3 = small_font.render('Los numeros indican la ', True, text_color, )
    instructions_4 = small_font.render('cantidad de cuadrados ', True, text_color, )
    instructions_5 = small_font.render('a rellenar por fila.', True, text_color, )
    completed = False
    level = 0
    return background, board, finished, black_space, completed, level, text, instructions_1, instructions_2, instructions_3, instructions_4, instructions_5

def get_cords_with_x(x, y):
    if y < 348:
        return (x, 318)
    elif y < 378:
        return (x, 348)
    elif y < 408:
        return (x, 378)
    elif y < 438:
        return (x, 408) #378, 408, 438, 468, 498, 558, 588
    elif y < 468:
        return (x, 438)
    elif y < 498:
        return (x, 468)
    elif y < 528:
        return (x, 498)
    elif y < 558:
        return (x, 528)
    elif y < 588:
        return (x, 558)
    else:
        return (x, 588)

def get_cords_with_pos(x, y):
    if x < 247:
        return get_cords_with_x(217, y)
    elif x < 277:
        return get_cords_with_x(247, y)
    elif x < 307:
        return get_cords_with_x(277, y)
    elif x < 337:
        return get_cords_with_x(307, y)
    elif x < 367:
        return get_cords_with_x(337, y)
    elif x < 397:
        return get_cords_with_x(367, y)
    elif x < 427:
        return get_cords_with_x(397, y)
    elif x < 457:
        return get_cords_with_x(427, y)
    elif x < 487:
        return get_cords_with_x(457, y)
    else:
        return get_cords_with_x(487, y)



def pos_element(pos, level):
    #if level = 0 --> necesitamos más nonogramas para implementar esto
    (x,y) = pos
    if x<217 or y<318:  #Mide 30 cada cuadrado
        pass
    elif x>527 or y>628:
        pass
    else:
        return get_cords_with_pos(x, y)

def fin_del_juego(posiciones):
    print(posiciones)
    comparativa = posiciones == {(487, 438), (307, 318), (397, 468), (427, 438), (277, 588), (487, 468), (247, 468), (457, 558), (307, 348), (427, 468), (397, 318), (487, 498), (277, 438), (247, 318), (367, 588), (457, 588), (457, 408), (427, 498), (427, 318), (307, 558), (277, 468), (247, 348), (217, 408), (457, 438), (307, 588), (307, 408), (427, 528), (427, 348), (277, 318), (487, 558), (487, 378), (367, 468), (457, 468), (217, 438), (307, 438), (427, 558), (397, 588), (487, 588), (487, 408), (277, 348), (277, 528), (247, 408), (367, 318), (217, 468), (337, 588), (427, 588), (427, 408), (307, 468), (247, 438), (367, 348)}
    
    '''{(217, 408), (217, 438), (217, 468),
                          (247, 318), (247, 348), (247, 408), (247, 438), (247, 468), 
                          (277, 318), (277, 348), (277, 438), (277, 468), (277, 528), (277, 588),
                          (307, 318), (307, 348), (307, 438), (307, 468), (307, 558), (307, 588),
                          (337, 588),
                          (367, 318), (265, 348), (265, 468), (265, 588),
                          (397, 318), (397, 468), (397, 588),
                          (427, 318), (427, 348), (427, 408), (427, 438), (427, 468), (427, 498), (427, 528), (427, 558), (427, 588),
                          (457, 408), (457, 438), (457, 468), (457, 558), (457, 588),
                          (487, 378), (487, 408), (487, 438), (487, 468), (487, 498), (487, 558), (487, 588)}'''
    print(comparativa)
    return comparativa

def run():
    #Screen settings
    pygame.init()
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    clock = pygame.time.Clock()   #Needed for fps

    #Get elements needed
    background, board, finished, black_space, completed, level, text, instructions_1, instructions_2, instructions_3, instructions_4, instructions_5 = get_elements()
    pintado = []

    #Show in screen before loop
    screen.blit(background,(0,0))
    screen.blit(board, (125,175))
    screen.blit(text, (700, 150))
    screen.blit(instructions_1, (650, 290))
    screen.blit(instructions_2, (650, 325))
    screen.blit(instructions_3, (650, 460))
    screen.blit(instructions_4, (650, 495))
    screen.blit(instructions_5, (650, 525))
    pygame.display.flip() #botones cords x = 650, y = 460 - 525

    #Game loop
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP:
                if not completed:
                    pos = pygame.mouse.get_pos() 
                    cords = pos_element(pos, level)
                    print(cords)
                    if cords:
                        if cords not in pintado:
                            pintado.append(cords)
                        else:
                            pintado.remove(cords)
                
                        if not fin_del_juego(set(pintado)):
                            screen.blit(board, (125,175))
                            for ink in pintado:
                                screen.blit(black_space, ink)
                        else: 
                            print('Lo has hecho')
                            screen.blit(finished, (100,150))
                            completed = True
                        pygame.display.flip()
                    
                    #Manejar botones rehacer y atras


if __name__ == '__main__':
    run()
    pygame.quit()
