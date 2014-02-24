#!/usr/bin/env python3

import os
import sys
SCRIPT_DIR = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(SCRIPT_DIR, "../.."))

from translit.unidecode.unidecode import unidecode as unidecode_py


def double_quoted_repr(s):
    s = ascii(s)[1:-1]
    if '"' in s:
        s = s.replace('"', '\\"')
    return '"{}"'.format(s)


def generate_table_h(overwrite=False):
    data_h_file = os.path.join(SCRIPT_DIR, "table.h")

    if os.path.isfile(data_h_file) and not overwrite:
        return

    max_code_point = None
    max_len = 0

    for n in range(sys.maxunicode):
        if unidecode_py(chr(n)):
            max_code_point = n

    with open(data_h_file, "w") as f:
        print("const char *TABLE[] = {", file=f)
        for n in range(max_code_point + 1):
            s = unidecode_py(chr(n))
            if len(s) > max_len:
                max_len = len(s)
            fmt = " {}"
            if n < max_code_point:
                fmt += ","
            print(fmt.format(double_quoted_repr(s)), file=f)
        print("};\n", file=f)
        print("const size_t TABLE_SIZE = sizeof (TABLE) / sizeof (char *);",
              file=f)
        print("const size_t MAX_LEN = {};".format(max_len), file=f)

    print("{!r} has been generated.".format(data_h_file))


if __name__ == "__main__":
    sys.exit(generate_table_h(overwrite=True))
