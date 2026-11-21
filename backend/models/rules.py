from .board_size import BoardSize

class Rules:
    def __init__(self, rows, columns, goal):
        self.rows = rows
        self.columns = columns
        self.goal = goal
        self.board_size = BoardSize(rows, columns)
        self.__validate__()

    def as_dict(self):
        return { "rows": self.rows, "columns": self.columns, "goal": self.goal }

    def __validate__(self):
        if self.goal < 3:
            raise ValueError("Goal must be at least 3")
        if self.goal > self.rows or self.goal > self.columns:
            raise ValueError("Board size is not big enough")

DEFAULT = Rules(6, 7, 4)