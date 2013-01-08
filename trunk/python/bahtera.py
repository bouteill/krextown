from datetime import datetime, timedelta
import email
from imapclient import IMAPClient

HOST = 'imap.gmail.com'
USERNAME = 'username'
PASSWORD = 'password'
ssl = True

today = datetime.today()
cutoff = today - timedelta(days=5)

## Connect, login and select the INBOX
server = IMAPClient(HOST, use_uid=True, ssl=ssl)
server.login(USERNAME, PASSWORD)
select_info = server.select_folder('INBOX')

## Search for relevant messages
## see http://tools.ietf.org/html/rfc3501#section-6.4.5
messages = server.search(
    ['FROM "Alerts@foobank.com"', 'SINCE %s' % cutoff.strftime('%d-%b-%Y')])
response = server.fetch(messages, ['RFC822'])

for msgid, data in response.iteritems():
    msg_string = data['RFC822']
    msg = email.message_from_string(msg_string)
    print 'ID %d: From: %s Date: %s' % (msgid, msg['From'], msg['date'])


import imaplib
import email

def extract_body(payload):
    if isinstance(payload,str):
        return payload
    else:
        return '\n'.join([extract_body(part.get_payload()) for part in payload])

conn = imaplib.IMAP4_SSL("imap.gmail.com", 993)
conn.login("user", "password")
conn.select()
typ, data = conn.search(None, 'UNSEEN')
try:
    for num in data[0].split():
        typ, msg_data = conn.fetch(num, '(RFC822)')
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_string(response_part[1])
                subject=msg['subject']                   
                print(subject)
                payload=msg.get_payload()
                body=extract_body(payload)
                print(body)
        typ, response = conn.store(num, '+FLAGS', r'(\Seen)')
finally:
    try:
        conn.close()
    except:
        pass
    conn.logout()

