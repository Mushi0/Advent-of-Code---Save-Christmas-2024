import sys
import time
import numpy as np

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        raw_data = f.read().splitlines()

    safe_reports = 0
    for line in raw_data:
        new_line = np.array([int(e) for e in line.split(' ')])

        diff = new_line[1:] - new_line[:-1]
        if not (np.all(diff > 0) or np.all(diff < 0)):
            continue
        
        diff_abs = np.abs(diff)
        if not (np.max(diff_abs) <= 3 and np.min(diff_abs) >= 1):
            continue
        
        safe_reports += 1
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'{safe_reports} reports are safe. ')

if __name__ == '__main__':
    main(sys.argv[1])