import utils


def main():
    commands = utils.read_file(utils.HISTORY_FILE_PATH)
    file_system = utils.FileSystem()
    file_system.execute_commands(commands)
    print(file_system.get_smallest_directory_to_free())


if __name__ == '__main__':
    main()
