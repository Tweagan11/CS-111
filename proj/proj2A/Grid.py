from copy import deepcopy


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
        for _ in range(self.height):
            row = [None] * self.width
            self.array.append(row)

    def get(self, x, y):
        """
        Gets the value stored value at (x, y).
        (x, y) should be in bounds.
        """
        if self.in_bounds(x, y):
            return self.array[y][x]
        else:
            raise IndexError("")

    def set(self, x, y, val):
        """
        Sets a new value into the grid at (x, y).
        (x, y) should be in bounds.
        """
        if self.in_bounds(x, y):
            self.array[y][x] = val
        else:
            raise IndexError("")

    def in_bounds(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            return True
        else:
            return False

    def __str__(self):
        return f"Grid({self.height}, {self.width}, first = {self.array[0][0]})"

    def __repr__(self):
        return f"Grid.build({self.array})"

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other.array
        elif isinstance(other, list):
            return self.array == other

    @staticmethod
    def check_list_malformed(lst):
        # if isinstance(lst, list) and lst:
        #     for sub in lst:
        #         if isinstance(sub, list):
        #             length = len(lst[0])
        #             if len(sub) == length:
        #                 print("True")
        if not isinstance(lst, list):
            raise ValueError
        if not lst:
            raise ValueError
        if all(isinstance(sub, list) for sub in lst):
            if all(len(sub) == len(lst[0]) for sub in lst):
                return
            else:
                raise ValueError
        else:
            raise ValueError

    @staticmethod
    def build(lst):
        Grid.check_list_malformed(lst)
        height, width = len(lst), len(lst[0])
        grid = Grid(width, height)
        grid.array = deepcopy(lst)
        return grid

    def copy(self):
        grid = deepcopy(self.build(self.array))
        return grid
