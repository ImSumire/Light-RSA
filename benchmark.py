from rsa import generate_keys, crypt, decrypt
from time import perf_counter
# import psutil


def markdown_table(categories, table):
    """
    Creation of  a table in markdown from the list of categories and the content
    of the table. All elements are centered thanks to `|:-:|`.
    """
    assert len(categories) == len(table[0])

    data = "| " + " | ".join(categories) + " |\n"  # Categories
    data += "|:-:" * len(categories) + "|\n"  # Separators
    for column in table:
        data += "| " + " | ".join([str(item) for item in column]) + " |\n"
    return data


# List of lengths to be processed
lenghts = [10, 100, 500, 1000, 5000, 10000, 50000, 100000, 150000, len(data) - 1]

# Table structure
categories = ["size", "crypt", "decrypt"]
table = []

data = ""  # Please implement your own data

# Benchmark loop
for lenght in lenghtes:
    infos = [lenght]

    temp_data = data[:lenght]
    # start_mem = psutil.Process().memory_info().rss

    public_key, private_key = generate_keys()

    start = perf_counter()
    encrypted_data = crypt(temp_data, public_key)
    infos.append(str(round((perf_counter() - start) * 1000, 4)) + "ms")

    start = perf_counter()
    decrypted_data = decrypt(encrypted_data, private_key)
    infos.append(str(round((perf_counter() - start) * 1000, 4)) + "ms")

    # infos.append(str((psutil.Process().memory_info().rss - start_mem) / (1024 * 1024)) + "MB")
    table.append(infos)

print(main(categories, table))
