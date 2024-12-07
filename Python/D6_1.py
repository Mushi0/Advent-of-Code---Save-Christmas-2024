import sys
import time

# directions = {'^': 0, '>': 1, 'v': 2, '<': 3}

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        raw_data = f.read()
    
    data_matrix = raw_data.split('\n')
    nb_rows = len(data_matrix)
    nb_cols = len(data_matrix[0])
    data_dic_hor = {i:set() for i in range(nb_rows)}
    data_dic_ver = {i:set() for i in range(nb_cols)}
    for i in range(nb_rows):
        data_dic_hor[i] = set()
        for j in range(len(data_matrix[i])):
            if data_matrix[i][j] == '#':
                data_dic_hor[i].add(j)
                data_dic_ver[j].add(i)
            elif data_matrix[i][j] == '^':
                this_position = [i, j]
    
    data_dic_hor[7].add(6)
    data_dic_ver[6].add(7)

    count_matrix = [[0 for _ in range(nb_cols)] for _ in range(nb_rows)]
    count_matrix[this_position[0]][this_position[1]] = 1
    this_dir = 0
    while this_position[0] > 0 and this_position[0] < (nb_rows - 1) and \
        this_position[1] > 0 and this_position[1] < (nb_cols - 1):
        if this_dir == 0:
            closest_obstacle = -1
            for obstacle in data_dic_ver[this_position[1]]:
                if obstacle < this_position[0] and obstacle > closest_obstacle:
                    closest_obstacle = obstacle
            for i in range(closest_obstacle + 1, this_position[0] + 1):
                count_matrix[i][this_position[1]] = 1
            this_position[0] = closest_obstacle + 1
        elif this_dir == 1:
            closest_obstacle = nb_cols
            for obstacle in data_dic_hor[this_position[0]]:
                if obstacle > this_position[1] and obstacle < closest_obstacle:
                    closest_obstacle = obstacle
            for i in range(this_position[1], closest_obstacle):
                count_matrix[this_position[0]][i] = 1
            this_position[1] = closest_obstacle - 1
        elif this_dir == 2:
            closest_obstacle = nb_rows
            for obstacle in data_dic_ver[this_position[1]]:
                if obstacle > this_position[0] and obstacle < closest_obstacle:
                    closest_obstacle = obstacle
            for i in range(this_position[0], closest_obstacle):
                count_matrix[i][this_position[1]] = 1
            this_position[0] = closest_obstacle - 1
        elif this_dir == 3:
            closest_obstacle = -1
            for obstacle in data_dic_hor[this_position[0]]:
                if obstacle < this_position[1] and obstacle > closest_obstacle:
                    closest_obstacle = obstacle
            for i in range(closest_obstacle + 1, this_position[1] + 1):
                count_matrix[this_position[0]][i] = 1
            this_position[1] = closest_obstacle + 1
        this_dir = (this_dir + 1) % 4

        print('-----------------------')
        for i, line in enumerate(count_matrix):
            for j, e in enumerate(line):
                if e:
                    print('X', end='')
                elif data_matrix[i][j] == '#':
                    print('#', end='')
                else:
                    print('.', end='')
            print()

    position_visiited = sum(sum(e for e in line) for line in count_matrix)
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'{position_visiited} distinct positions will the guard visit. ')

    # pint map
    for i, line in enumerate(count_matrix):
        for j, e in enumerate(line):
            if e:
                print('X', end='')
            elif data_matrix[i][j] == '#':
                print('#', end='')
            else:
                print('.', end='')
        print()

if __name__ == '__main__':
    main(sys.argv[1])