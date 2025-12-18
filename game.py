import pygame
import sys
from settings import WIDTH, HEIGHT, GRID_SIZE
from snake import Snake
from food import Food

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Змейка')

clock = pygame.time.Clock()

snake = Snake()
food = Food()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction((0, -GRID_SIZE))
            elif event.key == pygame.K_DOWN:
                snake.change_direction((0, GRID_SIZE))
            elif event.key == pygame.K_LEFT:
                snake.change_direction((-GRID_SIZE, 0))
            elif event.key == pygame.K_RIGHT:
                snake.change_direction((GRID_SIZE, 0))

    snake.move()

    # Проверка попадания змейки на еду
    if snake.positions[0] == (food.x, food.y):
        # добавим новую часть змейки или переместим еду
        food.spawn()

    # рисуем
    screen.fill((0, 0, 0))
    snake.draw(screen)
    food.draw(screen)
    pygame.display.flip()

    clock.tick(10)