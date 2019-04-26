from tests.context import hash_helper

test_strings = ['frodo', 'baggins']
test_sha_hex = '512ade49b07590a430d15136f70953ff6999b86271ea91c79300f733ed056724'


def test_multi_variable_hash():
    calculated_hash = hash_helper.hash(*test_strings)
    assert test_sha_hex == calculated_hash
