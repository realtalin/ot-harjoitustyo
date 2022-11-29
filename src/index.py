import pygame
from playfield import Playfield
from clock import Clock
from event_queue import EventQueue
from renderer import Renderer
from game_loop import GameLoop

PLAYFIELD_SIZE = 7
DISPLAY_SIZE = 800


def main():
    display = pygame.display.set_mode((DISPLAY_SIZE, DISPLAY_SIZE))
    pygame.display.set_caption("Visuaalimuisti")

    playfield = Playfield(PLAYFIELD_SIZE, DISPLAY_SIZE)
    clock = Clock()
    event_queue = EventQueue()
    renderer = Renderer(display, playfield, (173, 216, 230))
    game_loop = GameLoop(playfield, clock, event_queue, renderer)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
