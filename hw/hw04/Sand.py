from Grid import Grid


class Sand:

    def __init__(self, grid, x=0, y=0):
        self.x = x
        self.y = y
        self.grid = grid

    def __str__(self):
        return f"Sand({self.x},{self.y})"

    def gravity(self):
        if isinstance(self.grid.get(self.x, self.y), Sand):
            if self.is_move_ok(self.x, self.y + 1):
                pos = (self.x, self.y+1)
                return pos
            elif self.is_move_ok(self.x - 1, self.y + 1):
                pos = (self.x - 1, self.y+1)
                return pos
            elif self.is_move_ok(self.x + 1, self.y + 1):
                pos = (self.x+1, self.y+1)
                return pos
            else:
                return None

    def is_move_ok(self, x_to, y_to):
        try:
            if self.grid.get(x_to, y_to) is None:
                if x_to - self.x == 0:
                    return True
                elif x_to - self.x == 1:
                    if self.grid.get(x_to, self.y) is None or self.grid.get(self.x, y_to) is None:
                        return True
                elif x_to - self.x == -1:
                    if self.grid.get(x_to, self.y) is None or self.grid.get(self.x, y_to) is None:
                        return True
            return False
        except IndexError:
            return False

    def move(self, physics):
        coordinates = physics()
        if coordinates is None:
            return
        self.grid.set(self.x, self.y, None)
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.grid.set(self.x, self.y, self)
