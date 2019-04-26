import logging
import os
import src.csv_helper as csv
from src.hash_helper import hash
from src.csv_settings import CsvSettings

HASHED_PID_COLUMN_NAME = 'gds_hashed_pid'
HASHED_PID_FILE_SUFFIX = '_hpids'
logger = logging.getLogger(__name__)


class Hasher:
    def __init__(self):
        self.csv_settings = CsvSettings()

    def process_input(self, input_path):
        logger.debug(f'Parsing CSV: "{input_path}"')
        headers, rows = csv.read(input_path)
        self.csv_settings.next_csv(headers)
        add_hashed_pids(rows, self.csv_settings)
        output_path = generate_destination(input_path)
        output_headers = headers[:]
        output_headers.append(HASHED_PID_COLUMN_NAME)
        csv.write(output_path, output_headers, rows)
        logger.debug(f'Wrote output CSV file: "{output_path}"')


def add_hashed_pids(data, csv_settings):
    idp_id = csv_settings.idp_id
    for row in data:
        if csv_settings.idp_column_name:
            idp_id = row[csv_settings.idp_column_name]
        pid = row[csv_settings.pid_column_name]
        hashed_pid = hash(idp_id, pid)
        row[HASHED_PID_COLUMN_NAME] = hashed_pid


def generate_destination(input_path):
    prefix, extension = os.path.splitext(input_path)
    return prefix + HASHED_PID_FILE_SUFFIX + extension
