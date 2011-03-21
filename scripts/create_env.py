#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from helper import run, unzip
import os

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = STATIC_FOLDER = os.path.join(HERE, "../")
TOOLS_FOLDER = os.path.join(ROOT, "tools/")
ENV = os.path.join(ROOT, "env/")
REQ_FOLDER = os.path.join(ROOT, "requirements/")
STATIC_FOLDER = os.path.join(ROOT, "sites/default/static/")

def do_unzip():
    print '== do_unzip =='
    tools_zip_folder = os.path.join(TOOLS_FOLDER, "zip/")
    req_zip_folder = os.path.join(REQ_FOLDER, "zip/")
    unzip(os.path.join(req_zip_folder, "registration.zip"), REQ_FOLDER)
    static_scripts_folder = os.path.join(STATIC_FOLDER, 'scripts')

def do_pip():
    pip = os.path.join(ENV, "Scripts/pip.exe")
    if os.name == 'posix':
        pip = os.path.join(ENV, "bin/pip")
    print '== do_pip =='
    pip = "%s install " % pip
    run('%s %s' % (pip, 'Django==1.2.3'))
    run('%s %s' % (pip, 'django-helper'))
    run('%s %s' % (pip, 'django-lb-attachments'))
    run('%s %s' % (pip, 'django-onlineuser'))
    run('%s %s' % (pip, 'django-simple-avatar'))
    run('%s %s' % (pip, 'BeautifulSoup'))
    run('%s %s' % (pip, 'postmarkup'))
    run('%s %s' % (pip, 'PIL'))
    run('%s %s' % (pip, 'django-pagination'))
    run('%s %s' % (pip, 'South'))

if __name__ == '__main__':
    do_unzip()
    virtualenv_py = os.path.join(TOOLS_FOLDER, "virtualenv.py")
    print '== create ENV =='
    run('python %s %s' % (virtualenv_py, ENV))
    do_pip()
