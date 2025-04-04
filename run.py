import random
import time
from enums import Winner
from board import Board


def play_game(i):
    """
    Play new round with new empty board.
    If i is even the user starts, else computer starts.
    i will be increased after every round.
    """
    board = Board()  # Create new empty board
    winner = Winner.NONE  # Set the winner to NONE
    board.print()
    print(f"\nRound: {i + 1}\n")
    if i % 2 == 0:  # i is even >> you start
        print("You start.")
    else:  # i is odd >> computer starts
        print("Computer starts.")

    # The new game will keep going until the winner is not NONE
    while winner == Winner.NONE:
        if i % 2 == 0:  # User turn
            user_move(board)
        else:  # Computer turn
            computer_move(board)
        # After every move, we check if there is a winning combination
        winner = board.check_winner()
        if winner == Winner.USER:
            print("\n*** You win! *** " +
                  f" Winning comibination is: {board.win_combo} ***\n")
        elif winner == Winner.COMPUTER:
            print("\n*** Computer wins! ***" +
                  f" Winning comibination is: {board.win_combo} ***\n")
        elif winner == Winner.DRAW:
            print("\n*** It's a draw! ***\n")
        i += 1  # this will change the turn
    return winner


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


def computer_move(board):
    """
    In this function, the computer makes a move.
    The move will be taken according to the actual situation of the board.
    """
    print("\nComputer is thinking...\n")
    time.sleep(0.5)
    position_found = False
    position = 0

    # 1. Check if there is a winning move
    for pos in range(1, 10):  # check all cells
        if board.is_valid_move(pos):  # if the cell is empty >> valid move
            board.make_move(pos, 'o')  # first, make the move
            # Check if the move is winning move?
            if board.check_winner() == Winner.COMPUTER:
                position = pos
                position_found = True
                break
            board.clear_cell(pos)  # if it is not a winnig move, undo move

    # 2. Check if there is a block user's winning move
    if not position_found:
        for pos in range(1, 10):  # check all cells
            if board.is_valid_move(pos):  # if the cell is empty >> valid move
                board.make_move(pos, 'x')  # make the move for the user
                # Check if the move is blocking move
                # Blocking move means, it is a winning move for the user
                # if so, the computer should take it
                if board.check_winner() == Winner.USER:
                    board.clear_cell(pos)
                    board.make_move(pos, 'o')  # if it is, take it
                    position = pos
                    position_found = True
                    break
                board.clear_cell(pos)  # if it's not a blocking move, undo move

    # 3. Take center if empty
    if not position_found and board.is_valid_move(5):
        board.make_move(5, 'o')
        position = 5
        position_found = True

    # 4. Take a corner if available
    if not position_found:
        corners = [1, 3, 7, 9]
        # shaffle the corners list,
        # so the computer does not make the same move every time
        random.shuffle(corners)
        for pos in corners:
            if board.is_valid_move(pos):
                board.make_move(pos, 'o')
                position = pos
                position_found = True
                break

    # 5. Pick random cell
    if not position_found:
        available_cells = board.get_available_cells()
        pos = random.choice(available_cells)
        board.make_move(pos, 'o')
        position = pos

    print(f"Computer chooses position {position}.\n")
    time.sleep(0.5)
    board.print()


def main():
    """
    The main function which manages the game.
    Start a new round as long as the user wants to play.
    Check if there is a winner after each round.
    And increase the score accordingly.
    """
    print("\nWelcome to Tic Tac Toe!\n")
    i = 0  # when i is even >> user starts
    user_score = 0
    computer_score = 0
    continue_playing = True
    while continue_playing:
        winner = play_game(i)
        if winner == Winner.USER:
            user_score += 1
        elif winner == Winner.COMPUTER:
            computer_score += 1
        print(f"*** Your score: {user_score}, " +
              f"Computer score: {computer_score} ***\n")
        i += 1  # change the starting player
        print("Do you want to continue playing?")
        play_more = input("enter 'y' to continue, or any other key to exit: ")
        print()
        if play_more.upper() != 'Y':
            continue_playing = False
    # The user wants to stop
    print("Thanks for playing Tic Tac Toe.")
    print("Hope to see you again soon.\n")


main()
