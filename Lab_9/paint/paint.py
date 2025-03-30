import pygame

# Initialize Pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    drawing_mode = 'brush'  # Modes: brush, rectangle, circle, eraser, square, right_triangle, equilateral_triangle, rhombus
    points = []
    start_pos = None
    drawing = False
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Change color mode
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_e:
                    drawing_mode = 'eraser'
                elif event.key == pygame.K_c:
                    drawing_mode = 'circle'
                elif event.key == pygame.K_t:
                    drawing_mode = 'rectangle'
                elif event.key == pygame.K_s:
                    drawing_mode = 'square'
                elif event.key == pygame.K_y:
                    drawing_mode = 'right_triangle'
                elif event.key == pygame.K_u:
                    drawing_mode = 'equilateral_triangle'
                elif event.key == pygame.K_h:
                    drawing_mode = 'rhombus'
                elif event.key == pygame.K_p:
                    drawing_mode = 'brush'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click
                    start_pos = event.pos
                    drawing = True
                elif event.button == 3:  # Right click to change brush size
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if drawing_mode in ['rectangle', 'circle', 'square', 'right_triangle', 'equilateral_triangle', 'rhombus']:
                        drawShape(screen, drawing_mode, start_pos, event.pos, mode, radius)
                    drawing = False
            
            if event.type == pygame.MOUSEMOTION and drawing:
                if drawing_mode == 'brush':
                    points.append(event.pos)
                    points = points[-256:]
                elif drawing_mode == 'eraser':
                    pygame.draw.circle(screen, (0, 0, 0), event.pos, radius)
        
        screen.fill((0, 0, 0))
        
        # Draw all points for brush tool
        for i in range(len(points) - 1):
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
        
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    pygame.draw.line(screen, color, start, end, width)

def drawShape(screen, shape, start, end, color_mode, width):
    color_map = {'blue': (0, 0, 255), 'red': (255, 0, 0), 'green': (0, 255, 0)}
    color = color_map.get(color_mode, (255, 255, 255))
    
    if shape == 'rectangle':
        rect = pygame.Rect(start, (end[0] - start[0], end[1] - start[1]))
        pygame.draw.rect(screen, color, rect, width)
    elif shape == 'circle':
        center = start
        radius = int(((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2) ** 0.5)
        pygame.draw.circle(screen, color, center, radius, width)
    elif shape == 'square':
        side = min(abs(end[0] - start[0]), abs(end[1] - start[1]))
        rect = pygame.Rect(start, (side, side))
        pygame.draw.rect(screen, color, rect, width)
    elif shape == 'right_triangle':
        pygame.draw.polygon(screen, color, [start, (start[0], end[1]), (end[0], end[1])], width)
    elif shape == 'equilateral_triangle':
        height = abs(end[1] - start[1])
        pygame.draw.polygon(screen, color, [start, (start[0] + height, start[1] + height), (start[0] - height, start[1] + height)], width)
    elif shape == 'rhombus':
        width_rhombus = abs(end[0] - start[0])
        height_rhombus = abs(end[1] - start[1])
        pygame.draw.polygon(screen, color, [(start[0], start[1] - height_rhombus // 2), (start[0] + width_rhombus // 2, start[1]), (start[0], start[1] + height_rhombus // 2), (start[0] - width_rhombus // 2, start[1])], width)

main()