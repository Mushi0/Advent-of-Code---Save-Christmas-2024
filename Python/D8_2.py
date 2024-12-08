import sys
import time

def main(DATA_INPUT):
    start_time = time.time()

    with open(DATA_INPUT) as f:
        raw_data = f.read().splitlines()
    
    nb_rows = len(raw_data)
    nb_cols = len(raw_data[0])
    
    antennas = {}
    for i,line in enumerate(raw_data):  
        for j, location in enumerate(line):
            if location == '.':
                continue
            if location in antennas.keys():
                antennas[location].append([i, j])
            else:
                antennas[location] = [[i, j]]
    
    antinodes = set()
    for locations in antennas.values():
        n = len(locations)
        for i in range(n - 1):
            for j in range(i + 1, n):
                location_1 = locations[i]
                location_2 = locations[j]

                diff_0 = location_2[0] - location_1[0]
                diff_1 = location_2[1] - location_1[1]

                possible_loc_1 = tuple(location_1)
                possible_loc_2 = tuple(location_2)

                while possible_loc_1[0] >= 0 and possible_loc_1[0] < nb_rows and\
                    possible_loc_1[1] >= 0 and possible_loc_1[1] < nb_cols:
                    antinodes.add(possible_loc_1)
                    possible_loc_1 = (possible_loc_1[0] - diff_0, possible_loc_1[1] - diff_1)
                
                while possible_loc_2[0] >= 0 and possible_loc_2[0] < nb_rows and\
                    possible_loc_2[1] >= 0 and possible_loc_2[1] < nb_cols:
                    antinodes.add(possible_loc_2)
                    possible_loc_2 = (possible_loc_2[0] + diff_0, possible_loc_2[1] + diff_1)
    
    antinode_count = len(antinodes)
    
    print(f'Time taken: {(time.time() - start_time):.3e}s')
    print(f'{antinode_count} unique locations contain an antinode. ')

    for i, line in enumerate(raw_data):
        raw_data[i] = list(line)
    for location in antinodes:
        raw_data[location[0]][location[1]] = '#'
    for line in raw_data:
        for element in line:
            print(element, end = '')
        print()

if __name__ == '__main__':
    main(sys.argv[1])