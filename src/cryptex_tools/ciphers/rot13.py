def encrypt(text: str, key=None) -> str:
    """
    Encrypt (or decrypt) a string using the ROT13 cipher.

    Each letter in the input text is shifted by 13 positions in the alphabet.
    Non-alphabetic characters are left unchanged. The key argument is ignored
    (included for interface compatibility).

    Args:
        text (str): The input text to encrypt or decrypt.
        key: Ignored for ROT13.

    Returns:
        str: The transformed text after applying ROT13.
    """
    result = []
    for char in text:
        if char.isalpha():
            # Shift character by 13 within its case (A-Z or a-z)
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + 13) % 26 + base
            result.append(chr(shifted))
        else:
            # Leave non-alphabetic characters unchanged
            result.append(char)
    return "".join(result)

# ROT13 is symmetric; decrypt is same as encrypt
decrypt = encrypt

def get_info():
    """
    Get metadata information about the ROT13 cipher.

    Returns:
        dict: Information including name, key type, and description.
    """
    return {
        "name": "ROT13 Cipher",
        "key_type": "None",
        "description": "Shifts letters by 13 places; symmetric cipher (encrypt = decrypt).",
    }
