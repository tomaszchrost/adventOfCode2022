import data_reader
import height_map


def main():
    data = data_reader.DataReader().get_data()
    print(data.dijkstras())


if __name__ == '__main__':
    main()
