import pygame
from playfield import Playfield


PLAYFIELD_SIZE = 7
DISPLAY_SIZE = 800
    
def main():
    display = pygame.display.set_mode((DISPLAY_SIZE, DISPLAY_SIZE))

    playfield = Playfield(PLAYFIELD_SIZE, DISPLAY_SIZE)

    pygame.init()

    

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        display.fill((173, 216, 230))
        playfield.all_sprites.draw(display)
        
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()    
