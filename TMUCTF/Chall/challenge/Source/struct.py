# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: struct.py
# Compiled at: 1995-09-27 23:18:56
# Size of source mod 2**32: 272 bytes
__all__ = [
 'calcsize', 'pack', 'pack_into', 'unpack', 'unpack_from',
 'iter_unpack',
 'Struct',
 'error']
from _struct import *
from _struct import _clearcache
from _struct import __doc__