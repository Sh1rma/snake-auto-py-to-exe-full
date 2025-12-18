import pygame
import sys
from settings import WIDTH, HEIGHT, GRID_SIZE
from snake import Snake
from food import Food

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Змейка')
font = pygame.font.SysFont(None, 36)

clock = pygame.time.Clock()

# Начальная позиция змейки — чуть ближе к центру
start_x = WIDTH // 2
start_y = HEIGHT // 2
snake = Snake(start_x=start_x, start_y=start_y)  # предполагается, что в классе есть параметры start_x, start_y
food = Food()

score = 0
game_over = False

def check_collision(snake):
    head_x, head_y = snake.positions[0]
    if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
        return True
    if (head_x, head_y) in snake.positions[1:]:
        return True
    return False

def show_game_over(screen, score):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(180)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))
    text1 = font.render("Конец игры", True, (255, 0, 0))
    text2 = font.render(f"Очки: {score}", True, (255, 255, 255))
    restart_text = font.render("Нажмите ПРОБЕЛ чтобы начать заново", True, (255, 255, 255))
    screen.blit(text1, (WIDTH//2 - text1.get_width()//2, HEIGHT//2 - 60))
    screen.blit(text2, (WIDTH//2 - text2.get_width()//2, HEIGHT//2))
    screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 60))
    pygame.display.flip()

def reset_game():
    global snake, food, score, game_over
    snake = Snake(start_x=start_x, start_y=start_y)
    food.spawn()
    score = 0
    game_over = False

while True:
    if not game_over:
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

        if check_collision(snake):
            game_over = True

        if snake.positions[0] == (food.x, food.y):
            score += 1
            snake.positions.append(snake.positions[-1])
            food.spawn()

        screen.fill((0, 0, 0))
        snake.draw(screen)
        food.draw(screen)

        score_text = font.render(f"Очки: {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()

        clock.tick(5)  # чуть медленнее, если хотите
    else:
        show_game_over(screen, score)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    reset_game()