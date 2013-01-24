#!/usr/bin/env python
#
# bacatempo.py
# Reading all files in a directory containing tempo corpus.
#
# Anung Ariwibowo
# barliant@gmail.com
# startup folder for netbook
# TODO:
# - Different computer Box has different folder location
# VERSIONING
# 20120624
# - init() function.


import os
import utility
import nltk
import networkx as nx


def main():
    init('netbook')

    filelist = []
    root = '../corpus-local/tempo-txt'
    os.path.walk(root, utility.ls, filelist)
    print root, 'has', len(filelist), 'files.'
    print filelist[0]
    print filelist[-1]
    create_graph(filelist)


def create_graph(filelist):
def init(workplace):
    '''
    Change working directory, depends on workplace
    '''
    workplace = workplace.lower().strip()
    if workplace == 'netbook-kantor':
        os.chdir('C:\\Users\\user\\Documents\\/02254\\krextown\\python')
    elif workplace == 'netbook':
        os.chdir('C:\\Users\\user\\Documents\\/02254\\krextown\\python')
    else:
        print "krextown init: Unknown workplace."


if __name__ == '__main__':
    main()

