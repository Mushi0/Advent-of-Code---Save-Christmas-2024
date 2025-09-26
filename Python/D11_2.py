import sys
import time
from functools import lru_cache

def rules(this_number):
    # if this_number is 0, return 1
    str_num = str(this_number)
    length = len(str_num)
    if this_number == 0:
        return (1,)
    # if this_number has even digits, divide the number into two parts return the list of two numbers
    elif length % 2 == 0:
        half_length = length // 2
        return (int(str_num[:half_length]), int(str_num[half_length:]))
    # otherwise, return this_number * 2024
    else:
        return (this_number * 2024,)

@lru_cache(maxsize=None)
def one_blink(stone, blink_nb):
    new_stones = rules(stone)
    if blink_nb == 75:
        return len(new_stones)
    return sum(one_blink(s, blink_nb + 1) for s in new_stones)

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        raw_data = f.read()

    stones = (int(e) for e in raw_data.split(' '))

    nb_stones = 0
    for stone in stones:
        nb_stones += one_blink(stone, 1)
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'After blinking 25 times, there are: {nb_stones} stones. ')

if __name__ == '__main__':
    main(sys.argv[1])