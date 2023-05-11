# Yet Another Asymmetric Lib (YAAL)

This library provides an ultra-simplified version of the RSA encryption algorithm for educational and demonstration purposes. The RSA algorithm is a widely-used public-key cryptography system that allows secure transmission of information over unsecured channels. The encryption and decryption process is based on the use of two keys, a public key and a private key, which are mathematically related but cannot be derived from one another.

This library requires the gmpy2 and secrets modules for optimal performance, but fallback options using sympy and random are available if these modules are not available on the system.

## Installation

```bash
pip install -r requirements.txt
```

## Usage

To use this library, import the generate_keys, crypt, and decrypt functions as follows:

```py
from yaal import generate_keys, crypt, decryption  # or `__all__`
```
### Generating keys

To generate a pair of public and private keys, use the generate_keys function with a specified number of bits (minimum recommended is 64):

```py
public_key, private_key = generate_keys(bits=256)
```

The generate_keys function returns a tuple containing the public key (e, n) and the private key (d, n).

### Encryption

To encrypt a message using the public key, use the crypt function:

```py
encrypted_data = crypt("Hello World!", public_key)
```

The crypt function returns a list of integers representing the encrypted message.

### Decryption

To decrypt the encrypted message using the private key, use the decrypt function:

```py
decrypted_data = decrypt(encrypted_data, private_key)
```

The decrypt function returns the original message as a string.

## Benchmarking

To start the benchmark, just run :
```py
python3 benchmark.py
```
