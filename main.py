import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    astrofield = AsteroidField()
    #start game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        dt = clock.tick(60) / 1000
        screen.fill(BLACK)
        updatable.update(dt)
        
        for entity in drawable:
            entity.draw(screen)
            
        for asteroid in asteroids:
            for shot in shots:
                if shot.collision_detected(asteroid):
                    shot.kill()
                    new_asteroids = asteroid.split()
                    if new_asteroids:
                        asteroids.add(*new_asteroids)
            if player.collision_detected(asteroid):
                print("Game Over!")
                running = False
            
        pygame.display.flip()
        
        
if __name__ == "__main__":
    main()
