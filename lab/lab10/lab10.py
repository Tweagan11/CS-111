from Grid import Grid
from random import random, randint


def print_grid(grid):
    """Prints a Grid object with all the elements of a row
    on a single line separated by spaces.
    """
    for y in range(grid.height):
        for x in range(grid.width):
            print(grid.get(x, y) if grid.get(x, y) is not None else 0, end=" ")
        print()
    print()


def random_rocks(grid, chance_of_rock):
    '''Take a grid, loop over it and add rocks randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.'''
    "*** YOUR CODE HERE ***"
    new_grid = grid.copy()
    # for x in range(grid.width):
    #     for y in range(grid.height):
    #         if random() <= chance_of_rock:
    #             new_grid.set(x, y, 'r')
    # return new_grid
    return modify_grid(new_grid, lambda x, y:
                        new_grid.set(x, y, 'r'), chance_of_rock)



def random_bubbles(grid, chance_of_bubbles):
    '''Take a grid, loop over it and add bubbles 'b' randomly
    then return the new grid. If there is something already
    in a grid position, don't add anything in that position.'''
    "*** YOUR CODE HERE ***"
    new_grid = grid.copy()
    # for x in range(grid.width):
    #     for y in range(grid.height):
    #         if new_grid.get(x,y) is None:
    #             if random() <= chance_of_bubbles:
    #                 new_grid.set(x, y, 'b')
    # return new_grid
    return modify_grid(new_grid, lambda x, y:
                        new_grid.set(x, y, 'b'), chance_of_bubbles)



def modify_grid(grid, func, prob):
    """Write a function which can take in a grid, a function
    and a probability as parameters and updates the grid using
    the function passed in."""
    "*** YOUR CODE HERE ***"
    for y in range(grid.height):
        for x in range(grid.width):
            if grid.get(x, y) is None:
                if random() < prob:
                    func(x,y)
    return grid

def bubble_up(grid, x, y):
    """
    Write a function that takes a bubble that is known
    to be able to bubble up and moves it up one row.
    """
    "*** YOUR CODE HERE ***"
    new_grid = grid.copy()
    new_grid.set(x, y-1, 'b')
    new_grid.set(x, y, None)
    return new_grid


def move_bubbles(grid):
    """
    Write a function that loops over the grid, finds
    bubbles, checks if the bubble can move upward, moves
    the bubble up.
    """
    new_grid = grid.copy()
    for y in range(1,new_grid.height):
        for x in range(new_grid.width):
            if new_grid.get(x, y) == 'b' and new_grid.get(x, y - 1) is None:
                new_grid = bubble_up(new_grid, x, y)
    return new_grid



def animate_grid(grid, delay):
    """Given an Grid object, and a delay time in seconds, this
    function prints the current grid contents (calls print_grid),
    waits for `delay` seconds, calls the move_bubbles() function,
    and repeats until the grid doesn't change.
    """
    from time import sleep
    prev = grid
    count = 0
    message = "Start"
    while True:
        print("\033[2J\033[;H", end="")
        message = f"Iteration {count}"
        print(message)
        print_grid(prev)
        sleep(delay)
        newGrid = move_bubbles(prev)
        if newGrid == prev:
            break
        prev = newGrid
        count += 1


if __name__ == "__main__":
    grid = Grid(50,50)
    print_grid(grid)
    new_grid = random_rocks(grid,.2)
    print_grid(new_grid)
    # new_grid = modify_grid(grid, lambda x, y: grid.set(x, y, 's'), 0.3)
    new_grid = random_bubbles(new_grid,.4)
    print_grid(new_grid)
    print_grid(move_bubbles(new_grid))
    animate_grid(new_grid, 1)