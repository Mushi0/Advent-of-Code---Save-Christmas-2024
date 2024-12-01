import sys
import time

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        raw_data = f.read().splitlines()

    data_A = []
    data_B = []
    for line in raw_data:
        new_line = [int(e) for e in line.split('   ')]
        data_A.append(new_line[0])
        data_B.append(new_line[1])

    data_A.sort()
    data_B.sort()

    total_distance = 0
    for i, e in enumerate(data_A):
        total_distance += abs(e - data_B[i])
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The total distance is: {total_distance}')

if __name__ == '__main__':
    main(sys.argv[1])