import pygame


class GameLoop:
    def __init__(self, playfield, clock, event_queue, renderer):
        self._playfield = playfield
        self._clock = clock
        self._event_queue = event_queue
        self._renderer = renderer

    def start(self):
        while True:
            if self._handle_events() is False:
                break

            self._renderer.render()
            self._clock.run()

    def _handle_events(self):
        for event in self._event_queue.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:
                for cell in self._playfield.cells:
                    if cell.rect.collidepoint(pygame.mouse.get_pos()):
                        cell.click()
