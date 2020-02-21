#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function

import base64
import binascii
import collections
import fractions
import numbers
import random


sysrandom = random.SystemRandom()


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m


def miller_rabin(n, tests=50):
    assert isinstance(n, numbers.Integral)
    if n <= 3:
        return n == 2 or n == 3
    if n & 1 == 0:
        return False
    d = n - 1
    t = (1, d)
    s = 0
    while (d & 1) == 0:
        d >>= 1
        s += 1
    for _ in range(tests):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
        if x not in t:
            for _ in range(s - 1):
                x = pow(x, 2, n)
                if x == 1:
                    return False
                if x == n - 1:
                    break
            else:
                return False
    return True


def gen_random_prime(num_bits):
    lim1 = 1 << num_bits
    lim2 = lim1 << 1
    r = sysrandom.randrange(lim1, lim2)
    while r < lim2:
        if miller_rabin(r):
            return r
        r += 1
    assert False


def gen_coprime(n):
    assert isinstance(n, numbers.Integral)
    assert n > 2

    while True:
        r = sysrandom.randrange(2, n)
        if fractions.gcd(r, n) == 1:
            return r


class Key(object):
    def __init__(self, e, m):
        self.e = e
        self.m = m

    def __repr__(self):
        return 'Key(e={e}, m={m})'.format(e=hex(self.e), m=hex(self.m))

    @classmethod
    def encode_number(cls, n):
        res = '{:x}'.format(n)
        if len(res) & 1:
            res = '0' + res
        return res


KeyPair = collections.namedtuple('KeyPair', ('public_key', 'private_key'))


def gen_rsa_key(num_bits):
    p = gen_random_prime(num_bits)
    q = gen_random_prime(num_bits)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = gen_coprime(phi_n)
    d = modinv(e, phi_n)
    return KeyPair(public_key=Key(e=e, m=n), private_key=Key(e=d, m=n))


def rsa_encrypt(msg, public_key):
    msg_int = int(binascii.hexlify(msg), 16)
    assert msg_int < public_key.m
    encoded_msg = pow(msg_int, public_key.e, public_key.m)
    return binascii.unhexlify(Key.encode_number(encoded_msg).encode())


def rsa_decrypt(msg, private_key):
    return rsa_encrypt(msg, private_key)


if __name__ == '__main__':
    keypair = gen_rsa_key(128)
    print('Chave pública: {public_key}'.format(public_key=keypair.public_key))
    print('Chave privada: {private_key}'.format(private_key=keypair.private_key))    
    print()

    msg = b'hakuna matata'
    encoded_msg = rsa_encrypt(msg, keypair.public_key)
    decoded_msg = rsa_decrypt(encoded_msg, keypair.private_key)
    
    print('Mensagem original: {msg}'.format(msg=msg))
    print('Mensagem encriptada (em base64): {encoded_msg}'.format(encoded_msg=base64.b64encode(encoded_msg)))
    print('Mensagem decriptada: {decoded_msg}'.format(decoded_msg=decoded_msg))    
