import utils


def main():
    commands = utils.get_commands(utils.ACTIONS_FILE_PATH)
    rope_bridge = utils.RopeBridge()
    rope_bridge.execute_commands(commands)
    print(rope_bridge.get_locations_visited_count())


if __name__ == '__main__':
    main()
