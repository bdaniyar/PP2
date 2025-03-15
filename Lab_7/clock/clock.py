import pygame
import datetime


pygame.init()


clock_image = pygame.image.load("clock.png")
min_hand = pygame.image.load("min_hand.png")
sec_hand = pygame.image.load("sec_hand.png")


WIDTH, HEIGHT = clock_image.get_size()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Mouse Clock")

clock_center = (WIDTH // 2, HEIGHT // 2)


running = True
while running:
    screen.fill((255, 255, 255))  

    
    now = datetime.datetime.now() + datetime.timedelta(minutes=9)
    minutes = now.minute 
    seconds = now.second

    
    min_angle = -(minutes * 6) 
    sec_angle = -(seconds * 6)  

    
    rotated_min = pygame.transform.rotate(min_hand, min_angle)
    rotated_sec = pygame.transform.rotate(sec_hand, sec_angle)

    
    min_rect = rotated_min.get_rect(center=clock_center)
    sec_rect = rotated_sec.get_rect(center=clock_center)

    
    screen.blit(clock_image, (0, 0))
    screen.blit(rotated_min, min_rect)
    screen.blit(rotated_sec, sec_rect)

    
    pygame.display.flip()

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    pygame.time.Clock().tick(30)

pygame.quit()
