#!/usr/bin/python3 -tt
# Script is designed to work on Debian/Ubuntu Linux platform
# Requirements: Python 3+
__author__ = 'Ilia Shakitko'

import re
import os
import subprocess
import configparser

# get user home directory
home_dir = os.path.expanduser('~')
# path to distfiles
bashrc_dist_filename = 'bashrc.dist'
gitconfig_dist_filename = 'gitconfig.dist'
# We will identify if our addon exists by this comment
git_prompt_regexp = r'# Add git branch if its present to PS1'
# flag for content change
content_changed = False


def show_branch_in_shell(bashrc_content):
    global content_changed

    # modify bashrc_conent only if regexp is not match
    if not re.search(git_prompt_regexp, bashrc_content):
        bashrc_dist_handler = open(bashrc_dist_filename, 'r')
        dist_content = bashrc_dist_handler.read()
        bashrc_dist_handler.close()
        bashrc_content = bashrc_content + '\n' + dist_content
        content_changed = True

    return bashrc_content

def color_prompt_enable(bashrc_content):
    # Searches for commented out "force_color_prompt" and enables it
    return re.sub(r'#\s*force_color_prompt\s*=\s*yes', r'force_color_prompt=yes', bashrc_content)

def install_colordiff():
    # check if colordiff is installed
    out = subprocess.check_output(['apt-cache', 'policy', 'colordiff'])

    if re.search(r'Installed:\s*\(none\)', str(out)):
        # install with "sudo" if not exists
        subprocess.call(['sudo', 'apt-get', 'install', 'colordiff'])
        print('colordiff has been installed')

def add_git_aliases():
    # make absolute path for new .gitconfig in user home directory
    home_gitconfig_path = os.path.join(home_dir, '.gitconfig')
    if not os.path.exists(home_gitconfig_path):
        # create .gitconfig file if it doesn't exists
        subprocess.call(['cp', gitconfig_dist_filename, home_gitconfig_path])
        print('.gitconfig file has been created')
        return

    # optional (if exists, merge 2 configs and write the result)
    config = configparser.ConfigParser()
    config.read(home_gitconfig_path)
    config.read(gitconfig_dist_filename)

    # set up config file name
    config.filename = '.gitconfig'

    # write merged config to disk
    file_handler = open(home_gitconfig_path, 'w')
    config.write(file_handler)
    file_handler.close()

    print('.gitconfig file has been updated\n')


def main():
    path_bash = os.path.join(home_dir, '.bashrc')
    if not os.path.isfile(path_bash):
        print('bashrc is not found')
        exit(1)

    # read local .bashrc file
    file_handler = open(path_bash, 'rU')
    bashrc_content = file_handler.read()
    file_handler.close()

    # execute changes
    bashrc_content = show_branch_in_shell(
        color_prompt_enable(bashrc_content)
    )
    install_colordiff()
    add_git_aliases()


    if content_changed is True:
        # save changed bashrc
        file_handler = open(path_bash, 'w')
        file_handler.write(bashrc_content)
        file_handler.close()

if __name__ == '__main__':
    main()
