class Board:
    """
    Represents the game board
    """
    def __init__(self):
        """
        Initialize the board with empty nine cells.
        And empty winning combination of three cells.
        """
        self.cells = [' '] * 9
        self.win_combo = [' '] * 3

    def print(self):
        """
        Display the board on the screen in a 3x3 grid.
        """
        c1 = self.cells[0]
        c2 = self.cells[1]
        c3 = self.cells[2]
        c4 = self.cells[3]
        c5 = self.cells[4]
        c6 = self.cells[5]
        c7 = self.cells[6]
        c8 = self.cells[7]
        c9 = self.cells[8]

        print("┌───┬───┬───┐")
        print(f"│ {c1} │ {c2} │ {c3} │")
        print("├───┼───┼───┤")
        print(f"│ {c4} │ {c5} │ {c6} │")
        print("├───┼───┼───┤")
        print(f"│ {c7} │ {c8} │ {c9} │")
        print("└───┴───┴───┘")

    def make_move(self, position, symbol):
        """
        Make user move or computer move if it is valid.
        """
        # Attempt to make a selection at the given position (1-9)
        if self.is_valid_move(position):
            self.cells[position - 1] = symbol
            return True
        return False

    def is_valid_move(self, position):
        """
        Check if the move is valid (1-9 and not already taken).
        """
        return 1 <= position <= 9 and self.cells[position - 1] == ' '
