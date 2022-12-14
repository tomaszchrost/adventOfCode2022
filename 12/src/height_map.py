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
        minimum = -1
        min_x = -1
        min_y = -1
        for y in range(len(self.steps)):
            for x in range(len(self.steps[0])):
                if minimum == -1:
                    minimum = self.steps[y][x]
                    min_x = x
                    min_y = y
                if not self.visited[y][x] and self.steps[y][x] != -1 and self.steps[y][x] < minimum:
                    minimum = self.steps[y][x]
                    min_x = x
                    min_y = y

        return min_x, min_y

    def valid_index(self, x, y):
        return len(self.steps) > y > -1 and len(self.steps[0]) > x > -1

    @staticmethod
    def can_reach(current_height, to_reach_height):
        return current_height in (to_reach_height - 1, to_reach_height, to_reach_height + 1)

    def update_steps(self, x, y):
        if self.valid_index(x + 1, y) and self.can_reach(self.height_array[y][x], self.height_array[y][x + 1]):
            self.steps[y][x + 1] = min(self.steps[y][x + 1], self.steps[y][x] + 1)
        if self.valid_index(x - 1, y) and self.can_reach(self.height_array[y][x], self.height_array[y][x - 1]):
            self.steps[y][x - 1] = min(self.steps[y][x - 1], self.steps[y][x] + 1)

        if self.valid_index(x, y + 1) and self.can_reach(self.height_array[y][x], self.height_array[y + 1][x]):
            self.steps[y + 1][x] = min(self.steps[y + 1][x], self.steps[y][x] + 1)
        if self.valid_index(x, y - 1) and self.can_reach(self.height_array[y][x], self.height_array[y - 1][x]):
            self.steps[y - 1][x] = min(self.steps[y - 1][x], self.steps[y][x] + 1)

    def dijkstras(self):
        steps = []
        visited = []
        for i in range(len(self.height_array)):
            steps.append([-1] * len(self.height_array[0]))
        for i in range(len(self.height_array)):
            visited.append([False] * len(self.height_array[0]))

        steps[self.start_y][self.start_x] = 0
        x = self.start_x
        y = self.start_y

        while x != -1:
            visited[y][x] = True
            self.update_steps(x, y)
            x, y = self.get_min()

        return self.steps[self.end_y][self.end_x]
