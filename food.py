import pygame
import random
from settings import WIDTH, HEIGHT, GRID_SIZE

class Food:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.spawn()

    def spawn(self):
        self.x = random.randint(0, (WIDTH - GRID_SIZE) // GRID_SIZE) * GRID_SIZE
        self.y = random.randint(0, (HEIGHT - GRID_SIZE) // GRID_SIZE) * GRID_SIZE

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, GRID_SIZE, GRID_SIZE))