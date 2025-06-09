import string
import re
from collections import Counter

# English letter frequencies (relative) for chi-squared analysis
ENGLISH_FREQ = {
    'A': 0.08167, 'B': 0.01492, 'C': 0.02782, 'D': 0.04253,
    'E': 0.12702, 'F': 0.02228, 'G': 0.02015, 'H': 0.06094,
    'I': 0.06966, 'J': 0.00153, 'K': 0.00772, 'L': 0.04025,
    'M': 0.02406, 'N': 0.06749, 'O': 0.07507, 'P': 0.01929,
    'Q': 0.00095, 'R': 0.05987, 'S': 0.06327, 'T': 0.09056,
    'U': 0.02758, 'V': 0.00978, 'W': 0.02360, 'X': 0.00150,
    'Y': 0.01974, 'Z': 0.00074
}

ALPHABET = string.ascii_uppercase

def chi_squared_statistic(text):
    """
    Compute the chi-squared statistic for a given text compared to English letter frequencies.

    Args:
        text (str): The text to analyze.

    Returns:
        float: The chi-squared statistic (lower means closer to English).
    """
    text = text.upper()
    total = len(text)
    if total == 0:
        return float('inf')
    observed = Counter(text)
    chi_squared = 0.0
    for letter in ALPHABET:
        expected = ENGLISH_FREQ[letter] * total
        chi_squared += ((observed.get(letter, 0) - expected) ** 2) / expected
    return chi_squared

def index_of_coincidence(text):
    """
    Calculate the index of coincidence for a given text.

    Args:
        text (str): The text to analyze.

    Returns:
        float: The index of coincidence value.
    """
    N = len(text)
    if N <= 1:
        return 0.0
    freqs = Counter(text)
    ic = sum(f * (f - 1) for f in freqs.values()) / (N * (N - 1))
    return ic

def estimate_key_length_ic(ciphertext, max_key_len=16):
    """
    Estimate likely Vigenère key lengths using the index of coincidence.

    Args:
        ciphertext (str): The ciphertext to analyze.
        max_key_len (int): Maximum key length to consider.

    Returns:
        list[int]: Top 3 candidate key lengths.
    """
    ciphertext = re.sub(r'[^A-Z]', '', ciphertext.upper())
    ic_scores = []
    for key_len in range(1, max_key_len + 1):
        avg_ic = 0.0
        for i in range(key_len):
            column = ciphertext[i::key_len]
            avg_ic += index_of_coincidence(column)
        ic_scores.append((avg_ic / key_len, key_len))
    ic_scores.sort(reverse=True)
    return [k for _, k in ic_scores[:3]]

def break_caesar_chi(column):
    """
    Find the Caesar shift for a column that minimizes the chi-squared statistic.

    Args:
        column (str): The column of ciphertext.

    Returns:
        int: The best shift value (0-25).
    """
    best_shift = 0
    min_chi = float('inf')
    for shift in range(26):
        decrypted = ''.join(
            chr((ord(c) - 65 - shift) % 26 + 65) for c in column
        )
        chi = chi_squared_statistic(decrypted)
        if chi < min_chi:
            min_chi = chi
            best_shift = shift
    return best_shift

def decrypt_vigenere(ciphertext, key):
    """
    Decrypt a Vigenère ciphertext with a given key.

    Args:
        ciphertext (str): The ciphertext (A-Z only).
        key (str): The key (A-Z).

    Returns:
        str: The decrypted plaintext (A-Z).
    """
    ciphertext = ciphertext.upper()
    key = key.upper()
    decrypted = []
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            c = ord(char) - 65
            k = ord(key[i % len(key)]) - 65
            decrypted.append(chr((c - k + 26) % 26 + 65))
    return ''.join(decrypted)

def crack_vigenere_with_hint(ciphertext, partial_key):
    """
    Attempt to crack a Vigenère cipher given a partial key.

    Args:
        ciphertext (str): The ciphertext to crack.
        partial_key (str): The known part of the key.

    Returns:
        tuple[str, str]: (Guessed key, decrypted plaintext) or (None, "") if failed.
    """
    ciphertext = re.sub(r'[^A-Z]', '', ciphertext.upper())
    key_len = len(partial_key)
    remaining_len = 0

    # Try to estimate the full key length based on IC
    candidate_lengths = estimate_key_length_ic(ciphertext)
    for candidate_len in candidate_lengths:
        if candidate_len > key_len:
            key_len = candidate_len
            remaining_len = candidate_len - len(partial_key)
            break
    else:
        return None, ""

    guessed_key = partial_key.upper()
    for i in range(len(partial_key), key_len):
        column = ciphertext[i::key_len]
        shift = break_caesar_chi(column)
        guessed_key += chr(65 + shift)

    plaintext = decrypt_vigenere(ciphertext, guessed_key)
    if chi_squared_statistic(plaintext) < 150:
        return guessed_key, plaintext
    return None, ""

def crack_vigenere_with_auto_align(ciphertext, partial_key):
    """
    Attempt to crack a Vigenère cipher by aligning a partial key at different offsets.

    Args:
        ciphertext (str): The ciphertext to crack.
        partial_key (str): The known part of the key.

    Returns:
        tuple[str, str]: (Guessed key, decrypted plaintext) or (None, "") if failed.
    """
    ciphertext = re.sub(r'[^A-Z]', '', ciphertext.upper())
    best_result = ("", "")
    lowest_score = float('inf')

    for offset in range(len(partial_key)):
        trial_key = partial_key[offset:]
        key_len_guess = len(trial_key)

        # Estimate full key length using IC
        candidate_lengths = estimate_key_length_ic(ciphertext)
        for candidate_len in candidate_lengths:
            if candidate_len < key_len_guess:
                continue
            remaining_len = candidate_len - key_len_guess
            guessed_key = trial_key

            for i in range(len(trial_key), candidate_len):
                column = ciphertext[i::candidate_len]
                shift = break_caesar_chi(column)
                guessed_key += chr(65 + shift)

            decrypted = decrypt_vigenere(ciphertext, guessed_key)
            score = chi_squared_statistic(decrypted)
            if score < lowest_score:
                lowest_score = score
                best_result = (guessed_key, decrypted)

    if lowest_score < 150:
        return best_result
    return None, ""

def crack_vigenere_with_dictionary(ciphertext, wordlist_path=r"src/cryptex_tools/cryptanalysis/keywordlist.txt"):
    """
    Attempt to crack a Vigenère cipher using a dictionary of possible keys.

    Args:
        ciphertext (str): The ciphertext to crack.
        wordlist_path (str): Path to a file containing possible keys (one per line).

    Returns:
        tuple[str, str]: (Guessed key, decrypted plaintext) or (None, "") if failed.
    """
    ciphertext = re.sub(r'[^A-Z]', '', ciphertext.upper())
    best_key = ""
    best_plain = ""
    best_score = float('inf')

    try:
        with open(wordlist_path, "r") as file:
            words = [line.strip().upper() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Wordlist file not found: {wordlist_path}")
        return None, ""

    for word in words:
        decrypted = decrypt_vigenere(ciphertext, word)
        score = chi_squared_statistic(decrypted)
        if score < best_score:
            best_score = score
            best_key = word
            best_plain = decrypted

    if best_score < 150:
        return best_key, best_plain
    return None, ""

