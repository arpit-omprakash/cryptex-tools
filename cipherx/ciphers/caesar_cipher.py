class CaesarCipher:
    """
    A class for the Caesar Cipher.

    Attributes
    -----------
    alphabet : str
        A string that stores the working alphabet.
    shift : int
        The value by which the alphabet is shifted to
        the right for encryption (default is +3).
        Negative values indicate left shift.

    Methods
    --------
    encrypt(plaintext)
        Encrypts plaintext to produce ciphertext
    decrypt(ciphertext)
        Decrypts ciphertext to produce plaintext
    """

    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"

    def __init__(self, shift = 3):
        """
        Parameters
        -----------
        shift : int
            The value by which the alphabet is shifted to
            the right for encryption (default is +3).
            Negative values indicate left shift.
        """
        try:
            int(shift)
        except ValueError as e:
            print("Invalid shift entered, resetting shift to 3")
            shift = 3
        self.shift = int(shift)

    def encrypt(self, plaintext):
        """Function to encrypt strings using Caesar Cipher.

        The encryption works on only the alphanumeric English
        characters, any other characters present in the text
        are removed from the encrypted file.

        Parameters
        -----------
        plaintext : str
            The plaintext phrase to be encrypted.

        Returns
        --------
        str
            The encrypted ciphertext.
        """
        ciphertext = ""
        for letter in plaintext.lower():
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                cipher_index = (letter_index + self.shift) % len(self.alphabet)
                ciphertext += self.alphabet[cipher_index]
        return ciphertext

    def decrypt(self, ciphertext):
        """Function to decrypt strings using Caesar Cipher.

        The decryption works on only the alphanumeric English
        characters, any other characters present in the text
        are removed from the decrypted file.

        Parameters
        -----------
        ciphertext : str
            The ciphertext phrase to be decrypted.


        Returns
        --------
        str
            The decrypted plaintext message.
        """
        plaintext = ""
        for letter in ciphertext.lower():
            if letter in self.alphabet:
                letter_index = self.alphabet.index(letter)
                cipher_index = (letter_index - self.shift) % len(self.alphabet)
                plaintext += self.alphabet[cipher_index]
        return plaintext
