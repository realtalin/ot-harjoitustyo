import pygame
from game.game import Game


class GameLoop:
    def __init__(self, game, clock, event_queue, mouse, renderer):
        self._game = game
        self._clock = clock
        self._event_queue = event_queue
        self._mouse = mouse
        self._renderer = renderer

    def start(self):

        self._game.reset(self._clock.get_time())

        while True:
            if self._handle_events() is False:
                break

            self._renderer.render()
            self._clock.run()

            self._game.update_state(self._clock.get_time())

    def _handle_events(self):

        for event in self._event_queue.get():
            time = self._clock.get_time()

            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.MOUSEBUTTONDOWN and self._mouse.get_pressed()[0]:
                self._game.click(self._mouse.get_pos(), time)

        return True
