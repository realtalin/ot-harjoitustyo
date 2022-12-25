import pygame

from ui.menus import FailMenu, MainMenu


class Renderer():
    """Class for handling the rendering of the game

    Attributes:
        display: Pygame surface object
        game: The game to be rendered
        background_color (tuple): Tuple of 3 values representing an RGB value
    """

    def __init__(self, display, game, background_color: tuple):
        """Constructor for the class

        Args:
            display: Pygame surface object
            game: The game to be rendered
            background_color (tuple): Tuple of 3 values representing an RGB value
        """
        self._display = display
        self._game = game
        self._background_color = background_color

    def render(self):
        """Renders the background and level
        """
        self._display.fill(self._background_color)
        self.render_remaining_lives()
        self._game.level.all_sprites.draw(self._display)

        pygame.display.update()

    def render_remaining_lives(self):
        """Renders the remaining lives under the level grid
        """
        font = pygame.font.SysFont(None, 72)
        text = f"Elämiä: {self._game.lives}"
        text_image = font.render(text, True, (255, 255, 255))
        text_rect = text_image.get_rect()

        center_horizontal_position = self._display.get_width() / 2
        center_vertical_position = self._display.get_height() - text_rect.height
        text_rect.center = (center_horizontal_position,
                            center_vertical_position)

        self._display.blit(text_image, text_rect)

    def render_fail_menu(self, start_function, name_setter, username):
        """Renders the fail menu
        """

        main_menu = MainMenu(self._display, start_function,
                             name_setter, username)
        fail_menu = FailMenu(self._display, self._game.score, main_menu.render_main)
        fail_menu.render_fail()
