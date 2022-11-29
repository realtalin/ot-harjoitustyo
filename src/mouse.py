import pygame


class Mouse:
    def get_pos(self):
        return pygame.mouse.get_pos()

    def get_pressed(self):
        return pygame.mouse.get_pressed()