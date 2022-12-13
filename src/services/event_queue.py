import pygame


class EventQueue:
    """Class for the pygame event queue.
    """

    def get(self):
        """Gets a list of pygame events.

        Returns:
            A list of pygame events
        """
        return pygame.event.get()
