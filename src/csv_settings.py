import logging

logger = logging.getLogger(__name__)


class CsvSettings:
    def __init__(self):
        self.pid_column_name = None
        self.idp_column_name = None
        self.idp_id = None

    def next_csv(self, headers):
        """
        Prepare for a new CSV file.
        Checks whether the settings might still be valid.
        If obviously not (e.g. missing the column) or if user requests, will reset settings
        """
        if not self.headers_still_valid(headers):
            self.prompt_for_setup(headers)
            self.setup_pid_settings_from_headers(headers)
            self.setup_idp_settings_from_headers(headers)
        else:
            self.confirm_settings(headers)

    def headers_still_valid(self, headers):
        if not self.pid_column_name:
            return False
        if self.pid_column_name not in headers:
            return False
        if self.idp_column_name and self.idp_column_name not in headers:
            return False
        if not self.idp_column_name and not self.idp_id:
            return False
        return True

    def confirm_settings(self, headers):
        self.prompt_for_setup(headers)
        logger.info('These are the settings from the last CSV file parsed:')
        logger.info(f'\tPID column header:\t{self.pid_column_name}')
        if self.idp_column_name:
            logger.info(f'\tIDP column header:\t{self.idp_column_name}')
        else:
            logger.info(f'\tIDP entity ID:\t{self.idp_id}')
        prompt = input('Do these settings still look right? Please enter yes or no [yN]: ')
        if prompt[0].lower() != 'y':
            self.setup_pid_settings_from_headers(headers)
            self.setup_idp_settings_from_headers(headers)

    def prompt_for_setup(self, headers):
        logger.info('The following CSV headers were parsed:')
        for index, header in enumerate(headers, 1):
            logger.info(f'{index}\t{header}')

    def setup_pid_settings_from_headers(self, headers, needs_prompt=False):
        if needs_prompt:
            self.prompt_for_setup(headers)
        prompt = input('Which column contains the PID? Please enter the column index.\nColumn index: ')
        self.pid_column_name = headers[int(prompt.strip()) - 1]

    def setup_idp_settings_from_headers(self, headers, needs_prompt=False):
        if needs_prompt:
            self.prompt_for_setup(headers)
        self.idp_column_name = None
        self.idp_id = None
        prompt = input('Does this CSV include the IDP entity ID as a column? Please enter yes or no [yN]: ')
        if prompt[0].lower() == 'y':
            prompt = input('Which column? Please enter either the exact column name, or the index: ')
            self.idp_column_name = headers[int(prompt.strip()) - 1]
        else:
            prompt = input('Please provide the IDP entity ID. This is needed for the hashing process: ')
            self.idp_id = prompt.strip()
