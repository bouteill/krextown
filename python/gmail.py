#!/usr/bin/env python
#
# gmail.py
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


import imaplib
import getpass
import email


def main():
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(getpass.getuser(), getpass.getpass())
    mail.select('0-bahtera')
    result, data = mail.search(None, 'ALL')
    ids = data[0]
    id_list = ids.split()

    message = email.message_from_string(raw_email)


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

