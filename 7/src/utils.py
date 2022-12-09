import os
import enum

RESOURCES = os.path.abspath('resources/')
HISTORY_FILE_PATH = os.path.join(RESOURCES, 'history.dat')

class Commands(enum.Enum):
    LS = 0
    CD = 1


class Directory:
    def __init__(self):
        self.directories = []
        self.prev_directory = None
        self.files = []
        self.name = None


class File:
    def __init__(self):
        self.size = None
        self.name = None


class FileSystem:

    TOTAL_SIZE = 70000000
    FREE_SPACE_NEEDED = 30000000

    def __init__(self):
        root_dir = Directory()
        root_dir.name = None
        root_dir.prev_directory = None
        self.root_dir: Directory = root_dir
        self.current_dir: Directory = None
        self.dir_size_count = 0
        self.directory_size_to_remove = 0

    def execute_commands(self, commands):
        command_executor = CommandExecutor()
        command_executor.file_system = self
        command_executor.commands = commands
        command_executor.execute_commands()

    def _get_directory_size(self, directory: Directory):
        dir_sizes = [self._get_directory_size(directory) for directory in directory.directories]

        this_dir_size = sum(dir_sizes) + sum((file.size for file in directory.files))
        return this_dir_size

    def _calculate_directories_smaller_than(self, size, directory: Directory):
        dir_sizes = [self._calculate_directories_smaller_than(size, directory) for directory in directory.directories]

        this_dir_size = sum(dir_sizes) + sum((file.size for file in directory.files))
        if this_dir_size < size:
            self.dir_size_count += this_dir_size
        return this_dir_size

    def _calculate_smallest_directory_to_free(self, size, directory: Directory):
        dir_sizes = [self._calculate_smallest_directory_to_free(size, directory) for directory in directory.directories]

        this_dir_size = sum(dir_sizes) + sum((file.size for file in directory.files))
        if size < this_dir_size < self.directory_size_to_remove:
            self.directory_size_to_remove = this_dir_size
        return this_dir_size

    def get_directories_smaller_than(self, size):
        self.dir_size_count = 0
        self._calculate_directories_smaller_than(size, self.root_dir)
        return self.dir_size_count

    def get_total_size_of_dirs(self):
        return self._get_directory_size(self.root_dir)

    def get_smallest_directory_to_free(self):
        total_size = self.get_total_size_of_dirs()
        free_space = self.TOTAL_SIZE - total_size
        self.directory_size_to_remove = total_size
        space_needed = self.FREE_SPACE_NEEDED - free_space
        self._calculate_smallest_directory_to_free(space_needed, self.root_dir)
        return self.directory_size_to_remove

class CommandExecutor:
    COMMAND_CHARACTER = '$'

    def __init__(self):
        self.file_system: FileSystem = None
        self.commands = None
        self.cd_special_characters = self.init_cd_special_characters()

    @staticmethod
    def directory_exists(name, from_dir: Directory):
        return name in (directory.name for directory in from_dir.directories)

    @staticmethod
    def create_file(name, size, from_dir: Directory):
        new_file = File()
        new_file.name = name
        new_file.size = int(size)
        from_dir.files.append(new_file)

    @staticmethod
    def create_directory(name, from_dir: Directory):
        new_directory = Directory()
        new_directory.name = name
        new_directory.prev_directory = from_dir
        from_dir.directories.append(new_directory)

    def init_cd_special_characters(self):
        return {'..': self.move_back_dir, '/': self.move_to_root_dir}

    def move_back_dir(self):
        self.file_system.current_dir = self.file_system.current_dir.prev_directory

    def move_to_dir(self, name, from_dir: Directory):
        for directory in from_dir.directories:
            if directory.name == name:
                self.file_system.current_dir = directory

    def move_to_root_dir(self):
        self.file_system.current_dir = self.file_system.root_dir

    def execute_commands(self):
        for line in self.commands:
            line_list = line.split()
            is_command = line_list[0] == self.COMMAND_CHARACTER
            if is_command:
                current_command = Commands[line_list[1].upper()]
                if current_command == Commands.CD:
                    command_detail = line_list[2]
                    special_command = self.cd_special_characters.get(command_detail)
                    if special_command is not None:
                        special_command()
                    else:
                        self.move_to_dir(command_detail, self.file_system.current_dir)
                elif current_command == Commands.LS:
                    current_command = Commands.LS
            else:
                # current command is always ls
                item_type_or_size = line_list[0]
                item_name = line_list[1]

                if item_type_or_size == 'dir':
                    self.create_directory(item_name, self.file_system.current_dir)
                else:
                    self.create_file(item_name, item_type_or_size, self.file_system.current_dir)


def read_file(file_path):
    with open(file_path, 'r') as f:
        history = f.readlines()

    return [line.strip() for line in history]
