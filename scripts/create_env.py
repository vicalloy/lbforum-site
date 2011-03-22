#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from helper import run, unzip
import os
import shutil

import sys
sys.path.insert(0, 'E:/labs/lbforum_site_git')


HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "../")
TOOLS_FOLDER = os.path.join(ROOT, "tools/")
ENV = os.path.join(ROOT, "env/")
REQ_FOLDER = os.path.join(ROOT, "requirements/")
MEDIA_FOLDER = os.path.join(ROOT, "lbforum_site/media/")

def do_unzip():
    print '== do_unzip =='
    req_zip_folder = os.path.join(REQ_FOLDER, "zip/")
    unzip(os.path.join(req_zip_folder, "registration.zip"), REQ_FOLDER)

def copy_app_media():
    import lbforum
    src_dir = os.path.join(lbforum.__path__[0], 'media')
    obj_dir = os.path.join(MEDIA_FOLDER, 'lbforum')
    try:
        shutil.copytree(src_dir, obj_dir)
    except:
        print "== lbforum media skiped =="

def do_pip():
    pip = os.path.join(ENV, "Scripts/pip.exe")
    if os.name == 'posix':
        pip = os.path.join(ENV, "bin/pip")
    print '== do_pip =='
    pip = "%s install " % pip
    run('%s %s' % (pip, 'Django==1.2.3'))

    run('%s %s' % (pip, 'django-helper==0.8.1'))
    run('%s %s' % (pip, 'django-lb-attachments==0.8'))
    run('%s %s' % (pip, 'django-onlineuser==0.8'))
    run('%s %s' % (pip, 'django-simple-avatar==0.8.1'))
    run('%s %s' % (pip, 'lbforum'))

    run('%s %s' % (pip, 'BeautifulSoup'))
    run('%s %s' % (pip, 'postmarkup'))
    run('%s %s' % (pip, 'PIL'))
    run('%s %s' % (pip, 'django-pagination'))
    run('%s %s' % (pip, 'South'))

if __name__ == '__main__':
    do_unzip()
    virtualenv_py = os.path.join(TOOLS_FOLDER, "virtualenv.py")
    print '== create ENV =='
    if not os.path.exists(ENV): 
        run('python %s %s' % (virtualenv_py, ENV))
    do_pip()
    copy_app_media()
