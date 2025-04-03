import time
from board import Board


def user_move(board):
    """
    This function allows the user to make a move.
    It accepts only the valid moves.
    The valid moves are the empty cells in the board.
    """
    valid_move = False
    while not valid_move:
        try:
            position = int(input("\nYour move? (1-9): "))
            valid_move = board.make_move(position, 'x')
            if valid_move:
                print("\nValid move.\n")
                time.sleep(0.5)
                board.print()
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def main():
    """
    The main function which manages the game.
    """
    print("\nWelcome to Tic Tac Toe!\n")
    board = Board()
    board.print()
    user_move(board)


main()
