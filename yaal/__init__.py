"""
RSA : https://en.wikipedia.org/wiki/RSA_(cryptosystem)
Euler's Phi : https://en.wikipedia.org/wiki/Euler%27s_totient_function

Lib imports:
- gmpy2 : https://pypi.org/project/gmpy2/
  - `next_prime` : return int: x, where x is the next prime number
  - `invert` : return int: x, where a * x == 1 mod b
- secrets : https://pypi.org/project/secrets/
  - `randbits` : return int: x, where x is a random number between 0 and 2**bits

Just in case:
- sympy : https://pypi.org/project/sympy/
  - `nextprime` as next_prime
  - `mod_inverse` as invert
- random
  - `random` as randbits
"""

__all__ = [
    "generate_keys",
    "crypt",
    "decrypt",
]

# pylint: disable=invalid-name

### Next prime and invert import
try:
    from gmpy2 import next_prime, invert

except ImportError:
    print("WARNING: gmpy2 module not available : pip install gmpy2")
    from sympy import nextprime as next_prime, mod_inverse as invert


### Randbits import
try:
    from secrets import randbits


except ImportError:
    print("WARNING: secrets module not available: pip install secrets")
    from random import random

    def randbits(n: int):
        """Returns a random number between 0 and 2**n."""
        return int(random() * (2**n))


def generate_keys(bits: int = 256):
    """
    -bits: Minimum recommended: 64
    Generates the two  keys from two random primes p and q, using the same steps
    as the standard RSA key generation process.
    """
    p = next_prime(randbits(bits // 2))
    q = next_prime(randbits(bits // 2))
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # No common factor with phi
    d = invert(e, phi)
    return ((e, n), (d, n))


def crypt(data: str, key: tuple):
    """
    -key: The public key
    Encrypts data using the RSA algorithm. The variable data is converted into a
    list of integers, then each integer is encrypted using the public key.
    """
    e, n = key
    result = [int(pow(ord(c), e, n)) for c in data]
    return result


def decrypt(data: str, key: tuple):
    """
    -key: The private key
    Decrypts the  encrypted data using the  RSA  algorithm. Each integer in the
    data  list is decrypted using  the  private key,  and   then  the decrypted
    integers are converted to characters to form the original message.
    """
    d, n = key
    data = [chr(pow(c, d, n)) for c in data]
    return "".join(data)
