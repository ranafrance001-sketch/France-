import pygame
import random
import math
import sys

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Animated Snake Game")
clock = pygame.time.Clock()

BG_COLOR = (15, 23, 42)
GRID_COLOR = (30, 41, 59)
SNAKE_HEAD = (34, 197, 94)
SNAKE_BODY = (74, 222, 128)
FOOD_COLOR = (244, 63, 94)
FOOD_GLOW = (251, 113, 133)
TEXT_COLOR = (241, 245, 249)

snake = [[10, 10], [9, 10], [8, 10]]
direction = [1, 0]
next_direction = [1, 0]
score = 0
food = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]
food_pulse = 0
move_timer = 0
move_delay = 100
game_over = False

font = pygame.font.SysFont("Arial", 22, bold=True)

while True:
    dt = clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if game_over and (event.key == pygame.K_SPACE or event.key == pygame.K_r):
                snake = [[10, 10], [9, 10], [8, 10]]
                direction = [1, 0]
                next_direction = [1, 0]
                score = 0
                game_over = False
            elif not game_over:
                if event.key == pygame.K_UP and direction != [0, 1]: next_direction = [0, -1]
                elif event.key == pygame.K_DOWN and direction != [0, -1]: next_direction = [0, 1]
                elif event.key == pygame.K_LEFT and direction != [1, 0]: next_direction = [-1, 0]
                elif event.key == pygame.K_RIGHT and direction != [-1, 0]: next_direction = [1, 0]

    if not game_over:
        food_pulse += dt * 0.005
        move_timer += dt
        if move_timer >= move_delay:
            move_timer = 0
            direction = next_direction
            new_head = [snake[0][0] + direction[0], snake[0][1] + direction[1]]

            if not (0 <= new_head[0] < GRID_WIDTH and 0 <= new_head[1] < GRID_HEIGHT) or new_head in snake:
                game_over = True
            else:
                snake.insert(0, new_head)
                if new_head == food:
                    score += 10
                    food = [random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)]
                else:
                    snake.pop()

    screen.fill(BG_COLOR)
    
    fx = food[0] * GRID_SIZE + GRID_SIZE // 2
    fy = food[1] * GRID_SIZE + GRID_SIZE // 2
    radius = int(GRID_SIZE // 2 - 2 + math.sin(food_pulse) * 2)
    pygame.draw.circle(screen, FOOD_GLOW, (fx, fy), max(2, radius + 3))
    pygame.draw.circle(screen, FOOD_COLOR, (fx, fy), max(2, radius))

    for idx, seg in enumerate(snake):
        color = SNAKE_HEAD if idx == 0 else SNAKE_BODY
        pygame.draw.rect(screen, color, (seg[0]*GRID_SIZE+1, seg[1]*GRID_SIZE+1, GRID_SIZE-2, GRID_SIZE-2), border_radius=4)

    score_surface = font.render(f"Score: {score}", True, TEXT_COLOR)
    screen.blit(score_surface, (15, 15))

    if game_over:
        go_text = font.render("GAME OVER - Press Space/R", True, (239, 68, 68))
        screen.blit(go_text, (WIDTH//2 - go_text.get_width()//2, HEIGHT//2))

    pygame.display.flip()
