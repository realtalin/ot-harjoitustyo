import pygame
from ui.menus import FailMenu


class Renderer():
    def __init__(self, display, game, background_color: tuple):
        self._display = display
        self._game = game
        self._background_color = background_color

    def render(self):
        self._display.fill(self._background_color)
        self._game.draw_level(self._display)

        pygame.display.update()

    def render_fail_menu(self):
        menu = FailMenu(self._display.get_width())
        menu.mainloop(self._display)
