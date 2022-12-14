import os

from height_map import HeightMap

RESOURCES = os.path.abspath('resources/')
FILE_PATH = os.path.join(RESOURCES, 'height_map.dat')

class DataReader:

    @staticmethod
    def read_lines(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        return lines

    @staticmethod
    def format_lines_into_data(lines):
        height_map = HeightMap()
        height_map.height_array = []
        for line in lines:
            x_array = []
            line = line.strip()
            for character in line:
                if character == 'S':
                    ord_value = ord('a') - 1
                    height_map.start_x = len(x_array) + 1
                    height_map.start_y = len(height_map.height_array) + 1
                elif character == 'E':
                    ord_value = ord('z') + 1
                    height_map.end_x = len(x_array) + 1
                    height_map.end_y = len(height_map.height_array) + 1
                else:
                    ord_value = ord(character)
                x_array.append(ord_value)
            height_map.height_array.append(x_array)
        return height_map

    @staticmethod
    def get_data(file_path=FILE_PATH):
        lines = DataReader.read_lines(file_path)
        data = DataReader.format_lines_into_data(lines)
        return data
