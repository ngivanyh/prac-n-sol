# UVa Unidirectional TSP

h, w = map(int, input().split())
grid = [[int(cell) for cell in input().split()] for i in range(h)]

paths = []
print(grid)

def go(col, row, visited):
    pass

for i in range(h):
    go(0, i, [grid[i][0]])