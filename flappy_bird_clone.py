import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BIRD_WIDTH, BIRD_HEIGHT = 40, 40
PIPE_WIDTH, PIPE_HEIGHT = 50, 300
GRAVITY = 1
JUMP_VELOCITY = -15
PIPE_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Bird class
class Bird:
    def __init__(self):
        self.x = WIDTH // 4
        self.y = HEIGHT // 2
        self.velocity = 0
        self.rect = pygame.Rect(self.x, self.y, BIRD_WIDTH, BIRD_HEIGHT)

    def jump(self):
        self.velocity = JUMP_VELOCITY

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        self.rect.y = self.y

# Pipe class
class Pipe:
    def __init__(self):
        self.x = WIDTH
        self.gap_start = random.randint(50, HEIGHT - 150)
        self.rect_top = pygame.Rect(self.x, 0, PIPE_WIDTH, self.gap_start)
        self.rect_bottom = pygame.Rect(self.x, self.gap_start + 150, PIPE_WIDTH, HEIGHT - self.gap_start - 150)

    def update(self):
        self.x -= PIPE_SPEED
        self.rect_top.x = self.x
        self.rect_bottom.x = self.x

# Pygame window setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Create bird and pipes
bird = Bird()
pipes = []

# Clock setup
clock = pygame.time.Clock()

# Function to reset the game
def reset_game():
    global bird, pipes
    bird = Bird()
    pipes = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.jump()

    # Update bird
    bird.update()

    # Generate pipes
    if len(pipes) == 0 or pipes[-1].x < WIDTH - 200:
        pipes.append(Pipe())

    # Update pipes
    for pipe in pipes:
        pipe.update()

    # Check collisions
    if bird.rect.colliderect(pygame.Rect(pipe.x, 0, PIPE_WIDTH, pipe.gap_start)) or \
       bird.rect.colliderect(pygame.Rect(pipe.x, pipe.gap_start + 150, PIPE_WIDTH, HEIGHT - pipe.gap_start - 150)) or \
       bird.y < 0 or bird.y > HEIGHT - BIRD_HEIGHT:
        reset_game()

    # Remove off-screen pipes
    pipes = [pipe for pipe in pipes if pipe.x + PIPE_WIDTH > 0]

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, bird.rect)
    for pipe in pipes:
        pygame.draw.rect(screen, WHITE, pipe.rect_top)
        pygame.draw.rect(screen, WHITE, pipe.rect_bottom)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
