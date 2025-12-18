import pygame
from settings import GRID_SIZE

class Snake:
    def __init__(self, start_x, start_y):
        # self.positions — список блоков змейки, голова — первый элемент
        self.positions = [(start_x, start_y)]
        self.direction = (GRID_SIZE, 0)  # по умолчанию движение вправо

    def move(self):
        head_x, head_y = self.positions[0]
        dir_x, dir_y = self.direction
        new_head = (head_x + dir_x, head_y + dir_y)
        self.positions = [new_head] + self.positions[:-1]

    def change_direction(self, new_dir):
        # Можно добавить проверку, чтобы нельзя было задать направление противоположное текущему
        self.direction = new_dir

    def draw(self, surface):
        for pos in self.positions:
            rect = pygame.Rect(pos[0], pos[1], GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, (0, 255, 0), rect)