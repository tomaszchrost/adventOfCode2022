import data_reader


def main():
    data = data_reader.DataReader().get_data()
    print(data.simulate_sand_falling())


if __name__ == '__main__':
    main()
