with open("./input.txt") as f:
    grid = [list(l.rstrip()) for l in f]

rows, cols = len(grid), len(grid[0])


def remove_rolls(repeat=False):
    total = 0
    any_removed = True
    while any_removed:
        any_removed = False
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != "@":
                    continue
                count = 0
                for dr, dc in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
                    cr, cc = r + dr, c + dc
                    if 0 <= cr < rows and 0 <= cc < cols:
                        count += grid[cr][cc] == "@"

                if count < 4:
                    total += 1
                    any_removed = True
                    if repeat:
                        grid[r][c] = "."

        if not repeat:
            break

    return total


print(remove_rolls())  # part 1
print(remove_rolls(repeat=True))  # part 2
