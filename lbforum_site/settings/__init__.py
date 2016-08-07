SETTINGS = '.dev'
try:
    from .pre import SETTINGS
except ImportError:
    pass
exec 'from %s import *' % SETTINGS

try:
    from .local import *  # NOQA
except ImportError:
    pass
