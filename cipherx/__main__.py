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

# Argument Parsing
def parsing():
    """Function to parse inputs.

    Returns
    --------
    Namespace
        A Namespace object containing all the inputs passed to the program.
    """
    import argparse
    parser = argparse.ArgumentParser(prog='cipherx',
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    description=doc_string)
    parser.add_argument('-cipher', '-c',
                        default='1',
                        type=int,
                        choices=range(1,3),
                        help='Cipher to use for encryption or decryption (default = 1)')
    parser.add_argument('-decrypt', '-d',
                        action='store_true',
                        help='Turn this flag on to enter decrypt mode')
    parser.add_argument('-shift', '-s',
                        default=3,
                        type=int,
                        choices=range(1, 37),
                        help='The shift for Caesar Cipher, can range from 1 to 36 (default = 3)')
    parser.add_argument('in_file',
                        type=argparse.FileType('r', encoding='UTF-8'),
                        help='Path to input file',
                        metavar='I')
    parser.add_argument('out_file',
                        type=argparse.FileType('w', encoding='UTF-8'),
                        help='Path to output file (file is created if not existing)',
                        metavar='O')
    return parser.parse_args()


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
    from cipherx.ciphers.caesar_cipher import CaesarCipher
    c = CaesarCipher(shft)
    if args.decrypt:
        apply_cipher(c.decrypt)
    else:
        apply_cipher(c.encrypt)

# Program logic
if __name__ == '__main__':
    args = parsing()
    if args.cipher == 1:
        apply_caesar_cipher(args.shift)
    elif args.cipher == 2:
        apply_caesar_cipher(13)
