import sys
import time
from functools import lru_cache

@lru_cache(maxsize=None)
def rules(this_number):
    # if this_number is 0, return 1
    str_num = str(this_number)
    length = len(str_num)
    if this_number == 0:
        return [1]
    # if this_number has even digits, divide the number into two parts return the list of two numbers
    elif length % 2 == 0:
        half_length = length // 2
        return [int(str_num[:half_length]), int(str_num[half_length:])]
    # otherwise, return this_number * 2024
    else:
        return [this_number * 2024]

def one_blink(stones):
    new_stones = []
    for stone in stones:
        new_stones.extend(rules(stone))
    return new_stones

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        raw_data = f.read()

    stones = [int(e) for e in raw_data.split(' ')]

    for _ in range(25):
        stones = one_blink(stones)

    nb_stones = len(stones)
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'After blinking 25 times, there are: {nb_stones} stones. ')

if __name__ == '__main__':
    main(sys.argv[1])