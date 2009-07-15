#!/usr/bin/python
import sys
import os
import shutil

WEAVER_DIR = os.path.dirname(os.path.abspath(__file__))

def init(args):
    target_dir = args[0]
    try:
        os.mkdir(target_dir)
    except OSError:
        print 'Cannot start project. A project with that name (%s) appears to already exist.' % target_dir
        sys.exit(1)
    else:
        shutil.copy(
            os.path.join(WEAVER_DIR, 'settings.py.tmpl'), 
            os.path.join(target_dir, 'settings.py')
        )

def build(args):
    pass
    
commands = {
    'init':init,
    'build':build
}

if __name__ == '__main__':
    cmd = sys.argv[1]
    args = sys.argv[2:]
    
    try:
        commands[cmd](args)
    except KeyError:
        print '%s is not a weaver command.' % cmd