import codecs

from .downgrade import downgrade
from .upgrade import upgrade


def encode_factory(encoding):
    def func(input, errors="strict"): #@ReservedAssignment
        return downgrade(input, encoding).encode(encoding, errors), len(input)
    return func


def decode_factory(encoding, language=None):
    def func(input, errors="strict"): #@ReservedAssignment
        buf = bytes(input)
        return upgrade(buf.decode(encoding, errors), language), len(buf)
    return func


def search_function(encoding):
    parts = encoding.split("/")
    if len(parts) > 1 and parts[1] == "translit":
        e = parts[0]
        encode_func = encode_factory(e)
        decode_func = decode_factory(e, parts[2] if len(parts) > 2 else None)
        return codecs.CodecInfo(encode_func, decode_func)


codecs.register(search_function)
