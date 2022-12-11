import math

from monkey import Monkey


class KeepAway:
    def __init__(self):
        self.monkeys = []
        self.lcm = None

    def calculate_lcm(self):
        self.lcm = math.lcm(*(monkey.true_when_divisible_by for monkey in self.monkeys))

    def do_round(self, monkeys_get_bored):
        for monkey in self.monkeys:
            items: list = monkey.items.copy()
            for i in range(len(items)):
                item = items[i] % self.lcm
                item = monkey.inspect(item)
                if monkeys_get_bored:
                    item = monkey.get_bored(item)
                monkey_i = monkey.throwing_to(item)
                self.monkeys[monkey_i].items.append(item)
            monkey.items = []

    def get_monkey_business(self, rounds=20, monkeys_get_bored=True):
        for _ in range(rounds):
            self.do_round(monkeys_get_bored)
        inspections = [monkey.inspection_count for monkey in self.monkeys]
        max_value = max(inspections)
        inspections.remove(max_value)
        second_max_value = max(inspections)
        return max_value * second_max_value
