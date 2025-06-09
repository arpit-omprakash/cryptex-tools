# Unicode Pigpen cipher symbols for letters A-Z
# Source: Unicode block 'Geometric Shapes' & others approximating Pigpen glyphs

LETTER_TO_SYMBOL = {
    'A': '⨀', 'B': '⨁', 'C': '⨂', 'D': '⨃', 'E': '⨄', 'F': '⨅', 'G': '⨆', 'H': '⨇',
    'I': '⨈', 'J': '⨉', 'K': '⨊', 'L': '⨋', 'M': '⨌', 'N': '⨍', 'O': '⨎', 'P': '⨏',
    'Q': '⨐', 'R': '⨑', 'S': '⨒', 'T': '⨓', 'U': '⨔', 'V': '⨕', 'W': '⨖', 'X': '⨗',
    'Y': '⨘', 'Z': '⨙',
}

# Reverse mapping for decryption
SYMBOL_TO_LETTER = {v: k for k, v in LETTER_TO_SYMBOL.items()}

def encrypt(text: str, key=None) -> str:
    """
    Encrypt a string using the Pigpen cipher (Unicode symbols).

    Each letter A-Z is replaced with a corresponding Unicode Pigpen symbol.
    Non-alphabetic characters are left unchanged. The key argument is ignored
    (included for interface compatibility).

    Args:
        text (str): The plaintext to encrypt.
        key: Ignored for Pigpen cipher.

    Returns:
        str: The resulting ciphertext with Pigpen symbols.
    """
    result = []
    for c in text.upper():
        if c in LETTER_TO_SYMBOL:
            result.append(LETTER_TO_SYMBOL[c])
        else:
            result.append(c)
    return "".join(result)

def decrypt(text: str, key=None) -> str:
    """
    Decrypt a string encrypted with the Pigpen cipher (Unicode symbols).

    Each Pigpen symbol is replaced with its corresponding uppercase letter.
    Non-Pigpen symbols are left unchanged. The key argument is ignored.

    Args:
        text (str): The ciphertext to decrypt.
        key: Ignored for Pigpen cipher.

    Returns:
        str: The resulting plaintext (uppercase letters).
    """
    result = []
    for c in text:
        if c in SYMBOL_TO_LETTER:
            result.append(SYMBOL_TO_LETTER[c])
        else:
            result.append(c)
    return "".join(result)

def get_info():
    """
    Get metadata information about the Pigpen cipher.

    Returns:
        dict: Information including name, key type, and description.
    """
    return {
        "name": "Pigpen Cipher (Unicode)",
        "key_type": "None",
        "description": "Substitution cipher using Unicode Pigpen symbols for letters A-Z.",
    }
