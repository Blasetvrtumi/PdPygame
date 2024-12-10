import pygame
import pygame_menu
from pygame_menu import themes
import main

#pygame.init()
#surface = pygame.display.set_mode((600, 400))

def set_hair_color(value, ruta):
    print(value)
    with open('selected_character.txt', 'w') as f:
        f.write(ruta)        

def set_background(value, ruta):
    print(value)
    with open('selected_background.txt', 'w') as f:
        f.write(ruta) 

def start_the_game(mainmenu, loading):
    name = mainmenu.get_input_data()['name']
    with open('nombre_usuario.txt', 'w') as f:
        f.write(name)
    mainmenu._open(loading)
    pygame.time.set_timer(update_loading, 30)

def level_menu(mainmenu, level):
    mainmenu._open(level)

def create_main_menu(nombre, start_the_game, level_menu):
    mainmenu = pygame_menu.Menu('Bienvenido', 600, 400, theme=themes.THEME_SOLARIZED)
    mainmenu.add.text_input('Nombre: ', default=nombre, textinput_id='name')
    mainmenu.add.button('Jugar', start_the_game)
    mainmenu.add.button('Opciones', level_menu)
    mainmenu.add.button('Quitar', pygame_menu.events.EXIT)
    return mainmenu

def crear_menu_seleccion():
    level = pygame_menu.Menu('Select your preferences', 600, 400, theme=themes.THEME_BLUE)
    level.add.selector('Color de pelo :', [('Moreno', 'brunette_tileset.png'), ('Castaño', 'brown_hair.png')], onchange=set_hair_color)
    level.add.selector('Fondo :', [('Con botellas', 'background_2.jpg'), ('Sin botellas', 'background_1.jpg')], onchange=set_background)
    return level

def create_loading(text=None):    
    loading = pygame_menu.Menu('Loading the Game...', 600, 400, theme=themes.THEME_DARK)
    loading.add.progress_bar("Progress", progressbar_id="1", default=0, width=200)
    if text:
        loading.add.label(text)
    return loading

arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))
update_loading = pygame.USEREVENT + 0

def set_menu():
    pygame.init()
    surface = pygame.display.set_mode((600, 400))

    try:
        with open('nombre_usuario.txt', 'r') as f:
            nombre = f.read()
    except:
        nombre = 'username'

    mainmenu = create_main_menu(nombre, lambda: start_the_game(mainmenu, loading), lambda: level_menu(mainmenu, level))
    loading = create_loading()
    level = crear_menu_seleccion()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == update_loading:
                progress = loading.get_widget("1")
                progress.set_value(progress.get_value() + 1)
                if progress.get_value() == 100:
                    pygame.time.set_timer(update_loading, 0)
                    main.run()  # Llama a la función principal del módulo main
            if event.type == pygame.QUIT:
                exit()

        if mainmenu.is_enabled():
            mainmenu.update(events)
            mainmenu.draw(surface)
            if mainmenu.get_current().get_selected_widget():
                arrow.draw(surface, mainmenu.get_current().get_selected_widget())

        pygame.display.update()

if __name__ == "__main__":
    set_menu()