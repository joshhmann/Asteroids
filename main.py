import pygame
from constants import *

def main():
    pygame.init()
    pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    #start game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dt = pygame.tick(60)
            return
        screen.fill(BLACK)
        pygame.display.flip()
        
        
if __name__ == "__main__":
    
    main()
