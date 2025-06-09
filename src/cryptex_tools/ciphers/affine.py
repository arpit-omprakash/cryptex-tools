def _modinv(a: int, m: int) -> int:
    """
    Compute the modular inverse of a modulo m using the Extended Euclidean Algorithm.

    Args:
        a (int): The number to find the inverse of.
        m (int): The modulus.

    Returns:
        int: The modular inverse of a modulo m.

    Raises:
        ValueError: If the modular inverse does not exist.
    """
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for a={a} under modulo {m}")

def encrypt(text: str, key: tuple[int, int]) -> str:
    """
    Encrypt a plaintext string using the Affine cipher.

    Args:
        text (str): The plaintext to encrypt.
        key (tuple[int, int]): The key as a tuple (a, b), where 'a' and 26 must be coprime.

    Returns:
        str: The resulting ciphertext.
    """
    a, b = key
    result = []
    for char in text:
        if char.isalpha():
            # Preserve case and only encrypt alphabetic characters
            base = ord('A') if char.isupper() else ord('a')
            x = ord(char) - base
            enc = (a * x + b) % 26
            result.append(chr(enc + base))
        else:
            # Non-alphabetic characters are not encrypted
            result.append(char)
    return "".join(result)

def decrypt(text: str, key: tuple[int, int]) -> str:
    """
    Decrypt a ciphertext string encrypted with the Affine cipher.

    Args:
        text (str): The ciphertext to decrypt.
        key (tuple[int, int]): The key as a tuple (a, b), where 'a' and 26 must be coprime.

    Returns:
        str: The resulting plaintext.

    Raises:
        ValueError: If the modular inverse of 'a' does not exist.
    """
    a, b = key
    a_inv = _modinv(a, 26)
    result = []
    for char in text:
        if char.isalpha():
            # Preserve case and only decrypt alphabetic characters
            base = ord('A') if char.isupper() else ord('a')
            y = ord(char) - base
            dec = (a_inv * (y - b)) % 26
            result.append(chr(dec + base))
        else:
            # Non-alphabetic characters are not decrypted
            result.append(char)
    return "".join(result)

def get_info():
    """
    Get metadata information about the Affine cipher.

    Returns:
        dict: Information including name, key type, and description.
    """
    return {
        "name": "Affine Cipher",
        "key_type": "tuple[int, int]",
        "description": "Encrypts by (a*x + b) mod 26; 'a' must be coprime with 26.",
    }
