import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 400
PLAYER_SIZE = 50
ENEMY_SIZE = 30
BULLET_SIZE = 5
ENEMY_SPEED = 5
BULLET_SPEED = 7

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Pygame window setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Player setup
player_x = WIDTH // 2 - PLAYER_SIZE // 2
player_y = HEIGHT - PLAYER_SIZE - 10

# Enemy setup
enemies = []
for _ in range(10):
    enemy = pygame.Rect(random.randint(0, WIDTH - ENEMY_SIZE), random.randint(50, 200), ENEMY_SIZE, ENEMY_SIZE)
    enemies.append(enemy)

# Bullet setup
bullets = []

# Clock setup
clock = pygame.time.Clock()

# Function to draw the player, enemies, and bullets
def draw_elements():
    pygame.draw.rect(screen, GREEN, (player_x, player_y, PLAYER_SIZE, PLAYER_SIZE))
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = pygame.Rect(player_x + PLAYER_SIZE // 2 - BULLET_SIZE // 2, player_y, BULLET_SIZE, BULLET_SIZE)
                bullets.append(bullet)

    keys = pygame.key.get_pressed()
    player_x -= keys[pygame.K_LEFT] * 5
    player_x += keys[pygame.K_RIGHT] * 5
    player_x = max(0, min(WIDTH - PLAYER_SIZE, player_x))

    # Move enemies
    for enemy in enemies:
        enemy.y += ENEMY_SPEED
        if enemy.y > HEIGHT:
            enemy.y = 0
            enemy.x = random.randint(0, WIDTH - ENEMY_SIZE)

    # Move bullets
    for bullet in bullets:
        bullet.y -= BULLET_SPEED
        if bullet.y < 0:
            bullets.remove(bullet)

    # Check collisions
    for enemy in enemies:
        for bullet in bullets:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)
                enemy.y = 0
                enemy.x = random.randint(0, WIDTH - ENEMY_SIZE)

    # Check player collision
    for enemy in enemies:
        if enemy.colliderect((player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)):
            print("Game Over!")
            running = False

    # Draw everything
    screen.fill((0, 0, 0))
    draw_elements()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
