"""Bindings for libiconv
"""
import sys
import os
from ctypes import (CDLL, CFUNCTYPE, POINTER,
                    create_string_buffer, create_unicode_buffer,
                    get_errno, byref, cast, sizeof, cdll,
                    c_char_p, c_int, c_size_t, c_ssize_t)
from ctypes.util import find_library


__all__ = ["iconv", "iconv_str"]

DEFAULT_TO_CODE = "ascii"
ENCODING_MAP = {
    "charmap": "ascii",
    "cp858": "cp850",
    "euc_jis_2004": "euc-jisx0213",
    "euc_jisx0213": "euc-jisx0213",
    "euc_jp": "euc-jp",
    "euc_kr": "euc-kr",
    "hp_roman8": "hp-roman8",
    "hz": "gb2312",
    "iso2022_jp": "iso-2022-jp",
    "iso2022_jp_1": "iso-2022-jp",
    "iso2022_jp_2": "iso-2022-jp-2",
    "iso2022_jp_3": "iso-2022-jp-3",
    "iso2022_jp_2004": "iso-2022-jp-3",
    "iso2022_jp_ext": "iso-2022-jp",
    "iso2022_kr": "iso-2022-kr",
    "iso8859_2": "iso8859-2",
    "iso8859_3": "iso8859-3",
    "iso8859_4": "iso8859-4",
    "iso8859_5": "iso8859-5",
    "iso8859_6": "iso8859-6",
    "iso8859_7": "iso8859-7",
    "iso8859_8": "iso8859-8",
    "iso8859_9": "iso8859-9",
    "iso8859_10": "iso8859-10",
    "iso8859_11": "iso8859-11",
    "iso8859_13": "iso8859-13",
    "iso8859_14": "iso8859-14",
    "iso8859_15": "iso8859-15",
    "iso8859_16": "iso8859-16",
    "koi8_r": "koi8-r",
    "latin-1": "latin1",
    "latin_1": "latin1",
    "mac_cyrillic": "mac-cyrillic",
    "mac_greek": "greek",
    "mac-greek": "greek",
    "mac-iceland": "mac-is",
    "mac_iceland": "mac-is",
    "mac_latin2": "mac-centraleurope",
    "mac-latin2": "mac-centraleurope",
    "mac-roman": "macintosh",
    "mac_roman": "macintosh",
    "mac_turkish": "latin5",
    "mac-turkish": "latin5",
    "mbcs": "ascii",
    "ptcp154": "pt154",
    "shift_jis_2004": "shift_jisx0213",
    "tactis": "iso8859-11",
    "tis_620": "tis-620",
    "utf_7": "utf-7",
    "utf_8": "utf-8",
    "utf_16": "utf-16",
    "utf-16-be": "utf-16be",
    "utf_16_be": "utf-16be",
    "utf-16-le": "utf-16le",
    "utf_16_le": "utf-16le",
    "utf_32": "utf-32",
    "utf-32-be": "utf-32be",
    "utf_32_be": "utf-32be",
    "utf_32_le": "utf-32le",
    "utf-32-le": "utf-32le",
}


class Error(OSError):
    def __init__(self):
        super().__init__()
        self.errno = get_errno()
        if not self.errno and os.name == "nt":
            try:
                _errno = cdll.msvcrt._errno
                _errno.restype = POINTER(c_int)
                self.errno = _errno()[0]
            except:
                pass
        self.strerror = os.strerror(self.errno)


def iconv(buf: bytes, to_code=DEFAULT_TO_CODE, to_suffix=None,
          from_code="utf-8") -> bytes:
    to_code = ENCODING_MAP.get(to_code, to_code)
    from_code = ENCODING_MAP.get(from_code, from_code)
    if to_suffix:   # "translit" or "ignore"
        to_code += "//" + to_suffix
    cd = _iconv_open(to_code.encode(), from_code.encode())
    if cd == -1:
        raise Error()
    try:
        in_len = len(buf)
        in_buf = create_string_buffer(buf, in_len)
        in_bytes_left = c_size_t(sizeof(in_buf))
        out_capacity = in_len * 4 + 4
        out_bytes_left = c_size_t(out_capacity)
        out_buf = create_string_buffer(out_bytes_left.value)
        n = _iconv(cd,
                   byref(cast(in_buf, c_char_p)), byref(in_bytes_left),
                   byref(cast(out_buf, c_char_p)), byref(out_bytes_left))
        if n == -1:
            raise Error()
    finally:
        _iconv_close(cd)
    return out_buf.raw[:out_capacity - out_bytes_left.value]


def iconv_str(text: str, to_code=DEFAULT_TO_CODE, to_suffix=None) -> bytes:
    to_code = ENCODING_MAP.get(to_code, to_code)
    if to_suffix:   # 'translit' or 'ignore'
        to_code += "//" + to_suffix
    cd = _iconv_open(to_code.encode(), b"wchar_t")
    if cd == -1:
        raise Error()
    try:
        in_len = len(text)
        in_buf = create_unicode_buffer(text, in_len)
        in_bytes_left = c_size_t(sizeof(in_buf))
        out_capacity = in_len * 4 + 4
        out_bytes_left = c_size_t(out_capacity)
        out_buf = create_string_buffer(out_bytes_left.value)
        n = _iconv(cd,
                   byref(cast(in_buf, c_char_p)), byref(in_bytes_left),
                   byref(cast(out_buf, c_char_p)), byref(out_bytes_left))
        if n == -1:
            raise Error()
    finally:
        _iconv_close(cd)
    return out_buf.raw[:out_capacity - out_bytes_left.value]


def declare_libiconv_funcs():
    global _iconv_open, _iconv, _iconv_close

    if os.name == "nt":
        base_dirs = [os.path.dirname(sys.argv[0])]
        try:
            script_path = os.path.abspath(__file__)
            base_dirs.append(os.path.dirname(script_path))
        except NameError:
            pass
        dll_names = ["libiconv2.dll", "libiconv-2.dll", "libiconv.dll"]
        lib = None
        for base_dir in base_dirs:
            for dll_name in dll_names:
                p = os.path.join(base_dir, dll_name)
                if not os.path.isfile(p):
                    p = find_library(dll_name)
                if p:
                    cwd = os.getcwd()
                    os.chdir(base_dir)
                    try:
                        lib = CDLL(p, use_errno=True)
                    finally:
                        os.chdir(cwd)
                    break
            if lib:
                break
        else:
            raise OSError("can’t find libiconv")

        libiconv_open = lib.libiconv_open
        libiconv = lib.libiconv
        libiconv_close = lib.libiconv_close
    else:
        p = find_library("c")
        if not p:
            raise OSError("can’t find libiconv")
        lib = CDLL(p, use_errno=True)
        libiconv_open = lib.iconv_open
        libiconv = lib.iconv
        libiconv_close = lib.iconv_close

    # iconv_t iconv_open (const char* tocode, const char* fromcode);
    p = CFUNCTYPE(c_ssize_t, c_char_p, c_char_p)
    _iconv_open = p(libiconv_open)

    # size_t iconv (iconv_t cd,
    #               const char **in_buf, size_t *in_bytes_left,
    #               char **out_buf, size_t *out_bytes_left);
    p = CFUNCTYPE(c_ssize_t, c_ssize_t,
                  POINTER(c_char_p), POINTER(c_size_t),
                  POINTER(c_char_p), POINTER(c_size_t))
    _iconv = p(libiconv)

    # int iconv_close (iconv_t cd);
    p = CFUNCTYPE(c_int, c_ssize_t)
    _iconv_close = p(libiconv_close)


declare_libiconv_funcs()
