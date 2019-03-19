import os


def exists(path):
    return os.path.exists(path)


def file_extension(path):
    _, extension = os.path.splitext(path)
    return extension


def extension_matches(path, extension):
    return file_extension(path) == extension


def find_all_with_extension(path, extension):
    if not exists(path):
        return []
    files = []
    if extension_matches(path, extension):
        files.append(path)
    return files
