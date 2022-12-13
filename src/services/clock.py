import pygame


class Clock:
    """Class for the pygame clock

    Attributes:
        clock: Pygame clock object
    """

    def __init__(self):
        """Constructor for the clock
        """
        self._clock = pygame.time.Clock()

    def run(self):
        """Moves the clock forward, called every game loop
        """
        self._clock.tick(60)

    def get_time(self):
        """Method for the getting the current time

        Returns:
            Integer that represents the current time
        """
        return pygame.time.get_ticks()
