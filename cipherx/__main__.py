doc_string = """
Encrypt or Decrypt a provided file.

The program takes in one file as an input, encrypts (or decrypts)
it and saves the output as another file.
-----------------------------------------------
The following cipher options are supported till now:
1 = Caesar Cipher
2 = ROT 13 Cipher
-----------------------------------------------
"""

import argparse

# Argument Parsing
parser = argparse.ArgumentParser(prog='cipherx',
                                formatter_class=argparse.RawDescriptionHelpFormatter,
                                description=doc_string)
parser.add_argument('-cipher',
                    default='1',
                    type=int,
                    choices=range(1,3),
                    help='Cipher to use for encryption or decryption (default = 1)')
parser.add_argument('-conversion',
                    default='encrypt',
                    type=str,
                    choices=['encrypt', 'decrypt'],
                    help='Specify whether to encrypt or decrypt said file (default = encrypt)')
parser.add_argument('-shift',
                    default=3,
                    type=int,
                    choices=range(1, 37),
                    help='The shift for Caesar Cipher, can range from 1 to 36 (default = 3)')
parser.add_argument('in_file',
                    type=argparse.FileType('r', encoding='UTF-8'),
                    help='Path to input file', metavar='I')
parser.add_argument('out_file',
                    type=argparse.FileType('w', encoding='UTF-8'),
                    help='Path to output file (file is created if not existing)', metavar='O')
args  = parser.parse_args()


def apply_cipher(func):
    """Function to apply a supplied cipher function.

    The function works with strings explicitly. Should be invoked
    using functions that work with strings.
    The text is read from the earlier provided input file.
    The output is written to the provided output file.

    Parameters
    -----------
    func : function
        An encryption or decryption function
    """
    text = args.in_file.read()
    changed_text = func(text)
    args.out_file.write(changed_text)

def apply_caesar_cipher(shft):
    """Function to apply the Caesar Cipher.

    Parameters
    -----------
    shft : int
        The shift for Caesar Cipher
    """
    from cipherx.caesar_cipher import CaesarCipher
    c = CaesarCipher(shft)
    if args.conversion == 'encrypt':
        apply_cipher(c.encrypt)
    else:
        apply_cipher(c.decrypt)

# Program logic
if args.cipher == 1:
    apply_caesar_cipher(args.shift)
elif args.cipher == 2:
    apply_caesar_cipher(13)
