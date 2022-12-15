import os
import signals

RESOURCES = os.path.abspath('resources/')
FILE_PATH = os.path.join(RESOURCES, 'signals.dat')


class DataReader:

    @staticmethod
    def read_lines(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        return lines

    @staticmethod
    def format_lines_into_data(lines):
        stripped_lines = []
        signal_pairs = []
        for line in lines:
            stripped_lines.append(line.strip())

        for i in range(0, len(lines), 3):
            signal_pairs.append((eval(stripped_lines[i]), eval(stripped_lines[i+1])))
        return signal_pairs

    @staticmethod
    def get_data(file_path=FILE_PATH):
        lines = DataReader.read_lines(file_path)
        data = DataReader.format_lines_into_data(lines)
        return data

    @staticmethod
    def get_data_as_one_list(file_path=FILE_PATH):
        lines = DataReader.read_lines(file_path)
        data = DataReader.format_lines_into_data(lines)
        one_list = []
        for data_item in data:
            one_list.append(signals.Signal(data_item[0]))
            one_list.append(signals.Signal(data_item[1]))
        return one_list
