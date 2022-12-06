import pygame
from components.playfield import Playfield
from services.clock import Clock
from services.event_queue import EventQueue
from ui.renderer import Renderer
from game_loop import GameLoop
from ui.mouse import Mouse

PLAYFIELD_SIZE = 3
DISPLAY_SIZE = 800


def main():
    display = pygame.display.set_mode((DISPLAY_SIZE, DISPLAY_SIZE))
    pygame.display.set_caption(
        "Visuaalimuisti: paina SPACE aloittaaksesi uuden pelin")

    playfield = Playfield(PLAYFIELD_SIZE, DISPLAY_SIZE)
    clock = Clock()
    event_queue = EventQueue()
    mouse = Mouse()
    renderer = Renderer(display, playfield, (173, 216, 230))
    game_loop = GameLoop(playfield, clock, event_queue, mouse, renderer)

    pygame.init()
    game_loop.start()


if __name__ == "__main__":
    main()
