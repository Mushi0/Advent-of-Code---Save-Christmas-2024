import sys
import time

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        map = f.read().splitlines()
    map = [list(line) for line in map]
    
    # calculate the number of edges for each cell (perimeter)
    edges = [[4 for _ in range(len(map[0]))] for _ in range(len(map))]
    for i in range(len(map)):
        for j in range(len(map[0])):
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < len(map) and 0 <= nj < len(map[0]) and map[ni][nj] == map[i][j]:
                    edges[i][j] -= 1
    
    # calculate the number of tiles in each cell (area)
    # and the price = area * perimeter
    total_price = 0
    tiles_checked = set()
    for i in range(len(map)):
        for j in range(len(map[0])):
            if (i, j) in tiles_checked:
                continue
            stack = [(i, j)]
            area = 0
            perimeter = 0
            while stack:
                x, y = stack.pop()
                if (x, y) in tiles_checked:
                    continue
                tiles_checked.add((x, y))
                area += 1
                perimeter += edges[x][y]
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < len(map) and 0 <= ny < len(map[0]) and map[nx][ny] == map[x][y]:
                        stack.append((nx, ny))
            total_price += area * perimeter
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The total price is: {total_price}. ')

if __name__ == '__main__':
    main(sys.argv[1])