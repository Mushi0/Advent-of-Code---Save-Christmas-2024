import sys
import time

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        raw_data = f.read().splitlines()
    
    search_words = ['XMAS', 'SAMX']

    # find any XMAS in the raw_data matrix horizontally, vertically, and diagonally, in order or backwards
    xmas_count = 0
    for i, line in enumerate(raw_data):
        for j, letter in enumerate(line):
            if j <= len(raw_data) - 4 and line[j:j+4] in search_words:
                xmas_count += 1
            
            if i <= len(line) - 4 and \
                letter + raw_data[i+1][j] + raw_data[i+2][j] + raw_data[i+3][j] in search_words:
                xmas_count += 1
            
            if i <= len(raw_data) - 4 and j <= len(line) - 4 and \
                letter + raw_data[i+1][j+1] + raw_data[i+2][j+2] + raw_data[i+3][j+3] in search_words:
                xmas_count += 1
            
            if i >= 3 and j <= len(line) - 4 and \
                letter + raw_data[i-1][j+1] + raw_data[i-2][j+2] + raw_data[i-3][j+3] in search_words:
                xmas_count += 1
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'{xmas_count} XMAS appear. ')

if __name__ == '__main__':
    main(sys.argv[1])