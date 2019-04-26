import pytest
from tests.context import CsvSettings

idp_id = 'idp_id'
idp_column_name = 'idp_column'
pid_column_name = 'pid_column'
base_headers = ['header', 'another header']
headers_with_idp = base_headers + [idp_column_name]
headers_with_pid = base_headers + [pid_column_name]
all_headers = base_headers + [pid_column_name, idp_column_name]


@pytest.fixture
def csv_settings():
    return CsvSettings()


def test_headers_not_valid_without_pid(csv_settings):
    csv_settings.idp_id = idp_id
    csv_settings.idp_column_name = idp_column_name
    assert not csv_settings.headers_still_valid(all_headers)


def test_headers_not_valid_without_specified_pid_column(csv_settings):
    csv_settings.idp_id = idp_id
    csv_settings.idp_column_name = idp_column_name
    csv_settings.pid_column_name = pid_column_name
    assert not csv_settings.headers_still_valid(headers_with_idp)


def test_headers_not_valid_without_specified_idp_column(csv_settings):
    csv_settings.idp_column_name = idp_column_name
    csv_settings.pid_column_name = pid_column_name
    assert not csv_settings.headers_still_valid(headers_with_pid)


def test_headers_not_valid_without_idp(csv_settings):
    csv_settings.pid_column_name = pid_column_name
    assert not csv_settings.headers_still_valid(all_headers)


def test_headers_valid_for_idp_column(csv_settings):
    csv_settings.idp_column_name = idp_column_name
    csv_settings.pid_column_name = pid_column_name
    assert csv_settings.headers_still_valid(all_headers)


def test_headers_valid_for_idp_id(csv_settings):
    csv_settings.idp_id = idp_id
    csv_settings.pid_column_name = pid_column_name
    assert csv_settings.headers_still_valid(all_headers)
