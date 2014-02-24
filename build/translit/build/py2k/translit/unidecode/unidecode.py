"""Pure Python version of unidecode()
"""
from importlib import import_module


TABLE_SIZE = 0x800
EMPTY_TABLE = [""] * TABLE_SIZE
TABLE_MODULE_FORMAT = ".".join(__name__.split(".")[:-1] + ["tables.0x{:02x}"])
SOURCE_CODE_LANGUAGE = "Python"

tables = {}


def unidecode(text: str) -> str:
    """Transliterate a Unicode object into an ASCII string.
    """
    return "".join([c if c < "\x80" else unidecode_char(c) for c in text])


def unidecode_char(c):
    block, index = divmod(ord(c), TABLE_SIZE)
    try:
        table = tables[block]
    except KeyError:
        try:
            table = import_module(TABLE_MODULE_FORMAT.format(block)).TABLE
        except ImportError:
            table = EMPTY_TABLE
        tables[block] = table
    return table[index]
