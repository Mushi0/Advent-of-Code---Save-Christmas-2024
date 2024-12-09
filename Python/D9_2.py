import sys
import time

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        raw_data = f.read()
    
    file_sizes = []
    free_sizes = []
    for i in range(int(len(raw_data) / 2)):
        file_sizes.append((i, int(raw_data[2*i])))
        free_sizes.append(int(raw_data[2*i + 1]))
    if len(raw_data)%2 == 1:
        file_sizes.append((i + 1, int(raw_data[-1])))
        free_sizes.append(0)
    nb_files = len(file_sizes)

    # move blocks
    for file_id in range(nb_files - 1, -1, -1):
        for i in range(nb_files):
            if file_sizes[i][0] == file_id:
                break
        file_size = file_sizes[i][1]
        for j in range(i):
            free_space = free_sizes[j]
            if free_space >= file_size:
                if i - j == 1:
                    free_sizes[j] = 0
                    free_sizes[j + 1] = free_sizes[j + 1] + file_size
                else:
                    free_sizes = free_sizes[:j] + [0, free_space - file_size] + free_sizes[j + 1:i - 1] + [free_sizes[i - 1] + file_size + free_sizes[i]] + free_sizes[i + 1:]
                    file_sizes = file_sizes[:j + 1] + [file_sizes[i]] + file_sizes[j + 1:i] + file_sizes[i + 1:]
                break
    
    # create files
    files = []
    for i in range(nb_files):
        file_id = file_sizes[i][0]
        file_size = file_sizes[i][1]
        free_size = free_sizes[i]
        for _ in range(file_size):
            files.append(file_id)
        for _ in range(free_size):
            files.append(0)

    # calculate checksum
    checksum = 0
    for i, file in enumerate(files):
        checksum += i * file
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The filesystem checksum is: {checksum}. ')

if __name__ == '__main__':
    main(sys.argv[1])