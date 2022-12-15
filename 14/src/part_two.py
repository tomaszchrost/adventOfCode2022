import data_reader


def main():
    data = data_reader.DataReader().get_data()
    data.add_floor()
    print(data.simulate_sand_falling())


if __name__ == '__main__':
    main()
