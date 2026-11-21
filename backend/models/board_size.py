class BoardSize:
    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns

    def is_valid_position(self, row: int, col: int):
        return row >= 0 and row < self.rows and col >= 0 and col < self.columns