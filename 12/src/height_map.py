class HeightMap:

    def __init__(self):
        self.height_array = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None

        self.steps = None
        self.visited = None

    def get_min(self):
        minimum = float('inf')
        min_x = -1
        min_y = -1
        for y in range(len(self.steps)):
            for x in range(len(self.steps[0])):
                if not self.visited[y][x] and self.steps[y][x] < minimum:
                    minimum = self.steps[y][x]
                    min_x = x
                    min_y = y

        return min_x, min_y

    def valid_index(self, x, y):
        return len(self.steps) > y > -1 and len(self.steps[0]) > x > -1

    @staticmethod
    def can_reach(current_height, to_reach_height, going_backwards):
        if not going_backwards:
            return current_height == to_reach_height - 1 or to_reach_height <= current_height
        else:
            return current_height == to_reach_height + 1 or to_reach_height >= current_height

    def update_steps(self, x, y, going_backwards):
        if self.valid_index(x + 1, y) and self.can_reach(self.height_array[y][x], self.height_array[y][x + 1], going_backwards):
            self.steps[y][x + 1] = min(self.steps[y][x + 1], self.steps[y][x] + 1)
        if self.valid_index(x - 1, y) and self.can_reach(self.height_array[y][x], self.height_array[y][x - 1], going_backwards):
            self.steps[y][x - 1] = min(self.steps[y][x - 1], self.steps[y][x] + 1)

        if self.valid_index(x, y + 1) and self.can_reach(self.height_array[y][x], self.height_array[y + 1][x], going_backwards):
            self.steps[y + 1][x] = min(self.steps[y + 1][x], self.steps[y][x] + 1)
        if self.valid_index(x, y - 1) and self.can_reach(self.height_array[y][x], self.height_array[y - 1][x], going_backwards):
            self.steps[y - 1][x] = min(self.steps[y - 1][x], self.steps[y][x] + 1)

    def dijkstras(self, going_backwards=False):
        self.steps = []
        self.visited = []
        for i in range(len(self.height_array)):
            self.steps.append([float('inf')] * len(self.height_array[0]))
        for i in range(len(self.height_array)):
            self.visited.append([False] * len(self.height_array[0]))

        self.steps[self.start_y][self.start_x] = 0
        x = self.start_x
        y = self.start_y

        while x != -1:
            self.update_steps(x, y, going_backwards)
            self.visited[y][x] = True
            x, y = self.get_min()

        return self.steps[self.end_y][self.end_x]

    def best_starting_location(self):
        self.start_x = self.end_x
        self.start_y = self.end_y
        self.dijkstras(True)
        min_a = float('inf')
        for y in range(len(self.steps)):
            for x in range(len(self.steps[0])):
                if self.height_array[y][x] == ord('a'):
                    min_a = min(self.steps[y][x], min_a)
        return min_a
