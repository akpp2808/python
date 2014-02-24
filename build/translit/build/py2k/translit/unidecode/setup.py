#!/usr/bin/env python3

import os
import re
import sys

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

from generate_table_h import generate_table_h


if __name__ == "__main__":
    PYX_FILENAME = "_unidecode.pyx"
    USE_LEGACY_UNICODE_API_RE = re.compile(
        r"(^DEF USE_LEGACY_UNICODE_API\s*=\s*)(True|False)", re.M)

    generate_table_h()

    with open(PYX_FILENAME) as f:
        contents = f.read()
    new_contents = None
    match = USE_LEGACY_UNICODE_API_RE.search(contents)
    use_legacy_unicode_api = eval(match.group(2))
    if sys.version_info >= (3, 3):
        if use_legacy_unicode_api:
            new_contents = USE_LEGACY_UNICODE_API_RE.sub(r"\1False", contents)
    else:
        if not use_legacy_unicode_api:
            new_contents = USE_LEGACY_UNICODE_API_RE.sub(r"\1True", contents)
    if new_contents is not None:
        use_legacy_unicode_api = not use_legacy_unicode_api
        print("USE_LEGACY_UNICODE_API =", use_legacy_unicode_api)
        with open(PYX_FILENAME, "w") as f:
            f.write(new_contents)

    if os.name == "posix":
        EXTRA_COMPILE_ARGS = ["-Ofast"]
    else:
        EXTRA_COMPILE_ARGS = []

    setup(
        cmdclass={"build_ext": build_ext},
        ext_modules=[
            Extension("_unidecode", [PYX_FILENAME],
            extra_compile_args=EXTRA_COMPILE_ARGS)
        ],
    )
