import pytest
from cipherx.ciphers.caesar_cipher import *

c = CaesarCipher()

@pytest.mark.parametrize(('args', 'result'), (
('', 3),
(13, 13),
('a', 3),
))
def test_init(args, result):
    cs = CaesarCipher(args)
    assert cs.shift == result

@pytest.mark.parametrize(('text', 'encrypted'), (
('Hello there!', 'khoorwkhuh'),
('hellothere', 'khoorwkhuh'),
('hello there', 'khoorwkhuh'),
))
def test_encryption(text, encrypted):
    assert c.encrypt(text) == encrypted

@pytest.mark.parametrize(('text', 'decrypted'), (
('khoorw Khuh', 'hellothere'),
('kHoo rwkhuh!', 'hellothere'),
('khoorwkhuh', 'hellothere'),
))
def test_decryption(text, decrypted):
    assert c.decrypt(text) == decrypted
