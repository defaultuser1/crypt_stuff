from binascii import hexlify

def EVP_BytesToKey(password, salt, key_len, iv_len, count=1):
    """
    Derive the key and the IV from the given password and salt.
    """
    from hashlib import sha512
    from hashlib import sha1
    from hashlib import md5
    ncount = count
    dtot = None
    final = b''
    while True:
        if dtot:
            dtot = sha1(d + password + salt).digest()
        else:
            dtot = sha1(password + salt).digest()
        count = ncount
        d = dtot
        while count > 1:
            d = sha1(dtot).digest()
            dtot = d
            count -= 1
        final += d
        if len(final) >= (iv_len + key_len):
            break
    # while len(dtot)<(iv_len+key_len):
    #     d.append( sha1(d[-1] + password + salt).digest() )
    #     dtot += d[-1]
    return final[:key_len], final[key_len:key_len+iv_len]
    
print(hexlify(EVP_BytesToKey(b"test",b'AAAAAAAA',32,16)[0]))
print(hexlify(EVP_BytesToKey(b"test",b'AAAAAAAA',32,16)[1]))