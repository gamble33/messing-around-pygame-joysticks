import pygame
import math

# --- WINDOW --- 
(width, height) = (1280, 720)
bg_col = (150, 0, 255)
running = True

# --- INITIALIZATION ---
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
screen.fill(bg_col)
pygame.display.flip()
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print(joysticks)

# --- VARIABLES ---
t_last_frame = 0

# --- GAME DATA ---
oli = 10
oli_y = 360

# --- GAME LOOP ---
while running:
    
    t = pygame.time.get_ticks()
    dt = (t - t_last_frame) / 1000.0
    t_last_frame = t

    # --- EVENTS ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.JOYBUTTONUP:
            oli_y -= 10
        elif event.type == pygame.JOYBUTTONDOWN:
            oli_y += 10

    # --- UPDATE ---
    oli += 1 * dt
            
    screen.fill(bg_col)
    # --- DRAW ---
    pygame.draw.circle(
        screen,
        (30,30,30), 
        (720 + math.sin(oli)*10,  370),
         75
    )

    pygame.draw.circle(
        screen,
        (0,100,0), 
        (720 + math.sin(oli)*10,  oli_y),
         75
    )

    pygame.display.flip()
    clock.tick(30)
    
