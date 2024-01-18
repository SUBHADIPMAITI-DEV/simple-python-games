import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
BALL_SIZE = 20
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 60
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.y += self.speed

# Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_SIZE, BALL_SIZE))
        self.image.fill(RED)  # Set the color to red
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.speed = 5
        self.direction = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.x += self.speed * self.direction[0]
        self.rect.y += self.speed * self.direction[1]

        # Bounce off walls
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.direction[1] *= -1

        # Reset position if the ball goes out of bounds
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.reset_position()

    def reset_position(self):
        self.rect.center = (WIDTH // 2, HEIGHT // 2)
        self.direction = [random.choice([-1, 1]), random.choice([-1, 1])]

# Main function
def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong Game")

    all_sprites = pygame.sprite.Group()
    paddles = pygame.sprite.Group()
    ball = Ball()

    player1 = Paddle(20, HEIGHT // 2)
    player2 = Paddle(WIDTH - 20, HEIGHT // 2)

    all_sprites.add(player1, player2, ball)
    paddles.add(player1, player2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        all_sprites.update()

        # Check for collisions with paddles
        if pygame.sprite.spritecollide(ball, paddles, False):
            ball.direction[0] *= -1

        screen.fill((0, 0, 0))
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
