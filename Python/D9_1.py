import sys
import time

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        raw_data = f.read()
    
    # create the files
    files = []
    file_id = 0
    for i in range(int(len(raw_data) / 2)):
        file_size = int(raw_data[2*i])
        free_size = int(raw_data[2*i + 1])
        for _ in range(file_size):
            files.append(file_id)
        for _ in range(free_size):
            files.append(-1)
        file_id += 1
    if len(raw_data)%2 == 1:
        file_size = int(raw_data[-1])
        for _ in range(file_size):
            files.append(file_id)

    # move file blocks
    i = 0
    while i < len(files):
        if files[i] == -1:
            files[i] = files[-1]
            files.pop()
        while files[-1] == -1:
            files.pop()
        i += 1
    
    # calculate checksum
    checksum = 0
    for i, file in enumerate(files):
        checksum += i * file
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'The filesystem checksum is: {checksum}. ')

if __name__ == '__main__':
    main(sys.argv[1])