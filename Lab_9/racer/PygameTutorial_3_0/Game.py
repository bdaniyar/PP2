import pygame, sys, random, time
from pygame.locals import *

# Initializing Pygame
pygame.init()

# FPS settings
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)

# Game variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0  # Coin counter
COIN_THRESHOLD = 5   # Increase speed after collecting N coins

# Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Loading images
background = pygame.image.load("AnimatedStreet.png")

# Game window
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        """Moves the enemy downward and resets its position at the top"""
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        """Handles player movement"""
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (30, 30))  # Rescaling
        self.rect = self.image.get_rect()
        self.weight = random.randint(1, 3)  # Assign random weight (1-3)
        self.reset()

    def move(self):
        """Moves the coin downward and resets if it goes off-screen"""
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.reset()

    def reset(self):
        """Resets the coin at a random position above the screen with new weight"""
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), random.randint(-600, -50))
        self.weight = random.randint(1, 3)

# Creating objects
P1 = Player()
E1 = Enemy()
coins = [Coin() for _ in range(3)]  # Creating multiple coins

# Sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins_group = pygame.sprite.Group(coins)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, *coins)

# Speed increase timer
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Drawing the background
    DISPLAYSURF.blit(background, (0, 0))

    # Displaying score
    score_text = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(score_text, (10, 10))

    # Displaying collected coins
    coins_text = font_small.render(f"Coins: {COINS_COLLECTED}", True, RED)
    DISPLAYSURF.blit(coins_text, (SCREEN_WIDTH - 100, 10))

    # Moving all objects
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Checking for coin collection
    for coin in coins:
        if P1.rect.colliderect(coin.rect):  # If the player collects a coin
            COINS_COLLECTED += coin.weight  # Add coin weight to total
            coin.reset()  # Reset the coin
            if COINS_COLLECTED % COIN_THRESHOLD == 0:  # Increase speed at threshold
                SPEED += 1

    # Checking for collision with enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)

        # "Game Over" screen
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
