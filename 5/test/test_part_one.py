import os

import crate_reader
import crate_controller
import utils

SUPPLIES_TEST_FILE_PATH = os.path.join('resources/test_data.dat')


def test_part_one():
    reader = crate_reader.CrateReader(SUPPLIES_TEST_FILE_PATH)
    reader.setup_crates_and_instructions()
    controller = crate_controller.CrateController(reader.crates, reader.instructions)

    controller.execute_instructions_part_one()
    assert utils.get_solution_from_crate_controller(controller) == 'CMZ'
