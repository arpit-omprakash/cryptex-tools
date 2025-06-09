import click
from ..utils.cipher_loader import get_cipher_info, load_ciphers
from ..cryptanalysis.frequency_analysis import frequency_analysis
from ..cryptanalysis.brute_force_caesar import brute_force_caesar
from ..cryptanalysis.vigenere_crack import crack_vigenere_with_auto_align, crack_vigenere_with_dictionary

# Load all available cipher modules at startup
ciphers = load_ciphers()

@click.group()
def cli():
    """
    Cryptex Tools: Educational Cryptography Toolkit

    This is the main entry point for the cryptex_tools command-line interface.
    Provides commands for cryptanalysis, encryption, decryption, and listing ciphers.
    """
    pass

@cli.group()
def analyze():
    """
    Cryptanalysis tools group.

    Contains subcommands for analyzing ciphertexts, such as frequency analysis,
    brute-force attacks, and Vigenère cipher cracking.
    """
    pass

@analyze.command("freq")
@click.option("--text", required=True, help="Text to analyze")
def analyze_freq(text):
    """
    Perform frequency analysis on the provided text.

    Args:
        text (str): The text to analyze.

    Prints the frequency of each character in the text.
    """
    freq = frequency_analysis(text)
    for char, count in sorted(freq.items()):
        click.echo(f"{char}: {count}")

@analyze.command("brute-caesar")
@click.option("--text", required=True, help="Ciphertext to brute-force")
def analyze_caesar(text):
    """
    Brute-force all possible Caesar cipher shifts on the given ciphertext.

    Args:
        text (str): The ciphertext to brute-force.

    Prints all possible plaintexts for each Caesar shift.
    """
    results = brute_force_caesar(text)
    for shift, attempt in results.items():
        click.echo(f"{shift:2d}: {attempt}")

@analyze.command("crack-vigenere")
@click.option("--text", required=True, help="Ciphertext to crack")
@click.option("--wordlist", default=None, help="Path to dictionary file for key guesses")
@click.option("--partial-key", default="", help="Optional known part of key")
def crack_vigenere_cmd(text, partial_key, wordlist):
    """
    Attempt to crack a Vigenère cipher using either a partial key or a dictionary.

    Args:
        text (str): The ciphertext to crack.
        partial_key (str): Optional known part of the key.
        wordlist (str): Optional path to a dictionary file for key guesses.

    Prints the guessed key and decrypted text if successful.
    """
    key = None
    if partial_key:
        key, plain = crack_vigenere_with_auto_align(text, partial_key)
    elif wordlist:
        key, plain = crack_vigenere_with_dictionary(text, wordlist)
    else:
        key, plain = crack_vigenere_with_dictionary(text)
    if key:
        click.echo(f"[+] Guessed key: {key}")
        click.echo(f"[+] Decrypted text:\n{plain}")
    else:
        click.echo("[-] Cracking failed.")

@cli.command(name="list-ciphers")
def list_ciphers_cmd():
    """
    List all available ciphers with their descriptions and key types.

    Prints each cipher's ID, name, description, and key type.
    """
    for cipher in get_cipher_info():
        click.echo(f"{cipher['id']} - {cipher['name']}")
        click.echo(f"  {cipher['description']}")
        click.echo(f"  Key type: {cipher['key_type']}")
        click.echo("")

@cli.command()
@click.argument("cipher_name", type=click.Choice(list(ciphers.keys())))
@click.option("--text", help="Text to encrypt")
@click.option("--file", type=click.Path(exists=True), help="Path to plaintext file to encrypt")
@click.option("--key", help="Key for cipher (type depends on cipher)")
@click.option("--output", type=click.Path(), help="Output file path (for file encryption)")
def encrypt(cipher_name, text, file, key, output):
    """
    Encrypt text or file using the selected cipher.

    Args:
        cipher_name (str): The name of the cipher to use.
        text (str): The plaintext to encrypt.
        file (str): Path to a plaintext file to encrypt.
        key (str): The key for the cipher.
        output (str): Output file path for encrypted content.

    Writes the ciphertext to the output file or prints it to the console.
    """
    cipher = ciphers[cipher_name]

    if file:
        with open(file, "r", encoding="utf-8") as f:
            plaintext = f.read()
        # Convert key if needed (try int, tuple, or string)
        key_val = _parse_key(key, cipher)
        ciphertext = cipher.encrypt(plaintext, key_val)
        if output:
            with open(output, "w", encoding="utf-8") as f_out:
                f_out.write(ciphertext)
            click.echo(f"Encrypted content written to {output}")
        else:
            click.echo(ciphertext)

    elif text:
        key_val = _parse_key(key, cipher)
        ciphertext = cipher.encrypt(text, key_val)
        click.echo(ciphertext)
    else:
        click.echo("Please provide --text or --file to encrypt.")

@cli.command()
@click.argument("cipher_name", type=click.Choice(list(ciphers.keys())))
@click.option("--text", help="Text to decrypt")
@click.option("--file", type=click.Path(exists=True), help="Path to ciphertext file to decrypt")
@click.option("--key", help="Key for cipher (type depends on cipher)")
@click.option("--output", type=click.Path(), help="Output file path (for file decryption)")
def decrypt(cipher_name, text, file, key, output):
    """
    Decrypt text or file using the selected cipher.

    Args:
        cipher_name (str): The name of the cipher to use.
        text (str): The ciphertext to decrypt.
        file (str): Path to a ciphertext file to decrypt.
        key (str): The key for the cipher.
        output (str): Output file path for decrypted content.

    Writes the plaintext to the output file or prints it to the console.
    """
    cipher = ciphers[cipher_name]

    if file:
        with open(file, "r", encoding="utf-8") as f:
            ciphertext = f.read()
        key_val = _parse_key(key, cipher)
        plaintext = cipher.decrypt(ciphertext, key_val)
        if output:
            with open(output, "w", encoding="utf-8") as f_out:
                f_out.write(plaintext)
            click.echo(f"Decrypted content written to {output}")
        else:
            click.echo(plaintext)

    elif text:
        key_val = _parse_key(key, cipher)
        plaintext = cipher.decrypt(text, key_val)
        click.echo(plaintext)
    else:
        click.echo("Please provide --text or --file to decrypt.")

def _parse_key(key, cipher_module):
    """
    Parse the key string into the appropriate type for the cipher.

    Args:
        key (str): The key as a string.
        cipher_module: The cipher module, which provides key type info.

    Returns:
        The key converted to the appropriate type (int, tuple, str, or None).

    Raises:
        click.BadParameter: If the key cannot be converted as required.
    """
    key_type = cipher_module.get_info().get("key_type", "str")
    if key_type == "int":
        try:
            return int(key)
        except Exception:
            raise click.BadParameter(f"Key must be an integer for {cipher_module.get_info()['name']}")
    elif key_type == "tuple[int, int]":
        # Expect key as "a,b"
        try:
            parts = key.split(",")
            return (int(parts[0]), int(parts[1]))
        except Exception:
            raise click.BadParameter(f"Key must be two integers separated by a comma for {cipher_module.get_info()['name']}")
    elif key_type == "None":
        return None
    else:
        return key

if __name__ == '__main__':
    # Entry point for running the CLI directly
    cli()