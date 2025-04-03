from enums import Winner


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

    def get_available_cells(self):
        """
        Return a list of all empty cells in the board.
        """
        return [self.cells.index(cell) + 1
                for cell in self.cells if cell == ' ']

    def clear_cell(self, position):
        """
        Make the cell empty.
        Computer may need to make the cell empty again after some testing.
        """
        self.cells[position - 1] = ' '

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

    def check_winner(self):
        """
        Check if there is a winning combination in the board
        """
        win_combinations = [  # all winning combinations
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in win_combinations:
            if all(self.cells[i] == 'x' for i in combo):  # user wins
                self.win_combo = [i + 1 for i in combo]
                return Winner.USER
            elif all(self.cells[i] == 'o' for i in combo):  # computer wins
                self.win_combo = [i + 1 for i in combo]
                return Winner.COMPUTER
        if not (' ' in self.cells):  # the board is full >> draw
            return Winner.DRAW
        return Winner.NONE
