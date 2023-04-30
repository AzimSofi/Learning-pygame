# 40:00 timestamp
# https://www.youtube.com/watch?v=jO6qQDNa2UY&ab_channel=TechWithTim

import pygame
import os # to import path

WIDTH,HEIGHT = 800,600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("初めて")

BORDER = pygame.Rect(WIDTH/2 -5, 0, 10, HEIGHT) # Draw rectangle

RAINBOW_INDIGO = (30, 63, 102)
WHITE = (255, 255, 255)
FPS  = 144
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40
YELLOW_ANGLE, RED_ANGLE = -90, 90
VELOCITY = 3

# Object to be drawn (surface)
YELLOW_SPACESHIP_IMAGE = pygame.image.load(
     os.path.join('Assets', 'spaceship_yellow.png'))
YELLOW_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(
     YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), YELLOW_ANGLE) # Rotate the resized spaceship

RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
RED_SPACESHIP_IMAGE = pygame.transform.rotate(pygame.transform.scale(
     RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH,SPACESHIP_HEIGHT)), RED_ANGLE) # Rotate the resized spaceship

def draw_window(red, yellow):
        # Draw background before surface
        WIN.fill(RAINBOW_INDIGO)
        pygame.draw.rect(WIN, WHITE, BORDER)

        # To draw surface
        WIN.blit(YELLOW_SPACESHIP_IMAGE, (yellow.x, yellow.y)) # Within dimenssion of Window's W,H
        WIN.blit(RED_SPACESHIP_IMAGE, (red.x, red.y)) # Within dimenssion of Window's W,H
        pygame.display.update() # update the "drawing"

def yellow_user_movement(keys_pressed, yellow):
        if keys_pressed[pygame.K_LEFT] and yellow.x - VELOCITY > 0: # 左
            yellow.x -= VELOCITY
        if keys_pressed[pygame.K_UP] and yellow.y - VELOCITY > 0: # 上
            yellow.y -= VELOCITY
        if keys_pressed[pygame.K_RIGHT] and yellow.x + yellow.width - 7 - VELOCITY < WIDTH: # 右
            yellow.x += VELOCITY
        if keys_pressed[pygame.K_DOWN] and yellow.y + yellow.height + 20 - VELOCITY < HEIGHT: # 下
            yellow.y += VELOCITY

def red_user_movement(keys_pressed, red):
        if keys_pressed[pygame.K_a] and red.x - VELOCITY > 0: # 左
            red.x -= VELOCITY
        if keys_pressed[pygame.K_w] and red.y - VELOCITY > 0: # 上
            red.y -= VELOCITY
        if keys_pressed[pygame.K_d] and red.x + red.width - 7 - VELOCITY < WIDTH: # 右
            red.x += VELOCITY
        if keys_pressed[pygame.K_s] and red.y + red.height + 20 - VELOCITY < HEIGHT: # 下
            red.y += VELOCITY

# redrawing window, checking collision, update score など
def main():
    red = pygame.Rect(50, 280, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) #(x, y,width, height)
    yellow = pygame.Rect(700, 280, SPACESHIP_WIDTH, SPACESHIP_HEIGHT) 

    clock = pygame.time.Clock()
    # Event loop
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            # quit
            if event.type == pygame.QUIT: # pygame.QUIT -> x button top-right
                run = False
        '''
        yellow.y += 1
        red.y += 1
        '''

        # user input to object's movement
        keys_pressed = pygame.key.get_pressed() # returns -> assigned pressed keys to `keys_pressed`
        yellow_user_movement(keys_pressed, yellow)
        red_user_movement(keys_pressed, red)
        
        # passing (red, yellow)'s position 
        # So that it can be updated
        draw_window(red, yellow)
    
    pygame.quit()

# Run main() if we run the file directly
# Not run when importing this file
if __name__ == "__main__":
    main()
