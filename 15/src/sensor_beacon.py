from typing import List


class Coordinates:
    __slots__ = 'x', 'y'

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


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

    def get_cannot_be_x_coordinates_for_y(self, y, include_other_beacons=False, min_x=None, max_x=None):
        cannot_be_beacon = set()

        for sensor_beacon in self.sensor_beacons:
            y_distance = abs(sensor_beacon.sensor.coordinates.y - y)
            y_intersection_at = sensor_beacon.distance - y_distance
            if y_intersection_at >= 0:
                start_x = sensor_beacon.sensor.coordinates.x - y_intersection_at
                end_x = sensor_beacon.sensor.coordinates.x + y_intersection_at + 1
                for x in range(start_x, end_x):
                    if min_x is not None and x < min_x:
                        continue
                    if max_x is not None and x > max_x:
                        continue
                    if x not in cannot_be_beacon:
                        cannot_be_beacon.add(x)

        if not include_other_beacons:
            for sensor_beacon in self.sensor_beacons:
                beacon = sensor_beacon.beacon
                if beacon.coordinates.y == y and beacon.coordinates.x in cannot_be_beacon:
                    cannot_be_beacon.remove(beacon.coordinates.x)

        return cannot_be_beacon

    def cannot_contain_beacon_position_count(self, y):
        cannot_be_beacon = self.get_cannot_be_x_coordinates_for_y(y)
        return len(cannot_be_beacon)

    def get_tuning_frequency(self, min_range=0, max_range=4000000):
        possible_coordinates = {}
        for sensor_beacon in self.sensor_beacons:
            x = sensor_beacon.sensor.coordinates.x
            y = sensor_beacon.sensor.coordinates.y
            for distance in range(sensor_beacon.distance + 1, sensor_beacon.distance + 3):
                for i in range(distance):
                    coordinates_array = [Coordinates(x + distance - i, y + i),
                                         Coordinates(x - distance + i, y - i),
                                         Coordinates(x + i, y + distance - i),
                                         Coordinates(x - i, y - distance + i)]

                    for coordinates in coordinates_array:
                        if coordinates in possible_coordinates:
                            possible_coordinates[coordinates] += 1
                        else:
                            possible_coordinates[coordinates] = 1

        for key in possible_coordinates:
            if possible_coordinates[key] >= 2 and min_range <= key.x <= max_range and min_range <= key.y <= max_range:
                valid_coordinates = True
                for sensor_beacon in self.sensor_beacons:
                    local_distance = key.distance(sensor_beacon.sensor.coordinates)
                    if local_distance <= sensor_beacon.distance:
                        valid_coordinates = False
                        break
                if valid_coordinates:
                    return key.x * 4000000 + key.y
