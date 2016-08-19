from django.utils import six

SETTINGS = '.dev'
try:
    from .pre import SETTINGS
except ImportError:
    pass
six.exec_('from %s import *' % SETTINGS)

try:
    from .local import *  # NOQA
except ImportError:
    pass
