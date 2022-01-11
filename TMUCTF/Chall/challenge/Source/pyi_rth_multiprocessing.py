# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.7 (tags/v3.7.7:d7c567b08f, Mar 10 2020, 10:41:24) [MSC v.1900 64 bit (AMD64)]
# Embedded file name: PyInstaller\hooks\rthooks\pyi_rth_multiprocessing.py
import sys, os, re, multiprocessing
import multiprocessing.spawn as spawn
from subprocess import _args_from_interpreter_flags
multiprocessing.process.ORIGINAL_DIR = None

def _freeze_support():
    if len(sys.argv) >= 2:
        if sys.argv[(-2)] == '-c':
            if sys.argv[(-1)].startswith(('from multiprocessing.semaphore_tracker import main',
                                          'from multiprocessing.resource_tracker import main',
                                          'from multiprocessing.forkserver import main')):
                if set(sys.argv[1:-2]) == set(_args_from_interpreter_flags()):
                    exec(sys.argv[(-1)])
                    sys.exit()
    if spawn.is_forking(sys.argv):
        kwds = {}
        for arg in sys.argv[2:]:
            name, value = arg.split('=')
            if value == 'None':
                kwds[name] = None
            else:
                kwds[name] = int(value)

        (spawn.spawn_main)(**kwds)
        sys.exit()


multiprocessing.freeze_support = spawn.freeze_support = _freeze_support
if sys.platform.startswith('win'):
    import multiprocessing.popen_spawn_win32 as forking
else:
    import multiprocessing.popen_fork as forking
    import multiprocessing.popen_spawn_posix as spawning

class FrozenSupportMixIn:

    def __init__(self, *args, **kw):
        if hasattr(sys, 'frozen'):
            os.putenv('_MEIPASS2', sys._MEIPASS)
        try:
            (super().__init__)(*args, **kw)
        finally:
            if hasattr(sys, 'frozen'):
                if hasattr(os, 'unsetenv'):
                    os.unsetenv('_MEIPASS2')
                else:
                    os.putenv('_MEIPASS2', '')


class _Popen(FrozenSupportMixIn, forking.Popen):
    pass


forking.Popen = _Popen
if not sys.platform.startswith('win'):

    class _Spawning_Popen(FrozenSupportMixIn, spawning.Popen):
        pass


    spawning.Popen = _Spawning_Popen