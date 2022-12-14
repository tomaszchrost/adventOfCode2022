import data_reader
import height_map


def main():
    data = data_reader.DataReader().get_data()
    print(data.best_starting_location())


if __name__ == '__main__':
    main()
