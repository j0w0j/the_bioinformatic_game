"""
This is the start of this amazing game
"""

import pygame
import pygame_gui

# import main game
import game

pygame.init()

pygame.display.set_caption("The Bio-Informatic")
# set screen
window_surface = pygame.display.set_mode((1000, 750))

background = pygame.Surface((1000, 1000))
background.fill(pygame.Color("#ffbfee"))
screen_width, screen_height = window_surface.get_size()
font = pygame.font.SysFont("Impact", 50)

manager = pygame_gui.UIManager((1000, 1000), "static/theme.json")

start_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((390, 350), (200, 50)),
    text="START GAME",
    manager=manager,
    # theme.json
    object_id="#button",
)
cry_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((390, 410), (200, 50)),
    text="CRY FOR HELP?",
    manager=manager,
    object_id="#button",
)
back_button = pygame_gui.elements.UIButton(
    relative_rect=pygame.Rect((10, 100), (200, 50)),
    text="BACK",
    manager=manager,
    object_id="#button",
)
back_button.hide()  # Initially hide the back button

clock = pygame.time.Clock()


def display_message(message, color, x, y):
    """
    This function renders the given message and displays it on the screen.
    :param message: The message to be displayed
    :param color: RGB color picker
    :param x: horizontal
    :param y: vertical
    """
    message_surface = font.render(message, True, color)
    window_surface.blit(message_surface, (x, y))


def display_img(img_img, img_size, img_horizontal, img_vertical):
    """
    :param img_img: the file of the image
    :param img_size: the size of the image
    :param img_horizontal: the horizontal position
    :param img_vertical: the vertical position
    """
    img_surface = pygame.image.load(img_img)
    img_surface = pygame.transform.scale(img_surface, img_size)
    img_surface_rect = img_surface.get_rect()
    img_y = (screen_height - img_surface_rect.height) // 2
    img_x = img_horizontal
    img_y += img_vertical
    img_surface_rect.topleft = [img_x, img_y]
    window_surface.blit(img_surface, img_surface_rect)


def gui():
    is_running = True
    show_krebs = False  # Initialize the variable
    while is_running:
        # used for frames
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
            if event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    print("START GAME")
                    game.rungame()
                elif event.ui_element == cry_button:
                    show_krebs = True
                    # show and hide is to manage the buttons, only wanna see the scary krebs cycle here...
                    start_button.hide()
                    cry_button.hide()
                    back_button.show()
                    print("Cry for help?")
                elif event.ui_element == back_button:
                    show_krebs = False
                    start_button.show()
                    cry_button.show()
                    back_button.hide()
                    print("BACK")

            manager.process_events(event)

        manager.update(time_delta)

        window_surface.blit(background, (0, 0))
        if show_krebs:
            display_img("static/images/krebs.png", (600, 600), 210, 20)
        else:
            manager.draw_ui(window_surface)
            display_message(
                "The Bio-Informatic (game edition)", (255, 255, 255), 250, 150
            )
            display_img("static/images/start.png", (200, 200), 50, -200)

        manager.draw_ui(window_surface)  # Ensure UI elements are drawn on top
        pygame.display.update()


if __name__ == "__main__":
    print("running game.py")
    gui()
    print("Run complete")
