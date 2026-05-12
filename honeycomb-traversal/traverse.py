"""
traverses a honeycomb-shaped grid and report visited symbols & unique symbols visited

starts at the bottom-left cell (x=0, y=height-1).
0: up
1: right
2: down-right
3: down
4: left
5: up-left
stays in place if move is out-of-bounds
"""

height, width, move_count = map(int, input().split())

honeycomb = [input() for _ in range(height)]
passed = set()

moves = list(map(int, input().split()))

def walk(idx, x, y):
    if idx == len(moves):
        return

    old_x, old_y = x, y
    old_cell = honeycomb[y][x]

    match moves[idx]:
        case 0:
            y -= 1
        case 1:
            x += 1
        case 3:
            y += 1
        case 4:
            x -= 1
        case 2:
            y += 1
            x += 1
        case 5:
            y -= 1
            x -= 1
    invalid_pos = y < 0 or y >= height or x < 0 or x >= width
    cell = honeycomb[y][x] if not invalid_pos else old_cell
    passed.add(cell)

    pos = (x, y) if not invalid_pos else (old_x, old_y)

    print(cell, end="")

    return walk(idx + 1, pos[0], pos[1])

walk(0, 0, height - 1)
print(f"\n{len(passed)}")
