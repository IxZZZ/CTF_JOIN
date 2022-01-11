# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: PyInstaller\hooks\rthooks\pyi_rth_pkgres.py
import pkg_resources as res
from pyimod03_importers import FrozenImporter
res.register_loader_type(FrozenImporter, res.NullProvider)