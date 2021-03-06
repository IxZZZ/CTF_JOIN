# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: PyInstaller\loader\pyiboot01_bootstrap.py
import sys, pyimod03_importers
pyimod03_importers.install()
import os
if not hasattr(sys, 'frozen'):
    sys.frozen = True
sys.prefix = sys._MEIPASS
sys.exec_prefix = sys.prefix
sys.base_prefix = sys.prefix
sys.base_exec_prefix = sys.exec_prefix
VIRTENV = 'VIRTUAL_ENV'
if VIRTENV in os.environ:
    os.environ[VIRTENV] = ''
    del os.environ[VIRTENV]
python_path = []
for pth in sys.path:
    python_path.append(os.path.abspath(pth))
    sys.path = python_path

class NullWriter:
    softspace = 0
    encoding = 'UTF-8'

    def write(*args):
        pass

    def flush(*args):
        pass

    def isatty(self):
        return False


if sys.stdout is None:
    sys.stdout = NullWriter()
if sys.stderr is None:
    sys.stderr = NullWriter()
try:
    import encodings
except ImportError:
    pass

if sys.warnoptions:
    import warnings
try:
    import ctypes, os
    from ctypes import LibraryLoader, DEFAULT_MODE

    def _frozen_name(name):
        if name:
            frozen_name = os.path.join(sys._MEIPASS, os.path.basename(name))
            if os.path.exists(frozen_name):
                if not os.path.isdir(frozen_name):
                    name = frozen_name
        return name


    class PyInstallerImportError(OSError):

        def __init__(self, name):
            self.msg = 'Failed to load dynlib/dll %r. Most probably this dynlib/dll was not found when the application was frozen.' % name
            self.args = (self.msg,)


    class PyInstallerCDLL(ctypes.CDLL):

        def __init__(self, name, *args, **kwargs):
            name = _frozen_name(name)
            try:
                (super(PyInstallerCDLL, self).__init__)(name, *args, **kwargs)
            except Exception as base_error:
                try:
                    raise PyInstallerImportError(name) from base_error
                finally:
                    base_error = None
                    del base_error


    ctypes.CDLL = PyInstallerCDLL
    ctypes.cdll = LibraryLoader(PyInstallerCDLL)

    class PyInstallerPyDLL(ctypes.PyDLL):

        def __init__(self, name, *args, **kwargs):
            name = _frozen_name(name)
            try:
                (super(PyInstallerPyDLL, self).__init__)(name, *args, **kwargs)
            except Exception as base_error:
                try:
                    raise PyInstallerImportError(name) from base_error
                finally:
                    base_error = None
                    del base_error


    ctypes.PyDLL = PyInstallerPyDLL
    ctypes.pydll = LibraryLoader(PyInstallerPyDLL)
    if sys.platform.startswith('win'):

        class PyInstallerWinDLL(ctypes.WinDLL):

            def __init__(self, name, *args, **kwargs):
                name = _frozen_name(name)
                try:
                    (super(PyInstallerWinDLL, self).__init__)(name, *args, **kwargs)
                except Exception as base_error:
                    try:
                        raise PyInstallerImportError(name) from base_error
                    finally:
                        base_error = None
                        del base_error


        ctypes.WinDLL = PyInstallerWinDLL
        ctypes.windll = LibraryLoader(PyInstallerWinDLL)

        class PyInstallerOleDLL(ctypes.OleDLL):

            def __init__(self, name, *args, **kwargs):
                name = _frozen_name(name)
                try:
                    (super(PyInstallerOleDLL, self).__init__)(name, *args, **kwargs)
                except Exception as base_error:
                    try:
                        raise PyInstallerImportError(name) from base_error
                    finally:
                        base_error = None
                        del base_error


        ctypes.OleDLL = PyInstallerOleDLL
        ctypes.oledll = LibraryLoader(PyInstallerOleDLL)
except ImportError:
    pass

if sys.platform.startswith('darwin'):
    try:
        from ctypes.macholib import dyld
        dyld.DEFAULT_LIBRARY_FALLBACK.insert(0, sys._MEIPASS)
    except ImportError:
        pass

d = 'eggs'
d = os.path.join(sys._MEIPASS, d)
if os.path.isdir(d):
    for fn in os.listdir(d):
        sys.path.append(os.path.join(d, fn))