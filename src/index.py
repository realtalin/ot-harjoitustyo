import pygame
from playfield import Playfield


CELL_SIZE = 64
PLAYFIELD_SIZE = 12
    
def main():
    display_size = CELL_SIZE * PLAYFIELD_SIZE
    display = pygame.display.set_mode((display_size, display_size))

    playfield = Playfield(PLAYFIELD_SIZE, CELL_SIZE)

    pygame.init()

    playfield.cells.draw(display)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()    
