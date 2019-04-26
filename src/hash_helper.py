import hashlib


def hash(*args):
    hash = hashlib.sha256()
    for arg in args:
        hash.update(arg.encode('utf-8'))
    return hash.hexdigest()
