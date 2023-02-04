import pygame


class Player:
    def __init__(self, x, y, health,  sprite):
        self.health = health
        self.sprite = sprite
        self.x = x
        self.y = y

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= 3
        if keys[pygame.K_RIGHT]:
            self.x += 3

        if keys[pygame.K_UP]:
            self.y -= 3
        if keys[pygame.K_DOWN]:
            self.y += 3
