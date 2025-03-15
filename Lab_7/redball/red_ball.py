import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Red Ball")


WHITE = (255, 255, 255)
RED = (255, 0, 0)


ball_x = WIDTH // 2  
ball_y = HEIGHT // 2    
speed = 20
radius = 25

clock = pygame.time.Clock()


running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and ball_x - radius > 0:
        ball_x -= speed
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and ball_x + radius < WIDTH:
        ball_x += speed
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and ball_y - radius > 0:
        ball_y -= speed
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and ball_y + radius < HEIGHT:
        ball_y += speed

    
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (ball_x, ball_y), radius)

    
    pygame.display.update()
    
    
    clock.tick(60)

pygame.quit()
sys.exit()
