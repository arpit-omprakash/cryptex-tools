import string

def _generate_key_matrix(key: str):
    """
    Generate a 5x5 Playfair key matrix from the keyword.

    Args:
        key (str): The keyword for the Playfair cipher.

    Returns:
        list[list[str]]: 5x5 matrix of letters (with 'j' replaced by 'i').
    """
    key = key.lower().replace('j', 'i')
    seen = set()
    matrix = []
    for c in key + string.ascii_lowercase:
        if c == 'j':  # traditionally 'j' is merged with 'i'
            continue
        if c in seen or not c.isalpha():
            continue
        seen.add(c)
        matrix.append(c)
    return [matrix[i * 5:(i + 1) * 5] for i in range(5)]

def _find_position(matrix, char):
    """
    Find the row and column of a character in the Playfair matrix.

    Args:
        matrix (list[list[str]]): The Playfair key matrix.
        char (str): The character to find.

    Returns:
        tuple[int, int] or None: (row, col) if found, else None.
    """
    for i, row in enumerate(matrix):
        for j, c in enumerate(row):
            if c == char:
                return i, j
    return None

def _prepare_text(text):
    """
    Prepare the plaintext/ciphertext for Playfair encryption/decryption.

    - Converts to lowercase, replaces 'j' with 'i'.
    - Splits into digraphs, inserting 'x' between duplicate letters or at the end if needed.

    Args:
        text (str): The input text.

    Returns:
        list[str]: List of characters, ready for digraph processing.
    """
    text = text.lower().replace('j', 'i')
    prepared = []
    i = 0
    while i < len(text):
        c1 = text[i]
        if not c1.isalpha():
            i += 1
            continue
        if i + 1 < len(text):
            c2 = text[i + 1]
            if not c2.isalpha():
                prepared.append(c1)
                i += 1
                continue
            if c1 == c2:
                prepared.extend([c1, 'x'])
                i += 1
            else:
                prepared.extend([c1, c2])
                i += 2
        else:
            prepared.extend([c1, 'x'])
            i += 1
    return prepared

def encrypt(text: str, key: str) -> str:
    """
    Encrypt plaintext using the Playfair cipher.

    Args:
        text (str): The plaintext to encrypt.
        key (str): The keyword for the Playfair cipher.

    Returns:
        str: The resulting ciphertext (uppercase).
    """
    matrix = _generate_key_matrix(key)
    prepared = _prepare_text(text)
    result = []

    for i in range(0, len(prepared), 2):
        r1, c1 = _find_position(matrix, prepared[i])
        r2, c2 = _find_position(matrix, prepared[i + 1])
        if r1 == r2:
            # same row, shift right
            result.append(matrix[r1][(c1 + 1) % 5])
            result.append(matrix[r2][(c2 + 1) % 5])
        elif c1 == c2:
            # same column, shift down
            result.append(matrix[(r1 + 1) % 5][c1])
            result.append(matrix[(r2 + 1) % 5][c2])
        else:
            # rectangle swap
            result.append(matrix[r1][c2])
            result.append(matrix[r2][c1])
    return "".join(result).upper()

def decrypt(text: str, key: str) -> str:
    """
    Decrypt ciphertext encrypted with the Playfair cipher.

    Args:
        text (str): The ciphertext to decrypt.
        key (str): The keyword for the Playfair cipher.

    Returns:
        str: The resulting plaintext (uppercase, with 'x' fillers removed).
    """
    matrix = _generate_key_matrix(key)
    text = text.lower()
    result = []

    for i in range(0, len(text), 2):
        r1, c1 = _find_position(matrix, text[i])
        r2, c2 = _find_position(matrix, text[i + 1])
        if r1 == r2:
            # same row, shift left
            result.append(matrix[r1][(c1 - 1) % 5])
            result.append(matrix[r2][(c2 - 1) % 5])
        elif c1 == c2:
            # same column, shift up
            result.append(matrix[(r1 - 1) % 5][c1])
            result.append(matrix[(r2 - 1) % 5][c2])
        else:
            # rectangle swap
            result.append(matrix[r1][c2])
            result.append(matrix[r2][c1])
    # Remove 'x' used as fillers (may remove legitimate x's, as is common in Playfair)
    return "".join(result).replace('x', '').upper()

def get_info():
    """
    Get metadata information about the Playfair cipher.

    Returns:
        dict: Information including name, key type, and description.
    """
    return {
        "name": "Playfair Cipher",
        "key_type": "str",
        "description": "Digraph substitution cipher using a 5x5 matrix of letters based on a keyword.",
    }
