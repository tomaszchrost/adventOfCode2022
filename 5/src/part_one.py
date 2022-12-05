import crate_controller
import crate_reader
import utils


def main():
    reader = crate_reader.CrateReader(utils.SUPPLIES_FILE_PATH)
    reader.setup_crates_and_instructions()
    controller = crate_controller.CrateController(reader.crates, reader.instructions)

    controller.execute_instructions_part_one()
    print(utils.get_solution_from_crate_controller(controller))


if __name__ == '__main__':
    main()
