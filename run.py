import time
from enums import Winner
from board import Board
from computer import Computer


def play_game(i, level):
    """
    Play new round with new empty board.
    level is the difficulty of the game, 1 for easy, 2 for difficult
    If i is even the user starts, else computer starts.
    i will be increased after every round.
    """
    computer = Computer()  # Create the opponent (Computer)
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
            computer.move(board, level)
        # After every move, we check if there is a winning combination
        winner = board.check_winner()
        if winner == Winner.USER:
            print("\n*** You win! *** " +
                  f" Winning combination is: {board.win_combo} ***\n")
        elif winner == Winner.COMPUTER:
            print("\n*** Computer wins! ***" +
                  f" Winning combination is: {board.win_combo} ***\n")
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
            position = int(input("\nYour move? (1-9):\n"))
            valid_move = board.make_move(position, 'x')
            if valid_move:
                print("\nValid move.\n")
                time.sleep(0.5)
                board.print()
            else:
                print("Invalid move. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")


def select_game_level():
    """
    This function allows the user to select the game level.
    It accepts only 1 and 2 numbers.
    1 >> easy , 2 >> difficult.
    """
    print("Please enter the level of the game.")
    while True:
        try:
            level = int(input("1 for easy, 2 for difficult:\n"))
            if level >= 1 and level <= 2:

                difficulty = "easy" if level == 1 else "difficult"
                print(f"\nOk. The level of the game is {difficulty}\n")
                time.sleep(0.5)
                return level
            else:
                print("\nInvalid input. Please enter 1 or 2.")
        except ValueError:
            print("\nInvalid input. Please enter 1 or 2.")


def main():
    """
    The main function which manages the game.
    Start a new round as long as the user wants to play.
    Check if there is a winner after each round.
    And increase the score accordingly.
    """
    print("\nWelcome to Tic Tac Toe!\n")
    level = select_game_level()
    i = 0  # when i is even >> user starts
    user_score = 0
    computer_score = 0
    continue_playing = True
    while continue_playing:
        winner = play_game(i, level)
        if winner == Winner.USER:
            user_score += 1
        elif winner == Winner.COMPUTER:
            computer_score += 1
        print(f"*** Your score: {user_score}, " +
              f"Computer score: {computer_score} ***\n")
        i += 1  # change the starting player
        print("Do you want to continue playing?")
        play_more = input("enter 'y' to continue, or any other key to exit:\n")
        print()
        if play_more.upper() != 'Y':
            continue_playing = False
    # The user wants to stop
    print("Thanks for playing Tic Tac Toe.")
    print("Hope to see you again soon.\n")


main()
