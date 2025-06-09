def encrypt(text: str, key=None) -> str:
    """
    Encrypt (or decrypt) a string using the Atbash cipher.

    The Atbash cipher substitutes each letter with its reverse in the alphabet.
    For example, A <-> Z, B <-> Y, etc. Non-alphabetic characters are unchanged.

    Args:
        text (str): The input text to encrypt or decrypt.
        key: Ignored for Atbash (included for interface compatibility).

    Returns:
        str: The transformed text after applying the Atbash cipher.
    """
    def atbash_char(c):
        # Substitute uppercase letters with their reverse in the alphabet
        if c.isupper():
            return chr(ord('Z') - (ord(c) - ord('A')))
        # Substitute lowercase letters with their reverse in the alphabet
        elif c.islower():
            return chr(ord('z') - (ord(c) - ord('a')))
        # Leave non-alphabetic characters unchanged
        else:
            return c

    return "".join(atbash_char(c) for c in text)

# Atbash is symmetric; encryption and decryption are the same operation
decrypt = encrypt

def get_info():
    """
    Get metadata information about the Atbash cipher.

    Returns:
        dict: Information including name, key type, and description.
    """
    return {
        "name": "Atbash Cipher",
        "key_type": "None",
        "description": "Substitutes each letter with its reverse in the alphabet (A ↔ Z, B ↔ Y).",
    }
