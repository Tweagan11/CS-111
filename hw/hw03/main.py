from Grid import Grid

lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
grid = Grid.build(lst)
grid.set(0,1,10)
print(grid.get(0,1))
print(lst[0][1])
grid2 = grid.copy()
print(grid2.get(0,1))
print(repr(grid))

ls1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ls2 = "Hello"

Grid.build(ls1)
Grid.build(ls2)