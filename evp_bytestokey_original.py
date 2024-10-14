from binascii import hexlify

def EVP_BytesToKey(password, salt, key_len, iv_len):
    """
    Derive the key and the IV from the given password and salt.
    """
    from hashlib import md5
    dtot =  md5(password + salt).digest()
    d = [ dtot ]
    while len(dtot)<(iv_len+key_len):
        d.append( md5(d[-1] + password + salt).digest() )
        dtot += d[-1]
    return dtot[:key_len], dtot[key_len:key_len+iv_len]

print(hexlify(EVP_BytesToKey(b"test",b'AAAAAAAA',32,16)[0]))
print(hexlify(EVP_BytesToKey(b"test",b'AAAAAAAA',32,16)[1]))