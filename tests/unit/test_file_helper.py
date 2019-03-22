import os
import pytest
import random
import tempfile
import unittest
from tests.context import file_helper

ext = '.ext'
other_ext = '.not'


class TemporaryFilesystem():
    def __init__(self, root, files_with_ext):
        self.root = root
        self.files_with_ext = files_with_ext


@pytest.fixture(scope="module")
def temporary_filesystem():
    expected_paths = []
    try:
        tempdir_obj = tempfile.TemporaryDirectory()
        tempdir = tempdir_obj.name
        for _ in range(3):
            subdir_name = 'tmpdir' + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))
            subdir = os.path.join(tempdir, subdir_name)
            os.makedirs(subdir)
            for dir in [tempdir, subdir]:
                tempfile.NamedTemporaryFile(suffix=other_ext, dir=dir, delete=False)
                file_name = tempfile.NamedTemporaryFile(suffix=ext, dir=dir, delete=False).name
                expected_paths.append(os.path.join(dir, file_name))
        yield TemporaryFilesystem(tempdir, expected_paths)
    finally:
        tempdir_obj.cleanup()


def test_find_files_under_directory_with_extension(temporary_filesystem):
    temp_path = temporary_filesystem.root
    expected_paths = temporary_filesystem.files_with_ext
    walked_paths = file_helper.find_files_under_directory_with_extension(temp_path, ext)
    unittest.TestCase().assertCountEqual(expected_paths, walked_paths)
