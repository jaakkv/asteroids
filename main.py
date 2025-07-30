#import pygame
#from constants import *
from player import Player
#from asteroid import Asteroid
from asteroidfield import *
from shots import Shot
import sys


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = asteroids, updatable, drawable
    Player.containers = updatable, drawable
    AsteroidField.containers = updatable
    Shot.containers = shots, drawable, updatable

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if player.check_for_collision(asteroid):
                print("Game over!")
                sys.exit(1)

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()

        #limit framrate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
