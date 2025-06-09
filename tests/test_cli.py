import unittest
from click.testing import CliRunner
from src.cryptex_tools.cli.main import cli

class TestCipherCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_caesar_encrypt_decrypt(self):
        # Encrypt
        result = self.runner.invoke(cli, [
            "encrypt", "caesar cipher",
            "--text", "HELLO",
            "--key", "3"
        ])
        self.assertEqual(result.exit_code, 0)
        ciphertext = result.output.strip()
        self.assertNotIn("HELLO", ciphertext.upper())

        # Decrypt
        result2 = self.runner.invoke(cli, [
            "decrypt", "caesar cipher",
            "--text", ciphertext,
            "--key", "3"
        ])
        self.assertEqual(result2.exit_code, 0)
        self.assertIn("HELLO", result2.output.strip().upper())

    def test_atbash_roundtrip(self):
        plaintext = "TESTING123"
        result = self.runner.invoke(cli, [
            "encrypt", "atbash cipher",
            "--text", plaintext
        ])
        self.assertEqual(result.exit_code, 0)
        ciphertext = result.output.strip()

        result2 = self.runner.invoke(cli, [
            "decrypt", "atbash cipher",
            "--text", ciphertext
        ])
        self.assertEqual(result2.exit_code, 0)
        self.assertIn("TESTING", result2.output.strip().upper())

    def test_missing_text_error(self):
        result = self.runner.invoke(cli, [
            "encrypt", "caesar cipher"
        ])
        self.assertIn("Please provide", result.output)
        self.assertNotEqual(result.exit_code, "0")

if __name__ == "__main__":
    unittest.main()
