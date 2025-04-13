import pygame
import random
import sys
from db import create_users_table, insert_user, get_user_data, update_user_score
from utils import handle_pause

pygame.init()

# Game constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20
SNAKE_SPEED = 10  # Base speed
LEVEL_UP_FOOD = 3  # Foods needed to level up
FOOD_LIFETIME = 300  # Frames before food disappears

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Load font for score and level
font = pygame.font.Font(None, 36)

# Snake initial settings
snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"
change_to = direction

# Food class
class Food:
    def __init__(self):
        self.generate()
    
    def generate(self):
        while True:
            self.x = random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE
            self.y = random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
            if (self.x, self.y) not in snake:
                break
        self.weight = random.randint(1, 3)
        self.timer = FOOD_LIFETIME
    
    def draw(self):
        color = {1: RED, 2: BLUE, 3: WHITE}[self.weight]
        pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y, GRID_SIZE, GRID_SIZE))
    
    def update(self):
        self.timer -= 1
        if self.timer <= 0:
            self.generate()

food = Food()

# Game variables
score = 0
level = 1
speed = SNAKE_SPEED
clock = pygame.time.Clock()

def start_game(username):
    global score, level, snake, direction, change_to, food

    # Initialize game variables
    running = True
    score = 0
    level = 1
    speed = SNAKE_SPEED
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = "RIGHT"
    change_to = direction
    food = Food()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != "DOWN":
                    change_to = "UP"
                elif event.key == pygame.K_DOWN and direction != "UP":
                    change_to = "DOWN"
                elif event.key == pygame.K_LEFT and direction != "RIGHT":
                    change_to = "LEFT"
                elif event.key == pygame.K_RIGHT and direction != "LEFT":
                    change_to = "RIGHT"
                elif event.key == pygame.K_p:
                    handle_pause()

        direction = change_to
        head_x, head_y = snake[0]

        if direction == "UP":
            head_y -= GRID_SIZE
        elif direction == "DOWN":
            head_y += GRID_SIZE
        elif direction == "LEFT":
            head_x -= GRID_SIZE
        elif direction == "RIGHT":
            head_x += GRID_SIZE

        if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
            running = False

        new_head = (head_x, head_y)
        snake.insert(0, new_head)

        if new_head == (food.x, food.y):
            score += food.weight
            food.generate()
        else:
            snake.pop()

        if new_head in snake[1:]:
            running = False

        if score % LEVEL_UP_FOOD == 0 and score > 0:
            level = (score // LEVEL_UP_FOOD) + 1
            speed = SNAKE_SPEED + (level - 1) * 2

        food.update()

        screen.fill(BLACK)

        for segment in snake:
            pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))

        food.draw()

        score_text = font.render(f"Score: {score}", True, WHITE)
        level_text = font.render(f"Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(level_text, (SCREEN_WIDTH - 100, 10))

        pygame.display.flip()

        if not running:
            update_user_score(username, score, level)

        clock.tick(speed)

    pygame.quit()
    sys.exit()

def main():
    create_users_table()

    username = input("Enter your username: ")

    user_id, user_level, user_score = get_user_data(username)

    if user_id:
        print(f"Welcome back, {username}! Your current level is {user_level} and score is {user_score}.")
    else:
        insert_user(username)
        print(f"Welcome, {username}! Your account has been created.")

    start_game(username)

if __name__ == '__main__':
    main()
