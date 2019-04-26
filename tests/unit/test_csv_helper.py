import os
from unittest.mock import patch, mock_open

from tests.context import csv_helper

SEPARATOR = ','
NEW_LINE = os.linesep
rows = [
    'one,two,three,four',
    '1,2,3,4',
    '7,8,9,10'
]
test_csv = NEW_LINE.join(rows) + NEW_LINE


def test_read():
    m_open = mock_open(read_data=test_csv)
    with patch('tests.context.csv_helper.open', m_open):
        header, read_rows = csv_helper.read('some/path')
    assert SEPARATOR.join(header) == rows[0]
    for index, row in enumerate(read_rows, 1):
        assert SEPARATOR.join(row.values()) == rows[index]


def test_write():
    headers = rows[0].split(SEPARATOR)
    data = [{headers[i]: (row.split(SEPARATOR))[i] for i in range(4)} for row in rows[1:]]
    m_write = mock_open()
    with patch('tests.context.csv_helper.open', m_write):
        csv_helper.write('another/path', headers, data)
    assert test_csv == get_written_string_from_mock(m_write)


def get_written_string_from_mock(mock_open):
    return ''.join(call[0][0] for call in mock_open.return_value.write.call_args_list)
