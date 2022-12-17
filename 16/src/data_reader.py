from proboscidea_volcanium import *


class DataReader:

    @staticmethod
    def read_lines(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        return lines

    @staticmethod
    def format_lines_into_data(lines):
        valves = []
        to_add_valves = []
        for line in lines:
            line = line.strip()
            name = line.split(' ')[1]
            flow_rate = int(line.split('=')[1].split(';')[0])
            valves.append(Valve(name, flow_rate))
            split_lines = line.split(', ')
            to_add = split_lines[1:]
            to_add.append(split_lines[0].split(' ')[-1])
            to_add_valves.append(to_add)

        for i in range(len(valves)):
            for to_add in to_add_valves[i]:
                for valve in valves:
                    if to_add == valve.name:
                        valves[i].add_valve_connection(valve)

        return ProboscideaVolcanium(valves)

    @staticmethod
    def get_data(file_path):
        lines = DataReader.read_lines(file_path)
        data = DataReader.format_lines_into_data(lines)
        return data
