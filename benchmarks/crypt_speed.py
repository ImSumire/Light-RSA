"""
This module  is  used to  test  the encryption  and decryption  process for  the
benchmarking, please run `python3 benchmark.py` for it.
"""

from time import perf_counter
from lorem import get_sentence
from colorama import Fore, Style

# pylint: disable=import-error
from yaal import generate_keys, crypt, decrypt


# pylint: disable=missing-function-docstring
def run():
    print(f"{Fore.BLUE}[ INFO ] Estimated time : ~3.4 seconds")

    print("[ INFO ] Lorem ipsum generation...")
    sentence = get_sentence(1000)
    print("[ INFO ] Lorem ipsum generation done!")

    print("[ INFO ] Generating keys...")
    public_key, private_key = generate_keys()
    print(f"[ INFO ] Generating keys done!\n{Style.RESET_ALL}")

    lengths = range(1, len(sentence) + 1, 5000)
    durations = []
    for lenght in lengths:
        data = sentence[:lenght]

        crypt_start = perf_counter()
        temp = crypt(data, public_key)
        crypt_end = perf_counter() - crypt_start

        decrypt_start = perf_counter()
        decrypt(temp, private_key)
        decrypt_end = perf_counter() - decrypt_start
        durations.append([lenght, crypt_end, decrypt_end])

    return durations
