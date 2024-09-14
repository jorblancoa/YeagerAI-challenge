from typing import Dict, Any

def simple_hash(data: str) -> str:
    """
    A simple custom hashing function that produces a 30-character hash.
    Args:
        data (str): The input string to be hashed.
    Returns:
        str: A 30-character hash of the input data.
    """
    # Initialize hash value
    hash_value = 0

    # Use a prime number for multiplication to distribute bits
    prime = 101

    for char in data:
        # Multiply hash by prime and add ASCII value of character
        hash_value = (hash_value * prime + ord(char)) & 0xFFFFFFFF

    # Convert to hexadecimal and ensure it's 30 characters long
    hex_hash = hex(hash_value)[2:].zfill(30)
    return hex_hash[:30]

def reconstruct_data(fragments: Dict[int, Dict[str, Any]]) -> str:
    """
    Reconstructs the original data from fragments, verifying integrity.

    Args:
        fragments (Dict[int, Dict[str, Any]]): A dictionary of data fragments and their hashes.

    Returns:
        str: The reconstructed data if all fragments are valid, or an error message.
    """
    if not fragments:
        return "Error: No fragments provided."

    # Sort fragments by key to ensure correct order
    sorted_fragments = sorted(fragments.items())

    reconstructed_data = []
    for key, fragment in sorted_fragments:
        data = fragment.get('data')
        stored_hash = fragment.get('hash')

        if data is None or stored_hash is None:
            return f"Error: Fragment {key} is missing 'data' or 'hash'."

        # Verify integrity of the fragment
        calculated_hash = simple_hash(data)
        if calculated_hash != stored_hash:
            return f"Error: Data integrity verification failed at fragment {key}."

        reconstructed_data.append(data)

    return ''.join(reconstructed_data)

if __name__ == "__main__":
    # Example usage
    fragments = {
        1: {'data': 'Hello', 'hash': simple_hash('Hello')},
        2: {'data': 'World', 'hash': simple_hash('World')},
        3: {'data': '!', 'hash': simple_hash('!')}
    }
    original_data = reconstruct_data(fragments)
    print("Fragments:", fragments)
    print("Reconstructed Data:", original_data)