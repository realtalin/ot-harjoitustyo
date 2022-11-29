import pygame


class Renderer():
    def __init__(self, display, playfield, background_color: tuple):
        self._display = display
        self._playfield = playfield
        self._background_color = background_color

    def render(self):
        self._display.fill(self._background_color)
        self._playfield.all_sprites.draw(self._display)

        pygame.display.update()
