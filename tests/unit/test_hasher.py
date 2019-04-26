from tests.context import CsvSettings
from tests.context import hash_helper
from tests.context import hasher

idp_column_name = 'idp_id_column'
idp_id = 'idp_id'
pid_column_name = 'pid_column'
pid = 'test_pid'
hashed_pid = hash_helper.hash(idp_id, pid)


def test_add_hashed_pids_with_idp_column():
    dataset = [
        {idp_column_name: idp_id, pid_column_name: pid}
    ]
    csv_settings = CsvSettings()
    csv_settings.pid_column_name = pid_column_name
    csv_settings.idp_column_name = idp_column_name
    hasher.add_hashed_pids(dataset, csv_settings)

    assert hasher.HASHED_PID_COLUMN_NAME in dataset[0]
    assert dataset[0][hasher.HASHED_PID_COLUMN_NAME] == hashed_pid


def test_add_hashed_pids_with_idp_id():
    dataset = [
        {idp_column_name: idp_id, pid_column_name: pid}
    ]
    csv_settings = CsvSettings()
    csv_settings.pid_column_name = pid_column_name
    csv_settings.idp_id = idp_id
    hasher.add_hashed_pids(dataset, csv_settings)

    assert hasher.HASHED_PID_COLUMN_NAME in dataset[0]
    assert dataset[0][hasher.HASHED_PID_COLUMN_NAME] == hashed_pid


def test_generate_destination():
    expectations = [
        ('file.ext', 'file' + hasher.HASHED_PID_FILE_SUFFIX + '.ext'),
        ('file.intermediate.ext', 'file.intermediate' + hasher.HASHED_PID_FILE_SUFFIX + '.ext'),
        ('file', 'file' + hasher.HASHED_PID_FILE_SUFFIX),
        ('.hidden', '.hidden' + hasher.HASHED_PID_FILE_SUFFIX),
        ('.hidden.ext', '.hidden' + hasher.HASHED_PID_FILE_SUFFIX + '.ext'),
    ]
    for case in expectations:
        assert hasher.generate_destination(case[0]) == case[1]
