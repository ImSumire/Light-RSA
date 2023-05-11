"""
This module is used to format the time.
"""


# pylint: disable=missing-function-docstring
def format_time(seconds):
    units = ["s", "ms", "µs", "ns", "ps"]

    i = 0
    while seconds < 1 and i < len(units) - 1:
        seconds *= 1000
        i += 1

    return f"{round(seconds, 2)} {units[i]}"
