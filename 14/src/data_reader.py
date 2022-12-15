import os
import scanner
import terrain

RESOURCES = os.path.abspath('resources/')
FILE_PATH = os.path.join(RESOURCES, 'scans.dat')


class DataReader:

    @staticmethod
    def read_lines(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        return lines

    @staticmethod
    def format_lines_into_data(lines):
        scan = scanner.Scanner()
        lines_to_scan = []

        # get coords from lines
        for line in lines:
            line = line.strip().split(' -> ')
            coords = []
            for line_item in line:
                split_item = line_item.split(',')
                coor = scanner.Coordinate(int(split_item[0]), int(split_item[1]))
                coords.append(coor)
            lines_to_scan.append(coords)

        # set up cave as air
        max_x = max(map(lambda line: max(coord.x for coord in line), lines_to_scan)) + 1
        max_y = max(map(lambda line: max(coord.y for coord in line), lines_to_scan)) + 1
        rock_structure = []

        for i in range(max_y):
            rock_structure.append([])
            for j in range(max_x):
                rock_structure[i].append(terrain.Terrain.AIR)

        for line in lines_to_scan:
            for i in range(1, len(line)):
                if line[i-1].x != line[i].x:
                    starting_i = min(line[i-1].x, line[i].x)
                    difference = abs(line[i-1].x - line[i].x)
                    for x in range(starting_i, starting_i + difference + 1):
                        rock_structure[line[i].y][x] = terrain.Terrain.ROCK
                else:
                    starting_i = min(line[i-1].y, line[i].y)
                    difference = abs(line[i-1].y - line[i].y)
                    for y in range(starting_i, starting_i + difference + 1):
                        rock_structure[y][line[i].x] = terrain.Terrain.ROCK
        scan.rock_structure = rock_structure
        return scan






    @staticmethod
    def get_data(file_path=FILE_PATH):
        lines = DataReader.read_lines(file_path)
        data = DataReader.format_lines_into_data(lines)
        return data
