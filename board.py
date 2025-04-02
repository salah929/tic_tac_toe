class Board:
    """
    Represents the game board
    """
    # Represents the game board
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
