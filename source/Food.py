import random
import pygame


class Food:
    x = 200
    y = 200
    bsize = 20
    points = 0

    def __init__(self, resolution):
        self.x = random.randint(50, (resolution[0] - 50))
        self.y = random.randint(50, (resolution[1] - 50))
        self.bsize = 20
        self.points = 0
        self.rectFood = pygame.Rect(self.x, self.y, 20, 20)

    def draw(self, _display_surf):
        self.rectFood = pygame.Rect(self.x, self.y, 20, 20)
        pygame.draw.rect(_display_surf, (228, 38, 38), self.rectFood)