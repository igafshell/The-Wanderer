import pygame
import sys
from globalVariables import *

pygame.init()
screen = pygame.display.set_mode((width, height))


def main():
    running = True

    while running:
        pygame.time.Clock().tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        screen.fill((0, 100, 100))
        pygame.display.flip()


if __name__ == "__main__":
    main()
