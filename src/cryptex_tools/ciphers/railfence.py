def encrypt(text: str, key: int) -> str:
    """
    Encrypt a plaintext string using the Rail Fence cipher.

    The Rail Fence cipher writes the text in a zigzag pattern across a number of rails
    and then reads off each rail row-wise to produce the ciphertext.

    Args:
        text (str): The plaintext to encrypt.
        key (int): The number of rails to use.

    Returns:
        str: The resulting ciphertext.
    """
    if key == 1:
        return text

    rails = ['' for _ in range(key)]
    rail = 0
    direction = 1  # 1 for down, -1 for up

    for char in text:
        rails[rail] += char
        rail += direction
        # Change direction at the top or bottom rail
        if rail == 0 or rail == key - 1:
            direction *= -1

    return ''.join(rails)

def decrypt(text: str, key: int) -> str:
    """
    Decrypt a ciphertext string encrypted with the Rail Fence cipher.

    Args:
        text (str): The ciphertext to decrypt.
        key (int): The number of rails used during encryption.

    Returns:
        str: The resulting plaintext.
    """
    if key == 1:
        return text

    # Create an empty matrix to mark places with '*'
    rail_len = len(text)
    matrix = [['\n' for _ in range(rail_len)] for _ in range(key)]

    # Mark the zigzag pattern in the matrix
    rail = 0
    direction = 1
    for i in range(rail_len):
        matrix[rail][i] = '*'
        rail += direction
        if rail == 0 or rail == key - 1:
            direction *= -1

    # Fill the matrix with the ciphertext characters in the zigzag pattern
    index = 0
    for r in range(key):
        for c in range(rail_len):
            if matrix[r][c] == '*' and index < rail_len:
                matrix[r][c] = text[index]
                index += 1

    # Read the matrix in zigzag manner to reconstruct the plaintext
    result = []
    rail = 0
    direction = 1
    for i in range(rail_len):
        result.append(matrix[rail][i])
        rail += direction
        if rail == 0 or rail == key - 1:
            direction *= -1

    return ''.join(result)

def get_info():
    """
    Get metadata information about the Rail Fence cipher.

    Returns:
        dict: Information including name, key type, and description.
    """
    return {
        "name": "Rail Fence Cipher",
        "key_type": "int",
        "description": "A transposition cipher that writes text in a zigzag pattern on rails and reads row-wise.",
    }
