import sys
import time

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        raw_data = f.read().splitlines()
    
    # check whether test_value can be calculated with all the operands
    # following the order, and using only add and multiply
    def calculate(current_value, operands):
        if len(operands) == 0:
            return current_value == test_value
        else:
            return calculate(current_value + operands[0], operands[1:]) or \
                calculate(current_value * operands[0], operands[1:])

    total_calibration = 0
    for line in raw_data:
        [test_value, operands] = line.split(': ')
        test_value = int(test_value)
        operands = list(map(int, operands.split(' ')))
        
        if calculate(0, operands):
            total_calibration += test_value
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The total calibration result is: {total_calibration}. ')

if __name__ == '__main__':
    main(sys.argv[1])