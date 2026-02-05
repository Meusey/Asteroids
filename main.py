from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
import sys
import pygame
pygame.init()


def main():

    #object groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()



    #screen setup and starting messages
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(
        SCREEN_WIDTH / 2,
        SCREEN_HEIGHT / 2
    )

    print("Starting Asteroids with pygame version: 2.6.1")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    #clock and dt used to limit and optimize cpu use
    clock = pygame.time.Clock()
    dt = 0

    
    
    #infinite while loop to render the window and quit the window as needed
    while True:
        log_state()
        dt = clock.tick(60) / 1000

        updatable.update(dt)

        for a in asteroids:
            if a.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()



        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
#main call
if __name__ == "__main__":
    main()
