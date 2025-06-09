def brute_force_caesar(text):
    """
    Brute-force all possible Caesar cipher shifts on the given text.

    For each possible shift (0-25), attempts to decrypt the text and stores the result.

    Args:
        text (str): The ciphertext to brute-force.

    Returns:
        dict[int, str]: A dictionary mapping each shift value to the corresponding decrypted text.
    """
    possibilities = {}
    for shift in range(26):
        decrypted = ''.join(
            chr(((ord(char.upper()) - 65 - shift) % 26) + 65)
            if char.isalpha() else char
            for char in text
        )
        possibilities[shift] = decrypted
    return possibilities
