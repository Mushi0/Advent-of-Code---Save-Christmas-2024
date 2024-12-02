import sys
import time
import numpy as np

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        raw_data = f.read().splitlines()
    
    def check_safe(this_line):
        diff = this_line[1:] - this_line[:-1]
        if not (np.all(diff > 0) or np.all(diff < 0)):
            return False
        
        diff_abs = np.abs(diff)
        if not (np.max(diff_abs) <= 3 and np.min(diff_abs) >= 1):
            return False

        return True

    safe_reports = 0
    for line in raw_data:
        new_line = np.array([int(e) for e in line.split(' ')])

        if check_safe(new_line):
            safe_reports += 1
            continue

        # remove one element from new_line and check again
        for i in range(len(new_line)):
            if check_safe(np.delete(new_line, i)):
                safe_reports += 1
                break
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'{safe_reports} reports are safe. ')

if __name__ == '__main__':
    main(sys.argv[1])