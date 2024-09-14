import pytest
from challenge_1 import simple_hash, reconstruct_data

def test_simple_hash():
    """
    Test the simple_hash function for length, consistency, and different inputs.
    """
    # Test hash length
    assert len(simple_hash("TestData")) == 30, "Hash length should be exactly 30 characters."

    # Test consistency
    data = "ConsistencyCheck"
    assert simple_hash(data) == simple_hash(data), "Hashes for the same data should be identical."

    # Test different inputs
    assert simple_hash("DataOne") != simple_hash("DataTwo"), "Different inputs should produce different hashes."

    # Test empty string
    assert simple_hash("") == '0' * 30, "Hash of an empty string should be all zeros."

def test_reconstruct_data_success():
    """
    Test successful reconstruction of data from valid fragments.
    """
    fragments = {
        2: {'data': 'World', 'hash': simple_hash('World')},
        1: {'data': 'Hello', 'hash': simple_hash('Hello')},
        3: {'data': '!', 'hash': simple_hash('!')}
    }
    assert reconstruct_data(fragments) == "HelloWorld!", "Reconstructed data does not match expected output."

def test_reconstruct_data_integrity_failure():
    """
    Test reconstruction failure when fragments have invalid hashes.
    """
    # Test with one invalid fragment
    fragments_one_invalid = {
        1: {'data': 'Hello', 'hash': simple_hash('Hello')},
        2: {'data': 'World', 'hash': 'invalidhash'},
        3: {'data': '!', 'hash': simple_hash('!')}
    }
    assert reconstruct_data(fragments_one_invalid) == "Error: Data integrity verification failed at fragment 2."

    # Test with all invalid fragments
    fragments_all_invalid = {
        1: {'data': 'Hello', 'hash': 'invalidhash1'},
        2: {'data': 'World', 'hash': 'invalidhash2'},
        3: {'data': '!', 'hash': 'invalidhash3'}
    }
    assert reconstruct_data(fragments_all_invalid) == "Error: Data integrity verification failed at fragment 1."

def test_reconstruct_data_edge_cases():
    """
    Test reconstruction with various edge cases.
    """
    # Empty input
    assert reconstruct_data({}) == "Error: No fragments provided."

    # Missing data or hash
    fragments_missing_keys = {
        1: {'data': 'Hello'},
        2: {'hash': simple_hash('World')},
        3: {'data': '!', 'hash': simple_hash('!')}
    }
    assert reconstruct_data(fragments_missing_keys) == "Error: Fragment 1 is missing 'data' or 'hash'."

    # Non-sequential keys
    fragments_non_sequential = {
        10: {'data': 'Data10', 'hash': simple_hash('Data10')},
        5: {'data': 'Data5', 'hash': simple_hash('Data5')},
        15: {'data': 'Data15', 'hash': simple_hash('Data15')}
    }
    assert reconstruct_data(fragments_non_sequential) == "Data5Data10Data15"

def test_reconstruct_data_large_input():
    """
    Test reconstruction with a large number of fragments.
    """
    num_fragments = 1000
    fragments = {i: {'data': f'Fragment{i}', 'hash': simple_hash(f'Fragment{i}')} for i in range(1, num_fragments + 1)}
    expected_data = ''.join(f'Fragment{i}' for i in range(1, num_fragments + 1))
    assert reconstruct_data(fragments) == expected_data
