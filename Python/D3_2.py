import sys
import time
import re

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        raw_data = f.read()
    
    def get_mult(this_str):
        mults = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', this_str)

        this_sum = 0
        for mult in mults:
            this_sum += int(mult[0]) * int(mult[1])
        
        return this_sum

    data_list = raw_data.split("don't()")
    mult_sum = get_mult(data_list[0])
    for sub_str in data_list[1:]:
        if 'do()' in sub_str:
            dos = sub_str.split('do()')
            for one_do in dos[1:]:
                mult_sum += get_mult(one_do)
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The sum of the multiplications is: {mult_sum}. ')

if __name__ == '__main__':
    main(sys.argv[1])