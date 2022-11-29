import pygame

class Renderer():
    def __init__(self, display, playfield, background_color):
        self._display = display
        self._playfield = playfield
        self._background_color = background_color

    def render(self):
        self._display.fill((173, 216, 230))
        self._playfield.all_sprites.draw(self._display)
        
        pygame.display.update()
