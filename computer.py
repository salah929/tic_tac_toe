import random
import time
from enums import Winner


class Computer:
    """
    Represents the Computer as the opponent player.
    """

    def move_easy(self, board):
        """
        Make a move randomly.
        """

        # Pick random cell
        available_cells = board.get_available_cells()
        position = random.choice(available_cells)
        board.make_move(position, 'o')

        print(f"Computer chooses position {position}.\n")
        time.sleep(0.5)
        board.print()

    def move_hard(self, board):
        """
        Make a move according to the actual situation of the board.
        """

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
                board.clear_cell(pos)  # if it is not a winning move, undo move

        # 2. Check if there is a blocking move
        #    This means it is a user winning move
        if not position_found:
            for pos in range(1, 10):  # check all cells
                if board.is_valid_move(pos):  # if cell is empty >> valid move
                    board.make_move(pos, 'x')  # make the move for the user
                    # If user has a winning move, block it
                    if board.check_winner() == Winner.USER:
                        board.clear_cell(pos)
                        board.make_move(pos, 'o')  # if it is, take it
                        position = pos
                        position_found = True
                        break
                    board.clear_cell(pos)  # not a blocking move >> undo move

        # 3. Take center if empty
        if not position_found and board.is_valid_move(5):
            board.make_move(5, 'o')
            position = 5
            position_found = True

        # 4. Take a corner if available
        if not position_found:
            corners = [1, 3, 7, 9]
            # shuffle the corners list,
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
            position = random.choice(available_cells)
            board.make_move(position, 'o')

        print(f"Computer chooses position {position}.\n")
        time.sleep(0.5)
        board.print()

    def move(self, board, level):
        """
        In this function, the computer makes a move.
        The move will be taken accoring to the level of the game and
        the actual situation of the board.
        """

        print("\nComputer is thinking...\n")
        time.sleep(0.5)
        if level == 1:
            self.move_easy(board)
        else:
            self.move_hard(board)
