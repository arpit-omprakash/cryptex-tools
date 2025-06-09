from collections import Counter

def frequency_analysis(text):
    """
    Perform frequency analysis on the input text.

    Converts text to uppercase and counts the frequency of each alphabetic character.

    Args:
        text (str): The text to analyze.

    Returns:
        dict: A dictionary mapping each uppercase letter to its frequency count.
    """
    text = ''.join(filter(str.isalpha, text.upper()))
    return dict(Counter(text))
