from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
import main

update_loading = pygame.USEREVENT + 0
atras = False

def lanzar_carga():
    pygame.time.set_timer(update_loading, 30)

def lanzar_main():
    global atras
    atras = True
    pygame.time.set_timer(update_loading, 30)


def crear_carga_main(text = None):    
    atras = False
    loading = pygame_menu.Menu('Loading the Game...', 600, 400, theme=themes.THEME_DARK)
    loading.add.progress_bar("Progress", progressbar_id="1", default=0, width=200)
    if text:
        loading.add.label(text)
        loading.add.button("Entendido", lanzar_carga)
    loading.add.button("Atras", lanzar_main)
    return loading

def crear_carga_juego(text = None):    
    atras = False
    loading = pygame_menu.Menu('Loading the Game...', 600, 400, theme=themes.THEME_DARK)
    loading.add.progress_bar("Progress", progressbar_id="1", default=0, width=200)
    if text:
        loading.add.label(text)
        loading.add.button("Entendido", lanzar_main)
    loading.add.button("Jugar otra", lanzar_carga)
    return loading

def pagina_carga(text = None, programa = None, de_juego = False):   
    global atras
    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))
    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    if de_juego:
        loading = crear_carga_juego(text)
    else:
        loading = crear_carga_main(text)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == update_loading:
                progress = loading.get_widget("1")
                progress.set_value(progress.get_value() + 1)
                if progress.get_value() == 100:
                    pygame.time.set_timer(update_loading, 0)
                    print(atras)
                    if programa and not atras:
                        programa()
                    else:
                        main.run()  # Lanza rpg
            if event.type == pygame.QUIT:
                exit()

        if loading.is_enabled():
            loading.update(events)
            loading.draw(surface)
            if loading.get_current().get_selected_widget():
                arrow.draw(surface, loading.get_current().get_selected_widget())

        pygame.display.update()

if __name__ == '__main__':
    pagina_carga('Hola')
    