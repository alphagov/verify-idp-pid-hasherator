import argparse
import src.file_helper as file_helper
from src.hasher import Hasher


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'csv', nargs='+',
        help='Path to a CSV file. At least one must be specified.', type=str)
    return parser.parse_args()


def main():
    args = parse_arguments()
    csv_file_sets = [file_helper.find_all_with_extension(f, '.csv') for f in args.csv]
    hasherator = Hasher()
    for csv_file_set in csv_file_sets:
        for csv_file in csv_file_set:
            hasherator.process_input(csv_file)


if __name__ == '__main__':
    main()
