tweakgit.py
========

Tweakgit is a small Python3 script which makes your work with git in Debian/Ubuntu linux more visible and colourful

  * Adds useful git aliases to your .gitconfig
  * Enables color prompt for your bash (modifies .bashrc)
  * Displays current git branch name in command prompt (modifies .bashrc)
  * Enables git diff color output

This script uses tips written in [LeaseWebLabs blog](http://www.leaseweblabs.com/2013/08/git-tip-beautiful-colored-and-readable-output/).

### Requirements

  * Recent Debian-based Linux (Debian/Ubuntu/Mint/etc)
  * Python3 installed (sudo apt-get install python3)
  * No external dependencies

### Installation

To run tweakgit and improve your Git experience you must run

  * Clone this repo into your home folder using: git clone 
  * Execute the tweakgit script using: python3 tweakgit.py

NB: The script will execute the following sudo command:

  * sudo apt-get install colordiff
  
### Disclaimer

This code will update the following files

  * ~/.bashrc
  * ~/.gitconfig

Before you run the script make sure you make a backup of the above files.



