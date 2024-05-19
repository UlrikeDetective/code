import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen dimensions and colors
width, height = 800, 600
black = (0, 0, 0)
colors = [(255, 0, 0), (0, 255, 255), (255, 192, 203), (255, 255, 0), (0, 255, 0), (255, 165, 0)]

# Set up display
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame Drawing Example")

# Parameters
length = 100
angle = 50
size = 5

# Main loop
running = True
i = 0
while running and i < length:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    color = random.choice(colors)
    x = 400 + (i + 50) * math.cos(math.radians(i * angle))
    y = 300 + (i + 50) * math.sin(math.radians(i * angle))

    pygame.draw.circle(screen, color, (int(x), int(y)), size)
    pygame.display.flip()
    
    i += 1
    pygame.time.delay(100)

# Quit pygame
pygame.quit()
