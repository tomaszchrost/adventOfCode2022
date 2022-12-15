import data_reader
import signals


def main():
    data = data_reader.DataReader().get_data_as_one_list()
    print(signals.get_decoder_key(data))


if __name__ == '__main__':
    main()
