import os
import logging

logger = logging.getLogger(__name__)


def exists(path):
    return os.path.exists(path)


def is_directory(path):
    return os.path.isdir(path)


def file_extension(path):
    _, extension = os.path.splitext(path)
    return extension


def extension_matches(path, extension):
    return file_extension(path) == extension


def find_files_under_directory_with_extension(root, extension):
    logger.debug(f'Walking path rooted at directory: "{root}"')
    matched_files = []
    for directory, _, files in os.walk(root):
        logger.debug(f'Iterating through files in directory: "{directory}"')
        for file in files:
            if extension_matches(file, extension):
                matched_path = os.path.join(directory, file)
                logger.debug(f'Matched file "{matched_path}"')
                matched_files.append(matched_path)
    return matched_files


def find_all_with_extension(path, extension):
    if not exists(path):
        logger.debug(f'Specified path "{path}" does not exist.')
        return []
    logger.debug(f'Searching "{path}" for files with extension "{extension}"')
    if is_directory(path):
        files = find_files_under_directory_with_extension(path, extension)
    else:
        logger.debug(f'File path provided: "{path}"')
        files = []
        if extension_matches(path, extension):
            files = [path]
    logger.debug(f'Discovered the following matching files: {files}')
    return files
