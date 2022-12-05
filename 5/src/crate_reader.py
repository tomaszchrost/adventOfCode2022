import os
from instruction import Instruction


class CrateReader:

    def __init__(self, data_source):
        self.crates = None
        self.instructions = None
        self.data_source = data_source

    @staticmethod
    def split_crates_and_instructions(crates_and_instructions):
        split_at = crates_and_instructions.index('')
        return crates_and_instructions[:split_at], crates_and_instructions[split_at + 1:]

    @staticmethod
    def _format_file(lines):
        formatted_crates_and_instructions = [line.replace('\n', '') for line in lines]
        return formatted_crates_and_instructions

    @staticmethod
    def _format_crates(lines):
        # probably should set to matrix and transpose but oh well
        # format out of syntax including square brackets
        formatted_crates = []
        lines = lines[:-1]
        crate_stack_count = 0
        for line in lines:
            meaningful_characters = line[1::4]
            # last value is number
            formatted_line = [None if char == ' ' else char for char in meaningful_characters]
            formatted_crates.append(formatted_line)
            if crate_stack_count < len(formatted_line):
                crate_stack_count = len(formatted_line)
                for i in range(len(formatted_crates) - 1):
                    if len(formatted_crates[i]) < crate_stack_count:
                        formatted_crates[i].extend([None] * (crate_stack_count - len(formatted_crates[i])))

        # now create arrays of each stack, rather arrays of each crate at height

        crate_heights = formatted_crates
        stack_count = len(formatted_crates[0])
        crate_stacks = []
        for i in range(stack_count):
            crate_stacks.append([])

        for crate_height in crate_heights:
            for i in range(stack_count):
                if crate_height[i] is not None:
                    crate_stacks[i].append(crate_height[i])

        # reverse for it's a fifo structure, more readable later
        for crate_stack in crate_stacks:
            crate_stack.reverse()

        return crate_stacks

    @staticmethod
    def _format_instructions(lines):
        formatted_instructions = []
        for line in lines:
            split_line = line.split(' ')
            instruction = Instruction(int(split_line[1]), int(split_line[3]) - 1, int(split_line[5]) - 1)
            formatted_instructions.append(instruction)
        return formatted_instructions

    def _read_file(self):
        with open(self.data_source, 'r') as f:
            crates_and_instructions = f.readlines()
        return crates_and_instructions

    def _init_crates(self, crate_array):
        self.crates = self._format_crates(crate_array)

    def _init_instructions(self, instruction_array):
        self.instructions = self._format_instructions(instruction_array)

    def _init_crates_and_instructions(self, crates_and_instructions):
        crates, instructions = self.split_crates_and_instructions(crates_and_instructions)
        self._init_crates(crates)
        self._init_instructions(instructions)

    def setup_crates_and_instructions(self):
        lines = self._read_file()
        formatted_lines = self._format_file(lines)
        self._init_crates_and_instructions(formatted_lines)
