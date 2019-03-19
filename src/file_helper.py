import os
import logging

logger = logging.getLogger(__name__)


def exists(path):
    return os.path.exists(path)


def file_extension(path):
    _, extension = os.path.splitext(path)
    return extension


def extension_matches(path, extension):
    return file_extension(path) == extension


def find_all_with_extension(path, extension):
    logger.debug(f'Searching "{path}" for files with extension "{extension}"')
    if not exists(path):
        return []
    files = []
    if extension_matches(path, extension):
        files.append(path)
    logger.debug(f'Discovered the following matching files: {files}')
    return files
