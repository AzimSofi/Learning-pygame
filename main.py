# 12:00 timestamp
# https://www.youtube.com/watch?v=jO6qQDNa2UY&ab_channel=TechWithTim

import pygame

WIDTH,HEIGHT = 800,600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# redrawing window, checking collision, update score など
def main():
    
    # Event loop
    run = True
    while run:
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT: # pygame.QUIT -> x button top-right
                run = False
    
    pygame.quit()

# Run main() if we run the file directly
# Not run when importing this file
if __name__ == "__main__":
    main()
