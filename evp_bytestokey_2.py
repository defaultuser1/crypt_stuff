import hashlib, binascii
from passlib.utils.pbkdf2 import pbkdf1

def hasher(algo, data):
    hashes = {'md5': hashlib.md5, 'sha256': hashlib.sha256,
    'sha512': hashlib.sha512,'sha1': hashlib.sha1}
    h = hashes[algo]()
    h.update(data)

    return h.digest()

# pwd and salt must be bytes objects
def openssl_kdf(algo, pwd, salt, key_size, iv_size):
    if algo == 'md5':
        temp = pbkdf1(pwd, salt, 1, 16, 'md5')
    else:
        temp = b''

    fd = temp
    while len(fd) < key_size + iv_size:
        temp = hasher(algo, temp + pwd + salt)
        fd += temp

    key = fd[0:key_size]
    iv = fd[key_size:key_size+iv_size]

    print('salt=' + binascii.hexlify(salt).decode('ascii').upper())
    print('key=' + binascii.hexlify(key).decode('ascii').upper())
    print('iv=' + binascii.hexlify(iv).decode('ascii').upper())

    return key, iv

#openssl_kdf('md5', b'test', b'\xF6\x81\x8C\xAE\x13\x18\x72\xBD', 32, 16)
#openssl_kdf('sha256', b'test', b'\xF6\x81\x8C\xAE\x13\x18\x72\xBD', 32, 16)
openssl_kdf('sha1', b'test', b'\xF6\x81\x8C\xAE\x13\x18\x72\xBD', 32, 16)
