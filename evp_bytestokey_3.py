# require pycryptodome
import Crypto.Protocol
import Crypto.Protocol.KDF
from binascii import hexlify
prev = b''
final = b''
keylen = 32
ivlen = 16
while len(final) < (keylen + ivlen):
    prev = Crypto.Protocol.KDF.PBKDF1(prev+b"test",b"AAAAAAAA",20,1000,Crypto.Hash.SHA1)
    final += prev
print(hexlify(final[:keylen]))
print(hexlify(final[keylen:keylen+ivlen]))