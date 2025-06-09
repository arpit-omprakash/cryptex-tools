# Define QWERTY keyboard layout rows
QWERTY_ROWS = [
    "qwertyuiop",
    "asdfghjkl",
    "zxcvbnm",
]

def _find_char_pos(c: str):
    """
    Find the row index and position of a character in the QWERTY keyboard layout.

    Args:
        c (str): The character to locate.

    Returns:
        tuple: (row_idx, pos) if found, otherwise (None, None).
    """
    c_lower = c.lower()
    for row_idx, row in enumerate(QWERTY_ROWS):
        if c_lower in row:
            return row_idx, row.index(c_lower)
    return None, None

def _shift_char(c: str, key: int) -> str:
    """
    Shift a character by the given key within its QWERTY row.

    Args:
        c (str): The character to shift.
        key (int): The number of positions to shift.

    Returns:
        str: The shifted character, preserving case. Non-alphabetic characters are unchanged.
    """
    row_idx, pos = _find_char_pos(c)
    if row_idx is None:
        return c  # Non-alphabetic chars remain unchanged

    row = QWERTY_ROWS[row_idx]
    shifted_pos = (pos + key) % len(row)
    shifted_char = row[shifted_pos]

    return shifted_char.upper() if c.isupper() else shifted_char

def encrypt(text: str, key: int) -> str:
    """
    Encrypt text using the Keyboard Shift cipher.

    Args:
        text (str): The plaintext to encrypt.
        key (int): The shift value.

    Returns:
        str: The resulting ciphertext.
    """
    return "".join(_shift_char(c, key) for c in text)

def decrypt(text: str, key: int) -> str:
    """
    Decrypt text encrypted with the Keyboard Shift cipher.

    Args:
        text (str): The ciphertext to decrypt.
        key (int): The shift value used during encryption.

    Returns:
        str: The resulting plaintext.
    """
    return encrypt(text, -key)

def get_info():
    """
    Get metadata information about the Keyboard Shift cipher.

    Returns:
        dict: Information including name, key type, and description.
    """
    return {
        "name": "Keyboard Shift Cipher",
        "key_type": "int",
        "description": "Shifts letters according to their position in QWERTY keyboard rows.",
    }
