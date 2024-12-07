import sys
import time
import copy
from tqdm import tqdm

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
                start_position = [i, j]

    def find_loop(this_data_dic_hor, this_data_dic_ver):
        loop = False
        this_position = start_position.copy()
        visited_turns = {0:[this_position.copy()], 1:[], 2:[], 3:[]}
        this_dir = 0
        while this_position[0] > 0 and this_position[0] < (nb_rows - 1) and \
            this_position[1] > 0 and this_position[1] < (nb_cols - 1):
            if this_dir == 0:
                closest_obstacle = -1
                for obstacle in this_data_dic_ver[this_position[1]]:
                    if obstacle < this_position[0] and obstacle > closest_obstacle:
                        closest_obstacle = obstacle
                this_position[0] = closest_obstacle + 1
                if this_position in visited_turns[1]:
                    loop = True
                    break
                visited_turns[1].append(this_position.copy())
            elif this_dir == 1:
                closest_obstacle = nb_cols
                for obstacle in this_data_dic_hor[this_position[0]]:
                    if obstacle > this_position[1] and obstacle < closest_obstacle:
                        closest_obstacle = obstacle
                this_position[1] = closest_obstacle - 1
                if this_position in visited_turns[2]:
                    loop = True
                    break
                visited_turns[2].append(this_position.copy())
            elif this_dir == 2:
                closest_obstacle = nb_rows
                for obstacle in this_data_dic_ver[this_position[1]]:
                    if obstacle > this_position[0] and obstacle < closest_obstacle:
                        closest_obstacle = obstacle
                this_position[0] = closest_obstacle - 1
                if this_position in visited_turns[3]:
                    loop = True
                    break
                visited_turns[3].append(this_position.copy())
            elif this_dir == 3:
                closest_obstacle = -1
                for obstacle in this_data_dic_hor[this_position[0]]:
                    if obstacle < this_position[1] and obstacle > closest_obstacle:
                        closest_obstacle = obstacle
                this_position[1] = closest_obstacle + 1
                if this_position in visited_turns[0]:
                    loop = True
                    break
                visited_turns[0].append(this_position.copy())
            this_dir = (this_dir + 1) % 4
        return loop
    
    position_loop = 0
    for i in tqdm(range(nb_rows)):
        for j in tqdm(range(nb_cols)):
            new_data_dic_hor = copy.deepcopy(data_dic_hor)
            new_data_dic_ver = copy.deepcopy(data_dic_ver)
            if data_matrix[i][j] == '#' or data_matrix[i][j] == '^':
                continue
            new_data_dic_hor[i].add(j)
            new_data_dic_ver[j].add(i)
            position_loop += find_loop(new_data_dic_hor, new_data_dic_ver)
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'{position_loop} distinct positions can be chosen as an obstacle to create a loop. ')

if __name__ == '__main__':
    main(sys.argv[1])