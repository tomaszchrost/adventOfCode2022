from instruction import Instruction


class CrateController:

    def __init__(self, crates: list, instructions: list[Instruction]):
        self.crates = crates
        self.instructions = instructions

    def execute_instructions_part_one(self):
        for instruction in self.instructions:
            crates_to_move = list(self.crates[instruction.move_from][0-instruction.count:])
            crates_to_move.reverse()
            self.crates[instruction.move_to].extend(crates_to_move)
            self.crates[instruction.move_from] = self.crates[instruction.move_from][:0-instruction.count]

    def execute_instructions_part_two(self):
        for instruction in self.instructions:
            crates_to_move = self.crates[instruction.move_from][0-instruction.count:]
            self.crates[instruction.move_to].extend(crates_to_move)
            self.crates[instruction.move_from] = self.crates[instruction.move_from][:0-instruction.count]