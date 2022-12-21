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
        self.render_remaining_lives()
        self._game.level.all_sprites.draw(self._display)

        pygame.display.update()

    def render_remaining_lives(self):
        font = pygame.font.SysFont(None, 72)
        text = f"Elämiä: {self._game.get_lives()}"
        text_image = font.render(text, True, (255, 255, 255))
        text_rect = text_image.get_rect()

        center_horizontal_position = self._display.get_width() / 2
        center_vertical_position = self._display.get_height() - text_rect.height
        text_rect.center = (center_horizontal_position, center_vertical_position)
        
        self._display.blit(text_image, text_rect)

    def render_fail_menu(self):
        """Renders the fail menu, menu.mainloop takes over rendering from Renderer
        """
        menu = FailMenu(self._display.get_width(), self._display.get_height())
        menu.mainloop(self._display)
