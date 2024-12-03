import sys
import time
import re

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        raw_data = f.read().splitlines()

    mult_sum = 0
    for line in raw_data:
        # use regular expression to find mul(dd,dd) where dd are integers of 1-3 digits
        mults = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
        
        for mult in mults:
            mult_sum += int(mult[0]) * int(mult[1])
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of the multiplications is: {mult_sum}. ')

if __name__ == '__main__':
    main(sys.argv[1])