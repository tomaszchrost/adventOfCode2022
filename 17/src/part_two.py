import data_reader


def main():
    data = data_reader.DataReader().get_data('resources/jets.dat')
    data.simulate_big_flow()
    print(data.get_height())


if __name__ == '__main__':
    main()
