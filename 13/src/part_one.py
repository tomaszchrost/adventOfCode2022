import data_reader
import signals


def main():
    data = data_reader.DataReader().get_data()
    print(signals.sum_of_indices_in_order(data))


if __name__ == '__main__':
    main()
