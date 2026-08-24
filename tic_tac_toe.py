"""
Tic Tac Toe - Two Player Console Game
Players take turns entering positions 1-9 corresponding to the board layout:

 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9
"""

def print_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()


def check_winner(board, player):
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6),             # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_combos)


def is_board_full(board):
    return all(cell in ("X", "O") for cell in board)


def get_move(board, player):
    while True:
        choice = input(f"Player {player}, enter a position (1-9): ").strip()
        if not choice.isdigit() or not (1 <= int(choice) <= 9):
            print("Please enter a number between 1 and 9.")
            continue
        idx = int(choice) - 1
        if board[idx] in ("X", "O"):
            print("That spot is already taken. Try again.")
            continue
        return idx


def play_game():
    board = [str(i) for i in range(1, 10)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        idx = get_move(board, current_player)
        board[idx] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            break

        if is_board_full(board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

    play_again = input("Play again? (y/n): ").strip().lower()
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing!")


if __name__ == "__main__":
    play_game()
