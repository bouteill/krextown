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


from datetime import datetime, timedelta
import imaplib
import getpass
import email


def main():
    today = datetime.today()
    cutoff = today - timedelta(days=7)

    HOST = 'imap.gmail.com'
    USERNAME = 'barliant@gmail.com'
    folderName = '0-bahtera'

    print "Connecting to", HOST, "..."
    mail = imaplib.IMAP4_SSL(HOST)
    mail.login(USERNAME, getpass.getpass())
    print "Selecting folder", folderName, "..."
    mail.select(folderName)
    result, data = mail.search(None, 'ALL')
    ids = data[0]
    id_list = ids.split()
    latest_email_id = id_list[-1]

    result, data = mail.fetch(latest_email_id, '(RFC82)')
    raw_email = data[0][1]

    message = email.message_from_string(raw_email)

    print "Logging off..."
    mail.logout()


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

