#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from helper import run, unzip
import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
root = os.path.join(here, "../")
tools_folder = os.path.join(root, "tools/")
env = os.path.join(root, "env/")
req_folder = os.path.join(root, "requirements/")
media_folder = os.path.join(root, "lbforum_site/media/")

pip = os.path.join(env, "Scripts/pip.exe")
if os.name == 'posix':
    pip = os.path.join(env, "bin/pip")

def do_unzip():
    print '== do_unzip =='
    req_zip_folder = os.path.join(req_folder, "zip/")
    unzip(os.path.join(req_zip_folder, "registration.zip"), req_folder)

def import_new_env():
    import sys
    site_pkg = os.path.join(env, 'Lib/site-packages')
    sys.path.insert(0, site_pkg)

def copy_app_media():
    import lbforum
    src_dir = os.path.join(lbforum.__path__[0], 'media')
    obj_dir = os.path.join(media_folder, 'lbforum')
    try:
        shutil.copytree(src_dir, obj_dir)
    except:
        print "== lbforum media skiped =="

def do_pip():
    print '== do_pip =='
    requirements = os.path.join(req_folder, 'requirements.txt')
    run("%s install -r %s" % (pip, requirements))

if __name__ == '__main__':
    do_unzip()
    virtualenv_py = os.path.join(tools_folder, "virtualenv.py")
    print '== create env =='
    if not os.path.exists(env): 
        run('python %s %s' % (virtualenv_py, env))
    do_pip()
    import_new_env()
    copy_app_media()
