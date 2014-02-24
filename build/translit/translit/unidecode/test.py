#!/usr/bin/env python3

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))
import unittest
import warnings

try:
    from translit.unidecode._unidecode import unidecode, SOURCE_CODE_LANGUAGE
except ImportError:
    from translit.unidecode.unidecode import unidecode, SOURCE_CODE_LANGUAGE
else:
    from translit.unidecode.unidecode import unidecode as unidecode_py


class TestUnidecode(unittest.TestCase):
    def test_samples(self):
        tests = [
            ("Étude", "Etude"),
            ("北亰", "Bei Jing "),
            ("500\xa0€", "500 EUR"),
            ("☺", ":-)"),
        ]
        for text, result in tests:
            self.assertEqual(unidecode(text), result)

    def test_result(self):
        for n in range(128):
            c = chr(n)
            self.assertEqual(c, unidecode(c))
        for n in range(128, sys.maxunicode + 1):
            c = chr(n)
            self.assertNotEqual(c, unidecode(c))

    def test_encode_to_ascii(self):
        for n in range(sys.maxunicode + 1):
            unidecode(chr(n)).encode("ascii")

    if SOURCE_CODE_LANGUAGE == "Cython":
        def test_cython(self):
            self.assertIsNot(unidecode, unidecode_py)
            for n in range(sys.maxunicode + 1):
                c = chr(n)
                self.assertEqual(unidecode(c), unidecode_py(c))
    else:
        warnings.warn("Cython version is unavailable")


if __name__ == "__main__":
    unittest.main()
