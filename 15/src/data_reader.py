import os
from sensor_beacon import *

RESOURCES = os.path.abspath('resources/')
FILE_PATH = os.path.join(RESOURCES, 'beacon_sensors.dat')


class DataReader:

    @staticmethod
    def read_lines(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
        return lines

    @staticmethod
    def format_lines_into_data(lines):
        sensor_beacons = []
        for line in lines:
            line = line.strip().split('=')
            sensor = Sensor(Coordinates(int(line[1].split(',')[0]), int(line[2].split(':')[0])))
            beacon = Beacon(Coordinates(int(line[3].split(',')[0]), int(line[4])))
            sensor_beacon = SensorBeacon(sensor, beacon)
            sensor_beacons.append(sensor_beacon)
        return SensorBeaconArrangement(sensor_beacons)

    @staticmethod
    def get_data(file_path=FILE_PATH):
        lines = DataReader.read_lines(file_path)
        data = DataReader.format_lines_into_data(lines)
        return data
