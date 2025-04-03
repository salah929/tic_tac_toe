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
        This will print two boards.
        One is the actual board with the letters o, x or empty.
        The second one shows the remaining possible moves.
        """
        c1 = self.cells[0]
        p1 = "1" if c1 == " " else " "
        c2 = self.cells[1]
        p2 = "2" if c2 == " " else " "
        c3 = self.cells[2]
        p3 = "3" if c3 == " " else " "
        c4 = self.cells[3]
        p4 = "4" if c4 == " " else " "
        c5 = self.cells[4]
        p5 = "5" if c5 == " " else " "
        c6 = self.cells[5]
        p6 = "6" if c6 == " " else " "
        c7 = self.cells[6]
        p7 = "7" if c7 == " " else " "
        c8 = self.cells[7]
        p8 = "8" if c8 == " " else " "
        c9 = self.cells[8]
        p9 = "9" if c9 == " " else " "

        print("Actual Board           Possible Moves")
        print("┌───┬───┬───┐          ┌───┬───┬───┐")
        print(f"│ {c1} │ {c2} │ {c3} │" + "          " +
              f"│ {p1} │ {p2} │ {p3} │")
        print("├───┼───┼───┤" + "          " + "├───┼───┼───┤")
        print(f"│ {c4} │ {c5} │ {c6} │" + "          " +
              f"│ {p4} │ {p5} │ {p6} │")
        print("├───┼───┼───┤" + "          " + "├───┼───┼───┤")
        print(f"│ {c7} │ {c8} │ {c9} │" + "          " +
              f"│ {p7} │ {p8} │ {p9} │")
        print("└───┴───┴───┘" + "          " + "└───┴───┴───┘")

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
