def display_board(board):
    """
    Prints the current state of the board.
    board is a list of 9 elements (strings),
    each representing a cell of the Tic-Tac-Toe board.
    """
    print("\n")
    print("  " + board[0] + " | " + board[1] + " | " + board[2])
    print(" ---+---+---")
    print("  " + board[3] + " | " + board[4] + " | " + board[5])
    print(" ---+---+---")
    print("  " + board[6] + " | " + board[7] + " | " + board[8])
    print("\n")


def is_winner(board, player):
    """
    Check if player ('X' or 'O') has won on the current board.
    Returns True if there's a winning combination for the player, False otherwise.
    """
    # All winning positions (indices) on a 3x3 board
    winning_positions = [
        (0, 1, 2),  # top row
        (3, 4, 5),  # middle row
        (6, 7, 8),  # bottom row
        (0, 3, 6),  # left column
        (1, 4, 7),  # middle column
        (2, 5, 8),  # right column
        (0, 4, 8),  # diagonal
        (2, 4, 6)   # diagonal
    ]
    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def is_draw(board):
    """
    Check if the board is full and there is no winner, i.e., it's a draw.
    """
    return all(cell != " " for cell in board)


def get_move(board, player):
    """
    Ask the user for a valid move (1-9) and update the board accordingly.
    The input 1-9 corresponds to the cells:
        1 | 2 | 3
       ---+---+---
        4 | 5 | 6
       ---+---+---
        7 | 8 | 9
    """
    while True:
        try:
            user_input = int(input(f"Player {player}, choose your position (1-9): "))
            if user_input < 1 or user_input > 9:
                print("Invalid input. Position must be between 1 and 9.")
            elif board[user_input - 1] != " ":
                print("That space is already taken. Choose another position.")
            else:
                board[user_input - 1] = player
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def play_game():
    """
    Main function to coordinate the flow of the Tic-Tac-Toe game.
    """
    # Initialize board with 9 empty spaces
    board = [" "] * 9

    current_player = "X"
    while True:
        # Display the board
        display_board(board)

        # Get the player's move
        get_move(board, current_player)

        # Check for a winner
        if is_winner(board, current_player):
            display_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break

        # Check for a draw
        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    play_game()
