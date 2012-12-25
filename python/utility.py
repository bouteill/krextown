#!/usr/bin/env python
#
# utility.py
# Reading all files in a directory containing tempo corpus.
#
# Anung Ariwibowo
# barliant@gmail.com
# TODO:
# - Different computer Box has different folder location
# VERSIONING
# 20120624
# - init() function.


import os


def ls(arg, dirname, files):
    for eachfile in files:
        filepath = os.path.join(dirname, eachfile)
        if os.path.isfile(filepath):
            arg.append(filepath)


