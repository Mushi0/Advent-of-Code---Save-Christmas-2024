import sys
import time

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        raw_data = f.read().splitlines()
    data = [[int(x) for x in line] for line in raw_data]
    
    total_reachable_nines = 0
    starts = [(i, j) for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == 0]
    for start in starts:
        stack = [start]
        visited = set()
        reachable_nines = set()
        while stack:
            x, y = stack.pop()
            if (x, y) in visited:
                continue
            visited.add((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= len(data) or ny < 0 or ny >= len(data[0]):
                    continue
                if data[nx][ny] == (data[x][y] + 1):
                    stack.append((nx, ny))
                    if data[nx][ny] == 9:
                        reachable_nines.add((nx, ny))
        total_reachable_nines += len(reachable_nines)
        # print(f'Starting at {start}, reachable 9s: {len(reachable_nines)}')
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of the scores of all trailheads is: {total_reachable_nines}. ')

if __name__ == '__main__':
    main(sys.argv[1])