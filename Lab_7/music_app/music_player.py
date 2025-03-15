import pygame

pygame.init()


WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(None, 36)


playlist = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_track = 0


pygame.mixer.music.load(playlist[current_track])

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_track
    current_track = (current_track + 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

def previous_track():
    global current_track
    current_track = (current_track - 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_track])
    pygame.mixer.music.play()

running = True
while running:
    screen.fill(WHITE)

    
    text = FONT.render(f"Now Playing: {playlist[current_track]}", True, BLACK)
    screen.blit(text, (20, 80))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Space for Play
                play_music()
            elif event.key == pygame.K_s:  # 'S' for Stop
                stop_music()
            elif event.key == pygame.K_n:  # 'N' for Next
                next_track()
            elif event.key == pygame.K_p:  # 'P' for Previous
                previous_track()

pygame.quit()