class Grid:
    """
    2D grid with (x, y) int indexed internal storage
    Has .width .height size properties
    """
    width = None
    height = None
    array = None

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.array = []
        for y in range(self.height):
            row = [None] * self.width
            self.array.append(row)

    def get(self, x, y):
        """
        Gets the value stored value at (x, y).
        (x, y) should be in bounds.
        """
        if self.in_bounds(x,y):
            return self.array[y][x]

    def set(self, x, y, val):
        """
        Sets a new value into the grid at (x, y).
        (x, y) should be in bounds.
        """
        if self.in_bounds(x,y):
            self.array[y][x] = val

    def in_bounds(self, x, y):
        if x < self.width and y < self.height:
            return True
        else:
            return False

    def __str__(self):
        return f"Grid({self.height}, {self.width}, first = {self.array[0][0]})"

    def __repr__(self):
        return f"Grid({self.height}, {self.width}, first = {self.array[0][0]})"

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other.array




