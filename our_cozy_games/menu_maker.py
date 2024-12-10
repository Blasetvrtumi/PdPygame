from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
import main

update_loading = pygame.USEREVENT + 0

def lanzar_carga():
    pygame.time.set_timer(update_loading, 30)

def crear_carga(text = None):    
    loading = pygame_menu.Menu('Loading the Game...', 600, 400, theme=themes.THEME_DARK)
    loading.add.progress_bar("Progress", progressbar_id="1", default=0, width=200)
    if text:
        loading.add.label(text)
        loading.add.button("Entendido", lanzar_carga)
    return loading

def pagina_carga(text = None):   
    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))
    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    loading = crear_carga(text)

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

        if loading.is_enabled():
            loading.update(events)
            loading.draw(surface)
            if loading.get_current().get_selected_widget():
                arrow.draw(surface, loading.get_current().get_selected_widget())

        pygame.display.update()

if __name__ == '__main__':
    pagina_carga('Hola')
    