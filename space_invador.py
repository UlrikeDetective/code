import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Alien Shooter")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - 2 * player_size
player_speed = 5

# Alien
alien_size = 50
alien_speed = 2
alien_frequency = 25
aliens = []

# Bullet
bullet_size = 5
bullet_speed = 7
bullets = []

# Clock to control the frame rate
clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Move the player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and player_x > 0:
                player_x -= player_speed
            elif event.key == pygame.K_RIGHT and player_x < width - player_size:
                player_x += player_speed

            # Shoot a bullet
            elif event.key == pygame.K_SPACE:
                bullet = {'x': player_x + player_size // 2 - bullet_size // 2,
                          'y': player_y,
                          'speed': -bullet_speed}
                bullets.append(bullet)

    # Create aliens
    if random.randint(1, alien_frequency) == 1:
        alien = {'x': random.randint(0, width - alien_size),
                 'y': 0,
                 'speed': alien_speed}
        aliens.append(alien)

    # Move aliens
    for alien in aliens:
        alien['y'] += alien['speed']

        # Check for collisions with player
        if (player_x < alien['x'] < player_x + player_size or
                player_x < alien['x'] + alien_size < player_x + player_size) and \
                (player_y < alien['y'] + alien_size < player_y + player_size or
                 player_y < alien['y'] < player_y + player_size):
            pygame.quit()
            sys.exit()

        # Remove aliens that go off the screen
        if alien['y'] > height:
            aliens.remove(alien)

    # Move bullets
    for bullet in bullets:
        bullet['y'] += bullet['speed']

        # Remove bullets that go off the screen
        if bullet['y'] < 0:
            bullets.remove(bullet)

    # Check for collisions between bullets and aliens
    for bullet in bullets:
        for alien in aliens:
            if (alien['x'] < bullet['x'] < alien['x'] + alien_size or
                    alien['x'] < bullet['x'] + bullet_size < alien['x'] + alien_size) and \
                    (alien['y'] < bullet['y'] + bullet_size < alien['y'] + alien_size):
                aliens.remove(alien)
                bullets.remove(bullet)

    # Draw everything
    screen.fill(black)

    # Draw player
    pygame.draw.rect(screen, white, [player_x, player_y, player_size, player_size])

    # Draw aliens
    for alien in aliens:
        pygame.draw.rect(screen, red, [alien['x'], alien['y'], alien_size, alien_size])

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, white, [bullet['x'], bullet['y'], bullet_size, bullet_size])

    # Update the display
    pygame.display.flip()

    # Set the frame rate
    clock.tick(30)
