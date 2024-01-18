import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    # Check if the board is full (a draw)
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def get_user_move(board, current_player):
    while True:
        print_board(board)
        row = int(input(f"{current_player}, enter row (0, 1, or 2): "))
        col = int(input(f"{current_player}, enter column (0, 1, or 2): "))

        if board[row][col] == " ":
            board[row][col] = current_player
            break
        else:
            print("Invalid move. The cell is already occupied. Try again.")

def get_bot_move(board, current_player):
    print_board(board)
    print(f"{current_player} is making a move...")
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        if board[row][col] == " ":
            board[row][col] = current_player
            break

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")

    while True:
        user_name = input("Enter your name: ")
        user_symbol = input(f"Hello, {user_name}! Choose your symbol (X or O): ").upper()

        if user_symbol == "X":
            bot_symbol = "O"
        elif user_symbol == "O":
            bot_symbol = "X"
        else:
            print("Invalid symbol. Defaulting to X.")
            user_symbol = "X"
            bot_symbol = "O"

        print(f"{user_name}, you are {user_symbol}. The bot is {bot_symbol}.")

        board = [[" " for _ in range(3)] for _ in range(3)]
        current_player = user_symbol

        while True:
            if current_player == user_symbol:
                get_user_move(board, current_player)
            else:
                get_bot_move(board, current_player)

            if check_winner(board, current_player):
                print_board(board)
                print(f"{current_player} wins! Congratulations, {user_name}!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                current_player = user_symbol if current_player == bot_symbol else bot_symbol

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing. Goodbye!")
            break

if __name__ == "__main__":
    tic_tac_toe()
