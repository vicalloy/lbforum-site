import os
HERE = os.path.dirname(os.path.abspath(__file__))

from settings import *

LBF_STICKY_TOPIC_POST = True
LBF_LAST_TOPIC_NO_INDEX = True

import lbforum
V2EX_TEMPLATE_DIR = os.path.join(lbforum.__path__[0], 'templates_v2ex')

TEMPLATE_DIRS = (
        os.path.join(HERE, 'templates_plus'),
        os.path.join(HERE, 'templates_v2ex'),
        V2EX_TEMPLATE_DIR,
)

try:
    from local_settings import *
    CTX_CONFIG.update(CTX_CONFIG_)
except ImportError, e:
    pass
try:
    from v2ex_local_settings import *
    CTX_CONFIG.update(CTX_CONFIG_)
except ImportError, e:
    pass
