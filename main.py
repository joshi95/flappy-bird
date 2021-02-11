from entities.ground import Ground
from entities.bird import Bird
from entities.background import Background
import sys
from util.constants import Constants
from util.colors import Colors
import pygame


def run():
    pygame.init()
    screen = pygame.display.set_mode(Constants.game_dimention)
    
    background = Background()
    bird = Bird()
    ground = Ground()

    pygame.time.set_timer(pygame.USEREVENT, 200)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    bird.jump()
            if event.type == pygame.USEREVENT:
                bird.animate()
        
        bird.apply_gravity()
        background.display(screen)  
        bird.display(screen)
        ground.display(screen)
        pygame.display.flip()


if __name__ == '__main__':
    run()