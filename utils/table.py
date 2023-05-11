"""
This is the main function of the script. It creates a table in markdown from the
list of categories and the content of the table.
"""


def markdown_table(categories, table):
    """
    Creation of a table in markdown, like this:
    | Categories | Categories |
    | :-: | :-: |
    | Value | Value |
    """
    assert len(categories) == len(table[0])

    data = "| " + " | ".join(categories) + " |\n"  # Categories
    data += "|:-:" * len(categories) + "|\n"  # Separators
    for column in table:
        data += "| " + " | ".join([str(item) for item in column]) + " |\n"
    return data
