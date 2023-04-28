# 12:00 timestamp
# https://www.youtube.com/watch?v=jO6qQDNa2UY&ab_channel=TechWithTim

import pygame
import os # to import path

WIDTH,HEIGHT = 800,600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("初めて")

RAINBOW_INDIGO = (30, 63, 102)
FPS  = 144
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

# Object to be drawn (surface)
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
     os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(
     YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), 90) # Rotate the resized spaceship

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(
     RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), -90) # Rotate the resized spaceship

def draw_window():
        # Draw background before surface
        WIN.fill(RAINBOW_INDIGO)
        # To draw surface
        # D
        WIN.blit(YELLOW_SPACESHIP_IMAGE, (50,280)) # Within dimenssion of Window's W,H
        WIN.blit(RED_SPACESHIP_IMAGE, (700,280)) # Within dimenssion of Window's W,H
        pygame.display.update() # update the "drawing"

# redrawing window, checking collision, update score など
def main():
    clock = pygame.time.Clock()
    # Event loop
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT: # pygame.QUIT -> x button top-right
                run = False
        draw_window()
    
    pygame.quit()

# Run main() if we run the file directly
# Not run when importing this file
if __name__ == "__main__":
    main()
