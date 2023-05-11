"""
This module  is used to  test the key generation  process for the  benchmarking,
please run `python3 benchmark.py` for it.
"""

from time import perf_counter
from colorama import Fore, Style

# pylint: disable=import-error
from yaal import generate_keys


# pylint: disable=missing-function-docstring
def run():
    print(f"{Fore.BLUE}[ INFO ] Estimated time : between 0.8 and 3.2 seconds\n{Style.RESET_ALL}")

    lengths = range(1, 13)
    durations = []
    for bit_number in lengths:
        start = perf_counter()
        generate_keys(bits=2**bit_number)
        durations.append([2**bit_number, perf_counter() - start])

    return durations
