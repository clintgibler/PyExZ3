#!/bin/bash

# Homebrew default locations (both for python and z3)
export PYTHONMODS="usr/local/lib/python2.7/site-packages:/Library/Python/2.7/site-packages:~/Library/Python/2.7/lib/python/site-packages" 
export Z3HOME="/usr/local/Cellar/z3/4.3.1/lib/python2.7/site-packages/"
export Z3BIN="/usr/local/Cellar/z3/4.3.1/bin"

PyExZ3Dir=`pwd` #/PyExZ3

# Python setup
export PYTHONPATH=$PYTHONMODS:$Z3HOME:$PyExZ3Dir

# Path setup
export PATH=$PATH:$Z3BIN:$PyExZ3Dir


