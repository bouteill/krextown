#!/usr/bin/env python
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
import nltk


def main():
    pass


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


def test_read():
    text = read('000106-111.txt')
    print type(text)
    return text


def read(aFile):
    '''
    Given a text file aFile, open it, and returns an nltk.text.Text object from it.
    '''
    try:
        f = open(aFile, 'r')
        data = f.read()
        data.replace('\n', ' ')
        tokens = nltk.word_tokenize(data.strip())
        text = nltk.Text(tokens)
    except IOError:
        print "Something wrong with",aFile,"."
    finally:
        f.close()

    return text


if __name__ == '__main__':
    main()

