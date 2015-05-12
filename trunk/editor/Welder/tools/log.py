import os
import time
# get some color in here
COLORS_ENABLED = False
try:
    import colorama
    COLORS_ENABLED = True
    colorama.init()
except ImportError:
    pass


class bcolors:

    def __init__(self):
        self.enable()

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''

    def enable(self):
        self.HEADER = '\033[35m'
        self.OKBLUE = '\033[34m'
        self.OKGREEN = '\033[32m'
        self.WARNING = '\033[33m'
        self.FAIL = '\033[31m'
        self.ENDC = '\033[0m'


COLORS = bcolors()
if not COLORS_ENABLED:
    COLORS.disable()

LOG_PATH = None

FAIL = 'red'
BLUE = 'blue'
GREEN = 'green'
WARN = 'yellow'
HEAD = 'purple'


def init_log_file(path):
    global LOG_PATH
    LOG_PATH = os.path.abspath(path)
    f = open(LOG_PATH, "wb")
    time_str = bytes(
        "Log Starts: " +
        time.strftime("%a, %d %b %Y %H:%M:%S") + "\n",
        'UTF-8'
    )
    f.write(time_str)
    f.close()


def log(msg, color=None, p=True):
    COLOR_MAP = {
        "red": COLORS.FAIL,
        "blue": COLORS.OKBLUE,
        "green": COLORS.OKGREEN,
        "yellow": COLORS.WARNING,
        "purple": COLORS.HEADER
    }
    if p:
        if color and color in COLOR_MAP:
            print(COLOR_MAP[color] + msg + COLORS.ENDC)
        else:
            print(msg)
    if LOG_PATH:
        f = open(LOG_PATH, "ab")
        f.write(bytes('%s\n' % msg, 'UTF-8'))
        f.close()


import distutils.log
_orig_dist_Log_log = distutils.log.Log._log


def _log_replace(self, level, msg, args):
    log_msg = msg % args
    log('%s\n' % log_msg, p=False)
    _orig_dist_Log_log(self, level, msg, args)


def replace_distutils_Log_log():
    distutils.log.Log._log = _log_replace
