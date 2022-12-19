import pygame

from services.game.game import Game
from services.game.game_loop import GameLoop
from services.game.clock import Clock
from ui.event_queue import EventQueue
from ui.menus import MainMenu
from ui.mouse import Mouse
from ui.renderer import Renderer

DISPLAY_SIZE = 800


def main():
    display = pygame.display.set_mode((DISPLAY_SIZE, DISPLAY_SIZE))
    pygame.display.set_caption("Visuaalimuisti")

    game = Game(DISPLAY_SIZE)
    clock = Clock()
    event_queue = EventQueue()
    mouse = Mouse()
    renderer = Renderer(display, game, (173, 216, 230))
    game_loop = GameLoop(game, clock, event_queue, mouse, renderer)

    pygame.init()
    menu = MainMenu(DISPLAY_SIZE, game_loop.start)
    menu.mainloop(display)


if __name__ == "__main__":
    main()
