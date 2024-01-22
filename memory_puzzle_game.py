# memory_puzzle_game.py

import random
import time

def create_board(size):
    symbols = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    random_symbols = symbols * (size // 2)
    random.shuffle(random_symbols)

    board = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            board[i][j] = random_symbols.pop()

    return board

def display_board(board, revealed):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if revealed[i][j]:
                print(board[i][j], end=" ")
            else:
                print("*", end=" ")
        print()

def get_guess(size):
    while True:
        try:
            row = int(input(f"Enter the row (1-{size}): ")) - 1
            col = int(input(f"Enter the column (1-{size}): ")) - 1

            if 0 <= row < size and 0 <= col < size:
                return row, col
            else:
                print("Invalid input. Please enter valid row and column numbers.")
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def play_memory_puzzle():
    print("Welcome to Memory Puzzle!")

    board_size = 4
    board = create_board(board_size)
    revealed = [[False] * board_size for _ in range(board_size)]
    pairs_found = 0

    while pairs_found < board_size * board_size // 2:
        display_board(board, revealed)

        first_guess = get_guess(board_size)
        revealed[first_guess[0]][first_guess[1]] = True
        display_board(board, revealed)

        second_guess = get_guess(board_size)
        revealed[second_guess[0]][second_guess[1]] = True
        display_board(board, revealed)

        if board[first_guess[0]][first_guess[1]] == board[second_guess[0]][second_guess[1]]:
            print("You found a pair!")
            pairs_found += 1
        else:
            print("No match. Try again.")
            revealed[first_guess[0]][first_guess[1]] = False
            revealed[second_guess[0]][second_guess[1]] = False

        time.sleep(1)  # Pause for a moment to display the cards
        print("\n" + "-" * 30 + "\n")

    print("Congratulations! You found all the pairs.")

if __name__ == "__main__":
    play_memory_puzzle()
