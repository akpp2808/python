import locale
import re
import warnings

try:
    from functools import lru_cache
except ImportError:
    from .backports.functools import lru_cache

try:
    from . import spell
except ImportError:
    spell = None
    warnings.warn("pyenchant is unavaiable", ImportWarning)

from . import DEFAULT_ENCODING


TRANS_RE_SUBS = {
    "en": [
        (re.compile(r"(?<!\w)'([\w\s,.'’]+?)'(?!\w)", re.U), r"‘\1’"),
        (re.compile(r"(\d)'", re.U), r"\1′"),
        (re.compile(r"'"), r"’"),
        (re.compile(r'"(\w)', re.U), r"“\1"),
        (re.compile(r'^(?<!“)([^“]+\b\d+([.,]\d+)?)"', re.U), r"\1″"),
        (re.compile(r'"'), r"”"),
        (re.compile("«[ \xa0]"), "«\u202f"),
        (re.compile("[ \xa0]»"), "\u202f»"),
        (re.compile(r"--"), r"—"),
        (re.compile(r"\.{3}"), r"…"),
        (re.compile(r"^[-–—]\s", re.U | re.M), "–\xa0"),
        (re.compile(r"([^\d\w-])-([^\d\w-])", re.U), r"\1–\2"),
        (re.compile(r"(\d|\b)EUR(\d|\b)", re.U), r"\1€\2"),
        (re.compile(r"(\d|\b)GBP(\d|\b)", re.U), r"\1£\2"),
        (re.compile(r"(\d|\b)JPY(\d|\b)", re.U), r"\1¥\2"),
    ],
    "fr": [
        (re.compile(r"(?<!\w)'([\w\s,.'’]+?)'(?!\w)", re.U), r"‘\1’"),
        (re.compile(r"(\d)'", re.U), r"\1′"),
        (re.compile(r"'"), r"’"),
        (re.compile(r'"(\w)', re.U), "«\u202f\\1"),
        (re.compile(r'^(?<!«)([^«]+\b\d+([.,]\d+)?)"', re.U), r"\1″"),
        (re.compile(r'"'), "\u202f»"),
        (re.compile("«[ \xa0]"), "«\u202f"),
        (re.compile("[ \xa0]»"), "\u202f»"),
        (re.compile(r"--"), r"—"),
        (re.compile(r"\.{3}"), r"…"),
        (re.compile(r"^[-–—]\s", re.U | re.M), "–\xa0"),
        (re.compile(r"([^\d\w-])-([^\d\w-])", re.U), r"\1–\2"),
        (re.compile("(\\d)[ \xa0](\\d{3})\\b", re.U), "\\1\u202f\\2"),
        (re.compile("[ \xa0]([!?:;])"), "\u202f\\1"),
        (re.compile(r"(\d|\b)EUR(\d|\b)", re.U), r"\1€\2"),
        (re.compile(r"(\d|\b)GBP(\d|\b)", re.U), r"\1£\2"),
        (re.compile(r"(\d|\b)JPY(\d|\b)", re.U), r"\1¥\2"),
        (re.compile(r"\b(n)[o0°]\s*(\d)", re.U | re.I), "\\1º\xa0\\2"),
        (re.compile(r"oe(u|il)"), r"œ\1"),
        (re.compile(r"O(e|E)(u|U|il|IL)"), r"Œ\2"),
    ],
}
FAILSAFE_LANGUAGE = "en"


def _upgrade(text: str, language=None) -> str:
    """Try to undo a downgraded transliteration.
    """
    if language is None:
        language = locale.getdefaultlocale()[0]

    try:
        subs = TRANS_RE_SUBS[language]
    except KeyError:
        try:
            subs = TRANS_RE_SUBS[language.split("_")[0]]
        except KeyError:
            subs = TRANS_RE_SUBS[FAILSAFE_LANGUAGE]

    for pattern, repl in subs:
        text = pattern.sub(repl, text)

    return text


if spell:
    def upgrade(text: str, language=None) -> str:
        text = _upgrade(text, language)
        try:
            text = fix_spelling(text, language)
        except spell.errors.DictNotFoundError:
            warnings.warn(
                "dictionary not found for language: {!r}".format(language))
        return text

    @lru_cache(5)
    def get_dict(language=None):
        return spell.Dict(language)

    def fix_spelling(text, language=None):
        return get_dict(language).autofix(text)

else:
    upgrade = _upgrade


def decode(buf: bytes, encoding=DEFAULT_ENCODING, language=None) -> str:
    """Decode and try to undo a downgraded transliteration.
    """
    return upgrade(buf.decode(encoding, "replace"), language)
