import pygame
from ui.menus import FailMenu


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
        self._game.level.all_sprites.draw(self._display)

        pygame.display.update()

    def render_fail_menu(self):
        """Renders the fail menu, menu.mainloop takes over rendering from Renderer
        """
        menu = FailMenu(self._display.get_width())
        menu.mainloop(self._display)
