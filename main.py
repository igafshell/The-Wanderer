import pygame
import sys
from globalVariables import *
from playerClass import Player

pygame.init()

screen = pygame.display.set_mode((width, height))

map = pygame.image.load("sprites/Untitled.png")
map_rect = map.get_rect()

player_sprite = pygame.Surface((100, 100))
player = Player(100, 100, 100, player_sprite)


def screen_draw():
    screen.fill((0, 100, 100))
    screen.blit(map, (100, 100))

    player.move()
    player.sprite.fill((255, 0, 0))
    screen.blit(player.sprite, (player.x, player.y))


def main():
    running = True

    while running:
        pygame.time.Clock().tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        screen_draw()
        pygame.display.flip()


if __name__ == "__main__":
    main()
