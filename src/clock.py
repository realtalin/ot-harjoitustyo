import pygame


class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()

    def run(self):
        self._clock.tick(60)

    def get_time(self):
        return pygame.time.get_ticks()
