from __future__ import print_function

import builtins
import codecs
import os
import re
import sys
import warnings

from . import DEFAULT_ENCODING
from .unidecode import unidecode


ICONV_OS_BLACKLIST = [
    "nt",
]

if os.name in ICONV_OS_BLACKLIST:
    iconv = iconv_str = None
else:
    try:
        from .iconv import iconv, iconv_str, Error as IConvError
    except (ImportError, OSError) as e:
        iconv = iconv_str = None
        warnings.warn("iconv is unavaiable: {}".format(e), ImportWarning)


RE_SUBS = {
    ("«»", re.compile(r"«\s?|\s?»", re.U), r'"'),
    ("Æ", re.compile(r"Æ([a-zß-öø-ÿœ])"), r"Ae\1"),
    ("Þ", re.compile(r"Þ([a-zß-öø-ÿœ])"), r"Th\1"),
    ("Œ", re.compile(r"Œ([a-zß-öø-ÿœ])"), r"Oe\1"),
}

UNICODE_SUBS = {
    "\u202f": "\xa0",
    "℃": "°C",
    "℉": "°F",
    "№": "Nº",
}

needs_substitution_cache = {}
downgrade_cache = {}


def downgrade(text: str, encoding=DEFAULT_ENCODING) -> str:
    """Downgrade text to fit into the specified encoding.
    """
    encoding = codecs.lookup(encoding).name
    for chars, pattern, repl in RE_SUBS:
        try:
            needs_substitution = needs_substitution_cache[chars[0], encoding]
        except KeyError:
            try:
                chars[0].encode(encoding)
            except UnicodeEncodeError:
                needs_substitution = True
            else:
                needs_substitution = False
            needs_substitution_cache[chars[0], encoding] = needs_substitution
        if needs_substitution and any(c in text for c in chars):
            text = pattern.sub(repl, text)
    return _downgrade(text, encoding)


if iconv_str:
    def _downgrade(text, encoding):
        result = []
        for c in text:
            try:
                repl = downgrade_cache[c, encoding]
            except KeyError:
                try:
                    c.encode(encoding)
                except UnicodeEncodeError:
                    # Try iconv before using unidecode.
                    try:
                        # TODO: Investigate why iconv from Python 2
                        # behaves differently from Python 3 with \u202f.
                        nc = UNICODE_SUBS.get(c, c)
                        b = iconv_str(nc, encoding, "translit")
                    except IConvError:
                        repl = unidecode(c)
                    else:
                        repl = (unidecode(c) if b"?" in b else
                                b.decode(encoding))
                else:
                    repl = c
                downgrade_cache[c, encoding] = repl
            result.append(repl)
        return "".join(result)
else:
    def _downgrade(text, encoding):
        result = []
        for c in text:
            try:
                repl = downgrade_cache[c, encoding]
            except KeyError:
                try:
                    c.encode(encoding)
                except UnicodeEncodeError:
                    if c in UNICODE_SUBS:
                        nc = UNICODE_SUBS[c]
                        try:
                            nc.encode(encoding)
                        except UnicodeEncodeError:
                            # Use only unidecode.
                            repl = unidecode(c)
                        else:
                            repl = nc
                    else:
                        repl = unidecode(c)
                else:
                    repl = c
                downgrade_cache[c, encoding] = repl
            result.append(repl)
        return "".join(result)


def encode(text: str, encoding=DEFAULT_ENCODING) -> bytes:
    """Encode text into a transliterated form.
    """
    return downgrade(text, encoding).encode(encoding)


def print(*args, sep=" ", end="\n", file=sys.stdout): #@ReservedAssignment
    """A print function that performs transliteration.
    """
    if file is not None:
        encoding = file.encoding
        if not encoding.startswith("utf"):
            args = (downgrade(str(arg), encoding) for arg in args)
    builtins.print(*args, sep=sep, end=end, file=file)
