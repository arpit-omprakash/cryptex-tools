def _format_key(text: str, key: str) -> str:
    """
    Repeat and align the key to match the length and non-alpha positions of the text.

    Args:
        text (str): The text to encrypt or decrypt.
        key (str): The keyword for the Vigenère cipher.

    Returns:
        str: The formatted key, repeated and aligned with the text.
    """
    key = key.upper()
    key_repeated = []
    key_index = 0
    for char in text:
        if char.isalpha():
            key_repeated.append(key[key_index % len(key)])
            key_index += 1
        else:
            key_repeated.append(char)
    return "".join(key_repeated)

def encrypt(text: str, key: str) -> str:
    """
    Encrypt a plaintext string using the Vigenère cipher.

    Each letter in the input text is shifted by the corresponding letter in the key.
    Non-alphabetic characters are left unchanged.

    Args:
        text (str): The plaintext to encrypt.
        key (str): The keyword for the cipher.

    Returns:
        str: The resulting ciphertext.
    """
    result = []
    key = _format_key(text, key)
    for t_char, k_char in zip(text, key):
        if t_char.isalpha():
            base = ord('A') if t_char.isupper() else ord('a')
            k_shift = ord(k_char.upper()) - ord('A')
            shifted = (ord(t_char) - base + k_shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(t_char)
    return "".join(result)

def decrypt(text: str, key: str) -> str:
    """
    Decrypt a ciphertext string encrypted with the Vigenère cipher.

    Args:
        text (str): The ciphertext to decrypt.
        key (str): The keyword used during encryption.

    Returns:
        str: The resulting plaintext.
    """
    result = []
    key = _format_key(text, key)
    for t_char, k_char in zip(text, key):
        if t_char.isalpha():
            base = ord('A') if t_char.isupper() else ord('a')
            k_shift = ord(k_char.upper()) - ord('A')
            shifted = (ord(t_char) - base - k_shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(t_char)
    return "".join(result)

def get_info():
    """
    Get metadata information about the Vigenère cipher.

    Returns:
        dict: Information including name, key type, and description.
    """
    return {
        "name": "Vigenere Cipher",
        "key_type": "str",
        "description": "Uses a keyword to shift letters; the keyword repeats to match text length.",
    }
