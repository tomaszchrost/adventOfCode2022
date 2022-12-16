from typing import List


class Coordinates:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Sensor:
    def __init__(self, coordinates: Coordinates):
        self.coordinates = coordinates


class Beacon:
    def __init__(self, coordinates: Coordinates):
        self.coordinates = coordinates


class SensorBeacon:
    def __init__(self, sensor, beacon):
        self.sensor = sensor
        self.beacon = beacon
        self.distance = self.sensor.coordinates.distance(beacon.coordinates)

class ArrangementMapInfo:
    def __init__(self, coordinates: Coordinates, sensor: Sensor, beacon: Beacon):
        self.coordinates = coordinates
        self.sensor = sensor
        self.beacon = beacon
        self.can_contain_beach = True
class SensorBeaconArrangement:
    def __init__(self, sensor_beacons: List[SensorBeacon]):
        self.sensor_beacons = sensor_beacons
        self.arrange_map = None
        max_x_sensor = max(sensor_beacon.sensor.coordinates.x for sensor_beacon in self.sensor_beacons)
        max_x_beacon = max(sensor_beacon.beacon.coordinates.x for sensor_beacon in self.sensor_beacons)
        self.max_x = max(max_x_sensor, max_x_beacon)
        min_x_sensor = min(sensor_beacon.sensor.coordinates.x for sensor_beacon in self.sensor_beacons)
        min_x_beacon = min(sensor_beacon.beacon.coordinates.x for sensor_beacon in self.sensor_beacons)
        self.min_x = min(min_x_sensor, min_x_beacon)

    def can_contain_beacon(self, coordinates: Coordinates):
        for sensor_beacon in self.sensor_beacons:
            local_distance = coordinates.distance(sensor_beacon.sensor.coordinates)
            if (local_distance <= sensor_beacon.distance
                    and coordinates != sensor_beacon.beacon.coordinates):
                return False
        return True

    def cannot_contain_beacon_position_count(self, y):
        cannot_contain_count = 0
        for i in range(self.min_x, self.max_x + 1):
            if not self.can_contain_beacon(Coordinates(i, y)):
                cannot_contain_count += 1
        current_x = self.max_x + 1
        while True:
            if not self.can_contain_beacon(Coordinates(current_x, y)):
                cannot_contain_count += 1
                current_x += 1
            else:
                break
        current_x = self.min_x - 1
        while True:
            if not self.can_contain_beacon(Coordinates(current_x, y)):
                cannot_contain_count += 1
                current_x += -1
            else:
                break
        return cannot_contain_count

