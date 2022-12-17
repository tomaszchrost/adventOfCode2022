from typing import Set


class Valve:
    def __init__(self, name, flow_rate):
        self.name = name
        self.flow_rate = flow_rate
        self.leads_to = []
        self.distance_from = {}

    def add_valve_connection(self, valve):
        self.leads_to.append(valve)

    def init_distance_from(self, valves):
        distances = {}
        for valve in valves:
            if valve == self:
                distances[valve] = [0, False]
            else:
                distances[valve] = [float('inf'), False]

        while True:
            min_distance = float('inf')
            min_key = None
            for key in distances:
                if distances[key][0] < min_distance and not distances[key][1]:
                    min_distance = distances[key][0]
                    min_key = key
            if min_distance == float('inf'):
                break
            else:
                for valve in min_key.leads_to:
                    distances[valve][0] = min(distances[valve][0], distances[min_key][0] + 1)
                distances[min_key][1] = True
        distance_from = {}
        for key in distances:
            distance_from[key] = distances[key][0]
        self.distance_from = distance_from


class ProboscideaVolcanium:
    def __init__(self, valves):
        self.valves = valves
        self.starting_valve = self.get_starting_valve()
        self.non_zero_valves = self.get_non_zero_valves()
        for valve in self.valves:
            valve.init_distance_from(self.valves)

    def _switch_valve(self,
                      from_valve: Valve,
                      valve: Valve,
                      unvisited_valves: Set[Valve],
                      time_left: int,
                      pressure_released: int):
        time_left += -(from_valve.distance_from[valve] + 1)
        if time_left < 0:
            return pressure_released
        unvisited_valves = unvisited_valves.copy()
        unvisited_valves.remove(valve)
        pressure_released += time_left * valve.flow_rate
        if not unvisited_valves:
            return pressure_released

        max_value = -1
        for valve_to_switch in unvisited_valves:
            value = self._switch_valve(valve, valve_to_switch, unvisited_valves, time_left, pressure_released)
            if value > max_value:
                max_value = value
        return max_value

    def _recursive_get_max_pressure(self, time_left: int):
        return max(
            (self._switch_valve(self.starting_valve, valve, set(self.non_zero_valves), time_left, 0) for valve in self.non_zero_valves))

    def get_non_zero_valves(self):
        non_zero_valves = set()
        for valve in self.valves:
            if valve.flow_rate > 0:
                non_zero_valves.add(valve)
        return non_zero_valves

    def get_starting_valve(self):
        for valve in self.valves:
            if valve.name == 'AA':
                return valve

    def get_max_pressure(self):
        return self._recursive_get_max_pressure(30)

    def get_max_pressure_with_elephant(self):
        return
