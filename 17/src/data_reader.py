from pyroclastic_flow import *


class DataReader:

    @staticmethod
    def read_lines(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        return lines

    @staticmethod
    def format_lines_into_data(lines):
        directions = []
        for character in lines[0].strip():
            if character == '>':
                directions.append(Direction.RIGHT)
            elif character == '<':
                directions.append(Direction.LEFT)
        return PyroclasticFlow(directions)

    @staticmethod
    def get_data(file_path):
        lines = DataReader.read_lines(file_path)
        data = DataReader.format_lines_into_data(lines)
        return data
