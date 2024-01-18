
import pygame
import sys
import random
import requests
from io import BytesIO

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 600
GRID_SIZE = 4
CARD_SIZE = WIDTH // GRID_SIZE
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Cards (Provide image URLs)
CARD_URLS = [
    "https://productsbuckets.s3.eu-north-1.amazonaws.com/images/apple.png",
    "https://productsbuckets.s3.eu-north-1.amazonaws.com/images/banana.png",
    "https://productsbuckets.s3.eu-north-1.amazonaws.com/images/cherry.png",
    "https://productsbuckets.s3.eu-north-1.amazonaws.com/images/grape.png",
    "https://productsbuckets.s3.eu-north-1.amazonaws.com/images/lemon.png",
    "https://productsbuckets.s3.eu-north-1.amazonaws.com/images/orange.png",
    "https://productsbuckets.s3.eu-north-1.amazonaws.com/images/pear.png",
    "https://productsbuckets.s3.eu-north-1.amazonaws.com/images/strawberry.png"
]

# Shuffle the card URLs
random.shuffle(CARD_URLS)

# Create a dictionary to store the card images
CARD_DICT = {}

# Function to load image with error handling
def load_image(url, index):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        return pygame.image.load(BytesIO(response.content))
    except Exception as e:
        print(f"Error loading image from {url}: {e}")
        print(f"Image at index {index} will be set to None.")
        return None

# Load images and populate CARD_DICT
for i, url in enumerate(CARD_URLS):
    image = load_image(url, i)
    CARD_DICT[i] = image

# Game setup
game_board = [[-1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
selected_cards = []
score = 0

# Pygame window setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Memory Puzzle")

# Font setup
font = pygame.font.Font(None, 36)

# Function to draw the grid
def draw_grid():
    for i in range(GRID_SIZE + 1):
        pygame.draw.line(screen, WHITE, (i * CARD_SIZE, 0), (i * CARD_SIZE, HEIGHT), 2)
        pygame.draw.line(screen, WHITE, (0, i * CARD_SIZE), (WIDTH, i * CARD_SIZE), 2)

# Function to draw cards
def draw_cards():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if game_board[i][j] == -1:  # Card face-down
                pygame.draw.rect(screen, WHITE, (j * CARD_SIZE, i * CARD_SIZE, CARD_SIZE, CARD_SIZE))
            else:  # Card face-up
                if CARD_DICT[game_board[i][j]] is not None:
                    screen.blit(CARD_DICT[game_board[i][j]], (j * CARD_SIZE, i * CARD_SIZE))

# Function to display the score
def draw_score():
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

# Function to check for a win
def check_win():
    return all(card == -1 for row in game_board for card in row)

# Function to reset the game
def reset_game():
    global game_board, selected_cards, score
    random.shuffle(CARD_URLS)
    CARD_DICT.update({i: pygame.image.load(BytesIO(requests.get(url).content)) for i, url in enumerate(CARD_URLS)})
    game_board = [[-1 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    selected_cards = []
    score = 0

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            row = event.pos[1] // CARD_SIZE
            col = event.pos[0] // CARD_SIZE

            if (row, col) not in selected_cards and game_board[row][col] == -1:
                selected_cards.append((row, col))
                if len(selected_cards) == 2:
                    i1, j1 = selected_cards[0]
                    i2, j2 = selected_cards[1]

                    if game_board[i1][j1] == game_board[i2][j2]:
                        score += 1
                        if check_win():
                            reset_game()
                    else:
                        pygame.time.delay(1000)
                        game_board[i1][j1] = game_board[i2][j2] = -1

                    selected_cards = []

    screen.fill(BLACK)
    draw_grid()
    draw_cards()
    draw_score()

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
