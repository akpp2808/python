#!/usr/bin/env python3
import unittest
from collections import namedtuple

import translit #@UnusedImport


Result = namedtuple("Result", ("text", "encoding"))


class TestTranslit(unittest.TestCase):
    round_trip_tests = {
        "en": [
            ("“It’s wrong to be pissed at a black president…”", [
                Result(
                    '"It\'s wrong to be pissed at a black president..."',
                    "latin-1"
                ),
            ]),
        ],
        "fr": [
            ("–\xa0Pourquoi ça t’intéresse tant\u202f?\n"
             "–\xa0C’est tellement «\u202fparfait\u202f»…", [
                Result(
                    "- Pourquoi ca t'interesse tant ?\n"
                    "- C'est tellement \"parfait\"...",
                    "ascii"
                ),
                Result(
                    "-\xa0Pourquoi ça t'intéresse tant\xa0?\n"
                    "-\xa0C'est tellement «\xa0parfait\xa0»...",
                    "latin-1"
                ),
                Result(
                    "–\xa0Pourquoi ça t’intéresse tant\xa0?\n"
                    "–\xa0C’est tellement «\xa0parfait\xa0»…",
                    "cp1252"
                ),
            ]),
            ("ŒUF Œuf œuf CŒUR Cœur cœur", [
                Result(
                    "OEUF Oeuf oeuf COEUR Coeur coeur",
                    "latin-1"
                ),
                Result(
                    "ŒUF Œuf œuf CŒUR Cœur cœur",
                    "iso8859-15"
                ),
            ]),
        ],
    }

    one_way_tests = {
        "fr": [
            ("harcelé", Result("harcele", "ascii")),
            ("harcèle", Result("harcele", "ascii")),
        ],
    }

    def test_encode(self):
        for _, tests in self.round_trip_tests.items():
            for text, results in tests:
                for result in results:
                    encoded_result = result.text.encode(result.encoding)
                    encoded_text = text.encode(result.encoding + "/translit")
                    self.assertEqual(encoded_text, encoded_result)

    def test_decode(self):
        for language, tests in self.round_trip_tests.items():
            for text, results in tests:
                for result in results:
                    encoded_result = result.text.encode(result.encoding)
                    decoded_text = encoded_result.decode(
                        "{}/translit/{}".format(result.encoding, language))
                    self.assertEqual(decoded_text, text)

    def test_one_way(self):
        for language, tests in self.one_way_tests.items():
            for text, result in tests:
                encoded_result = result.text.encode(result.encoding)
                encoded_text = text.encode(result.encoding + "/translit")
                self.assertEqual(encoded_text, encoded_result)

                decoded_text = encoded_result.decode(
                    "{}/translit/{}".format(result.encoding, language))
                self.assertEqual(decoded_text, result.text)


if __name__ == "__main__":
    unittest.main()
