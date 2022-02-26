from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

key = os.urandom(16)
cipher = AES.new(key, AES.MODE_CBC)

print(key)
print(cipher.iv)
print(cipher.encrypt(pad(open("flag.txt", "rb").read(), 16)))

# b'M\x1f\xe5\xe3\xa00:?\x975\xc0}\x99N\x9a\xa5'
# b'\xa4\x1f7\xbb\x07\xdfU\xdd3\xd0\x81 \x8b^\xba_'
# b'+\xb5\xa6\x05\xc5t\xee\x1c9\xc2\xb3$\xf9\xb0/\x11\x80\xc1iL\xef\xd7Y\xc7\x1a\x85\xc1\xe5\xc0\xa4\xed\xfb#\xe8L\xc173N\xd6=\xf0\x06\xbc5);\xc9=^<@cn\x0bl\xca\x1bp\n\x11j-C'