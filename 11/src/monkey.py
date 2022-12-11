import math


class Monkey:

    def __init__(self,
                 starting_item_list,
                 operation,
                 true_when_divisible_by,
                 throw_true,
                 throw_false):
        self.items = starting_item_list
        self.operation = operation
        self.true_when_divisible_by = true_when_divisible_by
        self.throw_true = throw_true
        self.throw_false = throw_false
        self.inspection_count = 0

    def inspect(self, item):
        old = item
        new = self.operation(old)
        self.inspection_count += 1
        return new

    @staticmethod
    def get_bored(item):
        return math.floor(item // 3)

    def throwing_to(self, item):
        if item % self.true_when_divisible_by == 0:
            return self.throw_true
        else:
            return self.throw_false
