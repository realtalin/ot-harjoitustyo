import pygame
from components.game import Game
from services.clock import Clock
from services.event_queue import EventQueue
from ui.renderer import Renderer
from game_loop import GameLoop
from ui.mouse import Mouse
from ui.menu import MyMenu


DISPLAY_SIZE = 800


def main():
    display = pygame.display.set_mode((DISPLAY_SIZE, DISPLAY_SIZE))
    pygame.display.set_caption(
        "Visuaalimuisti")

    game = Game(DISPLAY_SIZE)
    clock = Clock()
    event_queue = EventQueue()
    mouse = Mouse()
    renderer = Renderer(display, game, (173, 216, 230))
    game_loop = GameLoop(game, clock, event_queue, mouse, renderer)

    pygame.init()
    menu = MyMenu(DISPLAY_SIZE, game_loop.start)
    menu.mainloop(display)


if __name__ == "__main__":
    main()
