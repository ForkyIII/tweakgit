#!/usr/bin/python -tt
__author__ = 'Ilia Shakitko'

import re
import os

path_bash = 'FULL_PATH_TO_YOUR_.bashrc'

def colorify_git():
  if not os.path.isfile(path_bash):
    print 'bashrc is not found'
    exit(1)

  f = open(path_bash, 'rU')
  bashrc_content = f.read()
  f.close()

  bashrc = open(path_bash, 'w')
  bashrc.write(re.sub(r'#force_color_prompt\s*=\s*yes', r'force_color_prompt=yes', bashrc_content))

  bashrc.close()

def main():
  colorify_git()

if __name__ == '__main__':
  main()
