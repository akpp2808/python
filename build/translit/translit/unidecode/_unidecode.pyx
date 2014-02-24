# -*- coding: utf-8 -*-
# cython: language_level=3
# cython: cdivision=True

from libc.stdlib cimport malloc, free
from cython.operator import postincrement as postinc


DEF USE_LEGACY_UNICODE_API = True

SOURCE_CODE_LANGUAGE = "Cython"

cdef enum PyUnicode_Kind:
    PyUnicode_1BYTE_KIND = 1
    PyUnicode_2BYTE_KIND = 2
    PyUnicode_4BYTE_KIND = 4

cdef extern from "Python.h":
    # Python 3.3+
    cdef int PyUnicode_READY(object o)
    cdef int PyUnicode_KIND(object o)
    cdef Py_UCS4 PyUnicode_READ(int kind, void *data, Py_ssize_t index) nogil
    cdef void *PyUnicode_DATA(object o)
    cdef Py_ssize_t PyUnicode_GET_LENGTH(object o)
    cdef object PyUnicode_FromKindAndData(int kind, void *buffer,
                                          Py_ssize_t size)

    # Deprecated
    cdef Py_UNICODE *PyUnicode_AS_UNICODE(object o)
    cdef Py_ssize_t PyUnicode_GET_SIZE(object o)
    cdef object PyUnicode_FromUnicode(Py_UNICODE *u, Py_ssize_t size)

    cdef object PyUnicode_FromStringAndSize(char *u, Py_ssize_t size)

IF USE_LEGACY_UNICODE_API:
    cdef inline int PyUnicode_READY(object o):
        return 0

    cdef inline int PyUnicode_KIND(object o):
        return sizeof(Py_UNICODE)

    cdef inline Py_UCS4 PyUnicode_READ(int kind, void *data,
                                       Py_ssize_t index) nogil:
        return (<Py_UNICODE *>data)[index]

    cdef inline void *PyUnicode_DATA(object o):
        return PyUnicode_AS_UNICODE(o)

    cdef inline Py_ssize_t PyUnicode_GET_LENGTH(object o):
        return PyUnicode_GET_SIZE(o)

    cdef inline object PyUnicode_FromKindAndData(int kind, void *buffer,
                                                 Py_ssize_t size):
        if kind == 1:
            # Can't have a real PyUnicode_1BYTE_KIND PyUnicode.
            return PyUnicode_FromStringAndSize(<char *>buffer, size)
        elif kind == sizeof(Py_UNICODE):
            return PyUnicode_FromUnicode(<Py_UNICODE *>buffer, size)
        raise ValueError("can’t emulate PyUnicode kind: {}".format(kind))

cdef extern from "table.h":
    char *TABLE[]
    size_t TABLE_SIZE
    size_t MAX_LEN


def unidecode(str text) -> str:
    """Transliterate a Unicode text into ASCII.
    """
    cdef int kind
    cdef void *buf
    cdef Py_ssize_t length
    cdef char *out_buf
    cdef Py_ssize_t out_capacity
    cdef Py_ssize_t out_length

    if PyUnicode_READY(text) < 0:
        raise MemoryError
    kind = PyUnicode_KIND(text)
    buf = PyUnicode_DATA(text)
    length = PyUnicode_GET_LENGTH(text)

    out_capacity = length * MAX_LEN
    out_buf = <char *>malloc(sizeof(char) * out_capacity)

    if out_buf == NULL:
        raise MemoryError

    try:
        with nogil:
            _unidecode(kind, buf, length, out_buf, out_capacity, &out_length)
        return PyUnicode_FromKindAndData(PyUnicode_1BYTE_KIND,
                                         out_buf, out_length)
    finally:
        free(out_buf)


cdef inline int _unidecode(int kind, void *buf, Py_ssize_t length,
                           char *out_buf, size_t out_capacity,
                           Py_ssize_t *pout_length) nogil:
    cdef Py_ssize_t i
    cdef Py_UCS4 uch
    cdef char *po, *po_max
    cdef char *pi

    po = out_buf
    po_max = po + out_capacity - 1

    for i in range(length):
        uch = PyUnicode_READ(kind, buf, i)
        if uch < 0x80:
            if po > po_max:
                break
            postinc(po)[0] = uch
            continue
        if uch >= TABLE_SIZE:
            continue
        pi = <char *>TABLE[uch]
        while pi[0] and po <= po_max:
            postinc(po)[0] = postinc(pi)[0]

    pout_length[0] = po - out_buf
    return 0 if po <= po_max else -1
