import data_reader


def main():
    data = data_reader.DataReader().get_data()
    print(data.cannot_contain_beacon_position_count(2000000))


if __name__ == '__main__':
    main()
