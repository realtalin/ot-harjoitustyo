import pygame

from services.game.clock import Clock
from services.game.event_queue import EventQueue
from services.game.game import Game
from services.game.game_loop import GameLoop
from services.game.mouse import Mouse
from ui.menus import MainMenu
from ui.renderer import Renderer

DISPLAY_WIDTH = 720
DISPLAY_HEIGHT = 900
BACKGROUND_COLOR = 0, 183, 235


def main():
    display = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
    pygame.display.set_caption("Visuaalimuisti")

    game = Game(min(DISPLAY_WIDTH, DISPLAY_HEIGHT))
    clock = Clock()
    event_queue = EventQueue()
    mouse = Mouse()
    renderer = Renderer(display, game, BACKGROUND_COLOR)
    game_loop = GameLoop(game, clock, event_queue, mouse, renderer)

    pygame.init()
    menu = MainMenu(DISPLAY_WIDTH, DISPLAY_HEIGHT,
                    game_loop.start, game.set_username)
    menu.mainloop(display)


if __name__ == "__main__":
    main()
