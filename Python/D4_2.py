import sys
import time

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        raw_data = f.read().splitlines()
    
    search_words = ['MAS', 'SAM']

    # find any matrix with [[M.S][.A.][M.S]] or [[.S.M][A..][.M.S]]
    xmas_count = 0
    for i, line in enumerate(raw_data):
        for j, letter in enumerate(line):
            if i >= 1 and j >= 1 and i <= len(raw_data) - 2 and j <= len(line) - 2:
                word_1 = raw_data[i-1][j-1] + letter + raw_data[i+1][j+1]
                word_2 = raw_data[i-1][j+1] + letter + raw_data[i+1][j-1]
                if (word_1 == word_2 or word_1 == word_2[::-1]) and \
                    word_2 in search_words:
                    xmas_count += 1
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'{xmas_count} X-MAS appear. ')

if __name__ == '__main__':
    main(sys.argv[1])