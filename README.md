# 🔐 Cryptex Tools

**cryptex_tools** is an educational cryptography toolkit written in Python, designed for learners and hobbyists. It demonstrates classical ciphers, basic cryptanalysis tools, and allows users to experiment with encryption and decryption via a simple command-line interface (CLI).

---

## 📦 Features

- Classical Ciphers:
  - Caesar, Vigenère, Atbash, Affine, Pigpen, ROT13, Keyboard Shift, Playfair, Rail Fence
- Cryptanalysis Tools:
  - Frequency analysis
  - Vigenère cipher cracking (with auto alignment and dictionary support)
  - Caesar cipher cracking (brute force)
- File-based encryption/decryption support
- Modular, extensible architecture with clean CLI powered by `click`

---

|||
|-|-|
|Author   | Arpit Omprakash             |
|License  | MIT License                 |
|Homepage | https://github.com/arpit-omprakash/cryptex-tools |

---

## 📁 Project Structure

cryptex-tools/  
├── src/cryptex_tools/  
│ ├── ciphers/ # Individual cipher modules  
│ ├── cli/ # CLI entry point and command setup  
│ ├── cryptanalysis/ # Cryptanalysis tools and helpers  
│ ├── utils/ # Utility functions like cipher loader  
├── tests/ # Unit tests for ciphers and CLI  
├── README.md  
└── requirements.txt  

---

## Supported Ciphers

`cryptex_tools` currently supports the following ciphers (see `src/cryptex_tools/ciphers`):

1. **Caesar Cipher** – Shifts each letter by a fixed number of positions.
2. **ROT13 Cipher** – Caesar cipher with a fixed shift of 13.
3. **Affine Cipher** – Encrypts using the formula `(a*x + b) mod 26`.
4. **Atbash Cipher** – Substitutes each letter with its reverse in the alphabet.
5. **Keyboard Shift Cipher** – Shifts letters according to their position in QWERTY keyboard rows.
6. **Pigpen Cipher (Unicode)** – Substitutes each letter with a Unicode Pigpen symbol.
7. **Playfair Cipher** – Digraph substitution cipher using a 5x5 matrix based on a keyword.
8. **Rail Fence Cipher** – Transposition cipher writing text in a zigzag pattern.
9. **Vigenère Cipher** – Uses a keyword to shift letters; the keyword repeats to match text length.

---


## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/arpit-omprakash/cryptex-tools.git
cd cryptex-tools
```

### 2. Set up virtual environment and install

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Install the package
pip install -e .
```

### 3. Run the CLI

```bash
# Help for the program
python -m cryptex_tools --help

# Help for a specific submenu
python -m cryptex_tools encrypt --help 
```

---

## 🛠 Usage Examples 

### Encrypt using Caesar Cipher

```bash
$ python -m cryptex_tools encrypt "caesar cipher" --text "HELLO" --key 3

# Output
$ KHOOR
```

### Decrypt using Vigenere Cipher

```bash
$ python -m cryptex_tools decrypt "vigenere cipher" --text "RIJVS" --key "KEY"

# Output
$ HELLO
```

### Crack Vigenere Cipher using Dictionary

```bash
$ python -m cryptex_tools analyze crack-vigenere --text "LLKJMLSQGJWTYI"

# Output
$ [+] Guessed key: SECRET
$ [+] Decrypted text:
$ THISISAMESSAGE
```

## ✅ Running Tests

To run all tests:

```bash
tests\run_tests.bat # Windows

# or manually
python -m unittest discover -s tests
```

## ✨ Contributing

Pull Requests, Feedback, and Suggestions are Welcome!

## 📜 License

```
MIT License

Copyright (c) 2025 Arpit Omprakash

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---