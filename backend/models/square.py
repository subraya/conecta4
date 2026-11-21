class Square:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.player = None
        self.available = False

    def occupy(self, player):
        if self.player: raise ValueError("Already occupied")
        if not self.available: raise ValueError("Not available")
    
        self.player = player
        self.available = False

    def mark_available(self):
        if self.player: raise ValueError("Already occupied")

        self.available = True

    def xy_coordinates(self):
        # returns square coordinate in xy format instead of row-column
        # it doesn't interpret whether row 0 is the one at the top or the bottom in a graphical view
        return (self.col, self.row)

    def rowcol_coordinates(self):
        return (self.row, self.col)

    def as_move_str(self):
        return f"r{self.row}c{self.col}"

    def __str__(self):
        return f"[{self.row},c{self.col}]"