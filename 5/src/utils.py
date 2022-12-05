import os

RESOURCES = os.path.abspath('resources/')
SUPPLIES_FILE_PATH = os.path.join(RESOURCES, 'crates.dat')


def get_solution_from_crate_controller(crate_controller):
    return ''.join([stack[-1] for stack in crate_controller.crates])
