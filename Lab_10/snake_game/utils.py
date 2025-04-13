import pygame

# Функция для обработки паузы
def handle_pause():
    paused = True
    font = pygame.font.Font(None, 36)
    pause_text = font.render("Paused. Press 'P' to resume.", True, (255, 255, 255))

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = False

        pygame.display.get_surface().blit(pause_text, (200, 150))
        pygame.display.update()
