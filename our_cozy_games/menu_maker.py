import pygame
import pygame_menu
from pygame_menu import themes
import main
from main_menu import set_menu
import textwrap
import tic_tac_toe

update_loading = pygame.USEREVENT + 0
atras = False

juegos = [{'nombre': "Tres en raya (2p)", 'programa': tic_tac_toe}]

def set_juegos(numero):
    if juegos[numero]:
        nombre = juegos[numero]['nombre']
        programa = juegos[numero]['programa']
        return nombre, programa.run
    else:
        error_page()
        return None, None

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
    loading.add.button("Ir a rpg", lanzar_main)
    return loading

def loading_page(text = None, programa = None, de_juego = False):   
    if isinstance(programa, (int, float)):
        nombre, juego = set_juegos(programa)
        print(juego)
        if not juego:
            error_page()
        else:
            programa = juego
            text = text + nombre

    global atras
    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))
    pygame.init()
    surface = pygame.display.set_mode((600, 400))

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
                    progress.set_value(0)

            if event.type == pygame.QUIT:
                exit()

        if loading.is_enabled():
            loading.update(events)
            loading.draw(surface)
            if loading.get_current().get_selected_widget():
                arrow.draw(surface, loading.get_current().get_selected_widget())

        pygame.display.update()

def settings_page():
    set_menu()
    
def create_error_page():
    loading = pygame_menu.Menu('Loading the Game...', 600, 400, theme=themes.THEME_DARK)
    loading.add.progress_bar("Progress", progressbar_id="1", default=0, width=200)
    loading.add.label("Aún no está operativo ese juego")
    loading.add.button("Volver", lanzar_main)
    return loading

def error_page():
    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))
    pygame.init()

    surface = pygame.display.set_mode((600, 400))
    loading = create_error_page()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == update_loading:
                progress = loading.get_widget("1")
                progress.set_value(progress.get_value() + 1)
                if progress.get_value() == 100:
                    pygame.time.set_timer(update_loading, 0)
                    print(atras)
                    main.run()  # Lanza rpg
            if event.type == pygame.QUIT:
                exit()

        if loading.is_enabled():
            loading.update(events)
            loading.draw(surface)
            if loading.get_current().get_selected_widget():
                arrow.draw(surface, loading.get_current().get_selected_widget())

        pygame.display.update()


def create_story_page(title, text):
    size = 35
    loading = pygame_menu.Menu(title, 600, 400, theme=themes.THEME_DEFAULT)
    texts = textwrap.wrap(text, width=size, break_long_words=False) 
    for line in texts:
        loading.add.label(line)
    return loading

def story_page(title, text):
    pygame.init()
    surface = pygame.display.set_mode((600, 400))
    arrow = pygame_menu.widgets.LeftArrowSelection(arrow_size=(10, 15))
    pygame.init()

    surface = pygame.display.set_mode((600, 400))
    story = create_story_page(title, text)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()

        if story.is_enabled():
            story.update(events)
            story.draw(surface)
            if story.get_current().get_selected_widget():
                arrow.draw(surface, story.get_current().get_selected_widget())

        pygame.display.update()

if __name__ == '__main__':
    #loading_page("Juego: Tres en raya (2p).", tic_tac_toe.run)
    loading_page("Juego: ", 0)
    #settings_page()
    #story_page("Dia 1 de muchos", "Ya he perdido la cuenta de la de días que llevo encerrado. Que llevo sin respirar aire fresco porque no hay aire fresco. Desde ese apocalipsis que hizo que la vegetación se apoderara del planeta, me es imposible saber qué pasa ahí fuera. Solo tengo un par de juegos que tenía guardados para entretenerme. A veces incluso finjo que soy otra persona y juego conmigo al tres en raya...")
    #error_page()