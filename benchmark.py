"""
This module is  a global execution time benchmark  for the key generation, crypt
and decrypt benchmarks.
"""

import benchmarks.key_generation
import benchmarks.crypt_speed

from utils.table import markdown_table
from utils.humanize import format_time


# Key generation benchmarks
bench_key = benchmarks.key_generation.run()
print(
    markdown_table(
        ["Number of bits (2**n)", "Time"],
        list(map(lambda x: [x[0], format_time(x[1])], bench_key)),
    )
)

bench_crypt = benchmarks.crypt_speed.run()
print(
    markdown_table(
        ["Data lenght", "Crypt (time)", "Decrypt (time)"],
        list(map(lambda x: [x[0], format_time(x[1]), format_time(x[2])], bench_crypt)),
    )
)
