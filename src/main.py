import argparse
import logging
import src.file_helper as file_helper
from src.hasher import Hasher

logger = logging.getLogger(__name__)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--verbose', help='Verbose mode.', action='store_true')
    parser.add_argument(
        'csv', nargs='+',
        help='Path to a CSV file. At least one must be specified.', type=str)
    return parser.parse_args()


def main():
    args = parse_arguments()
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    csv_file_sets = [file_helper.find_all_with_extension(f, '.csv') for f in args.csv]
    logger.debug(f'CSV files: {csv_file_sets}')
    hasherator = Hasher()
    for csv_file_set in csv_file_sets:
        for csv_file in csv_file_set:
            hasherator.process_input(csv_file)


if __name__ == '__main__':
    main()
