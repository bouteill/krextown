import urllib2

auth_handler = urllib2.ProxyBasicAuthHandler(urllib2.HTTPPasswordMgrWithDefaultRealm())
#auth_handler.add_password(realm=None, uri='http://proxy.example.com:3128/', user='USERNAME', passwd='PASSWORD')
auth_handler.add_password(realm=None,
    uri='http://192.168.11.179:3128/', user='anung',
    passwd='1kosong58')
opener = urllib2.build_opener(auth_handler)
urllib2.install_opener(opener)

import nltk
nltk.download()

