import unittest
from src.cryptex_tools.utils.cipher_loader import load_ciphers

CIPHERS_DIR = "src/ciphers"
CIPHERS = load_ciphers()

class AllCipherTests(unittest.TestCase):
    def test_all_ciphers_encrypt_decrypt(self):
        for name, cipher in CIPHERS.items():
            with self.subTest(cipher=name):
                key_type = cipher.get_info().get("key_type", "str")
                key = get_sample_key(key_type)
                encrypted = cipher.encrypt("HELLO WORLD", key)
                decrypted = cipher.decrypt(encrypted, key)
                self.assertIsInstance(encrypted, str)
                self.assertIsInstance(decrypted, str)
                # remove spaces and compare case-insensitively
                self.assertIn("HELLOWORLD", decrypted.replace(" ", "").upper())

def get_sample_key(key_type):
    if key_type == "int":
        return 3
    elif key_type == "tuple[int, int]":
        return (5, 8)  # a and b for affine
    elif key_type == "None":
        return None
    else:
        return "KEYWORD"

if __name__ == "__main__":
    unittest.main()
