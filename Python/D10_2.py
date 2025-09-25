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
        reachable_paths_list = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
        reachable_paths_list[start[0]][start[1]] = 1
        for value in range(1, 10):
            for i in range(len(data)):
                for j in range(len(data[0])):
                    if data[i][j] != value:
                        continue
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = i + dx, j + dy
                        if nx < 0 or nx >= len(data) or ny < 0 or ny >= len(data[0]):
                            continue
                        if data[nx][ny] == (data[i][j] - 1):
                            reachable_paths_list[i][j] += reachable_paths_list[nx][ny]
        reachable_nines = sum(reachable_paths_list[i][j] for i in range(len(data)) for j in range(len(data[0])) if data[i][j] == 9)
        # print(f'Starting at {start}, reachable paths to 9s: {reachable_nines}')
        total_reachable_nines += reachable_nines
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of the scores of all trailheads is: {total_reachable_nines}. ')

if __name__ == '__main__':
    main(sys.argv[1])