import data_reader


def main():
    data = data_reader.DataReader().get_data('resources/valves.dat')
    print(data.get_max_pressure_with_elephant())


if __name__ == '__main__':
    main()
