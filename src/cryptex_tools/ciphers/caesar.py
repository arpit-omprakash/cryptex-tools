def encrypt(text: str, key: int) -> str:
    """
    Encrypt a plaintext string using the Caesar cipher.

    Each letter in the input text is shifted by the specified key value.
    Non-alphabetic characters are left unchanged.

    Args:
        text (str): The plaintext to encrypt.
        key (int): The shift value (number of positions to shift).

    Returns:
        str: The resulting ciphertext.
    """
    result = []
    for char in text:
        if char.isalpha():
            # Shift character within its case (A-Z or a-z)
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + key) % 26 + base
            result.append(chr(shifted))
        else:
            # Leave non-alphabetic characters unchanged
            result.append(char)
    return "".join(result)

def decrypt(text: str, key: int) -> str:
    """
    Decrypt a ciphertext string encrypted with the Caesar cipher.

    Args:
        text (str): The ciphertext to decrypt.
        key (int): The shift value used during encryption.

    Returns:
        str: The resulting plaintext.
    """
    return encrypt(text, -key)

def get_info():
    """
    Get metadata information about the Caesar cipher.

    Returns:
        dict: Information including name, key type, and description.
    """
    return {
        "name": "Caesar Cipher",
        "key_type": "int",
        "description": "Shifts each letter by a fixed number of positions in the alphabet.",
    }
