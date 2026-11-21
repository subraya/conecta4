class MoveTester:
    @classmethod
    def is_all_player(self, tested_player, tested_square, combination):
        for square in combination:
            if square.row == tested_square.row and square.col == tested_square.col:
                pass
            elif square.player != tested_player:
                return False

        return True