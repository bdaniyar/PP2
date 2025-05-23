import pygame
import random
import sys


pygame.init()

# Game constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
GRID_SIZE = 20
SNAKE_SPEED = 10  # Base speed
LEVEL_UP_FOOD = 3  # Foods needed to level up

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
snake = [(100, 100), (80, 100), (60, 100)]  # List of (x, y) positions
direction = "RIGHT"
change_to = direction

# Initial food position
def generate_food():
    """Generates food at a random position avoiding the snake body."""
    while True:
        food_x = random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE
        food_y = random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
        if (food_x, food_y) not in snake:  # Ensure food is not inside the snake
            return (food_x, food_y)

food = generate_food()

# Game variables
score = 0
level = 1
speed = SNAKE_SPEED

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handling key events for direction change
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"

    # Update snake direction
    direction = change_to

    # Move snake head
    head_x, head_y = snake[0]
    if direction == "UP":
        head_y -= GRID_SIZE
    elif direction == "DOWN":
        head_y += GRID_SIZE
    elif direction == "LEFT":
        head_x -= GRID_SIZE
    elif direction == "RIGHT":
        head_x += GRID_SIZE

    # Check for border collision
    if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT:
        running = False  # End game

    # Insert new head position
    new_head = (head_x, head_y)
    snake.insert(0, new_head)

    # Check if the snake eats food
    if new_head == food:
        score += 1
        food = generate_food()  # Generate new food
    else:
        snake.pop()  # Remove tail if no food eaten

    # Check if the snake collides with itself
    if new_head in snake[1:]:
        running = False  # End game

    # Level up condition
    if score % LEVEL_UP_FOOD == 0 and score > 0:
        level = (score // LEVEL_UP_FOOD) + 1
        speed = SNAKE_SPEED + (level - 1) * 2  # Increase speed

    # Drawing everything
    screen.fill(BLACK)

    # Draw snake
    for segment in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # Draw food
    pygame.draw.rect(screen, RED, pygame.Rect(food[0], food[1], GRID_SIZE, GRID_SIZE))

    # Display score and level
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (SCREEN_WIDTH - 100, 10))

    # Update display
    pygame.display.flip()

    # Control speed
    clock.tick(speed)


pygame.quit()
sys.exit()
