#!/usr/bin/env python

"""
Simple Indexer
=================================
Author: Jon Hurlock, October 2011

This script basically crawls a domain (not just a page) and 
then extracts all links <a href=""></a>, and finds all links
 on that domain it also is able extract different file types
 as you can see by the media type arrays. e.g. rtmp, mp4, 
wmv, jpg, png, gif

It then places its output in text files

Usage: 	>>> python crawl.py <insert web page here>
	e.g.
	>>> python crawl.py http://myviewson.tumblr.com/

Forked from:
Author:  Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
Website: https://pythonadventures.wordpress.com/2011/03/10/extract-all-links-from-a-web-page/

"""
import re
import sys
import urllib
import urlparse
from BeautifulSoup import BeautifulSoup

extracted_urls = []
elinks = []
opened = []
rtmps = []
mp4 = []
wmv = []
jpg = []
png = []
gif = []

class MyOpener(urllib.FancyURLopener):
	version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'


def process(url):
	print "Parsing",str(url)
	from urlparse import urlparse # To allow urlparse
	spliturl = urlparse(url)
	haveWeSeenThisPageBefore = False
	for pages in opened:
		if pages == str(url):
			haveWeSeenThisPageBefore = True
	# Yes I know this is retartedly long, 
	# and needs to be cleaned up.
	if str(url).endswith('.swf'):
		haveWeSeenThisPageBefore = True
	if str(url).endswith('.exe'):
		haveWeSeenThisPageBefore = True
	if str(url).endswith('.jpg'):
		jpg.append(str(url))
		haveWeSeenThisPageBefore = True
	if str(url).endswith('.JPG'):
		jpg.append(str(url))
		haveWeSeenThisPageBefore = True
	if str(url).endswith('.mp4'):
		mp4.append(str(url))
		haveWeSeenThisPageBefore = True
	if str(url).endswith('.wmv'):
		wmv.append(str(url))
		haveWeSeenThisPageBefore = True
	if str(url).endswith('.WMV'):
		wmv.append(str(url))
		haveWeSeenThisPageBefore = True
	if str(url).endswith('.wm'):
		wmv.append(str(url))
		haveWeSeenThisPageBefore = True
	if str(url).endswith('.WM'):
		wmv.append(str(url))
		haveWeSeenThisPageBefore = True
	if str(url).endswith('.png'):
		png.append(str(url))
		haveWeSeenThisPageBefore = True
	if str(url).endswith('.gif'):
		gif.append(str(url))
		haveWeSeenThisPageBefore = True
	if haveWeSeenThisPageBefore == False:
		opened.append(str(url))
		myopener = MyOpener()
		print "Opening:",url
		page = myopener.open(url)
		text = page.read()
		page.close()
		soup = BeautifulSoup(text)
		m = re.search(r"rtmp://",text)
		n = re.search(r"([a-zA-Z0-9.:-_/]*)(_external)",text)
	#	print "Extracting RTMP"
		try:
			print text[m.start():n.end()]
			rtmps.append(str(text[m.start():n.end()]))
		except Exception as re.Error:
			nothing = re.Error
			# Didnt find anything
			#print re.Error
		for tag in soup.findAll('a', href=True):
			import urlparse # To allow url.join
			tag['href'] = urlparse.urljoin(url, tag['href'])
			if tag['href'].startswith(spliturl.scheme+'://'+spliturl.netloc):
				extracted_urls.append(str(''+tag['href']+''))
			if tag['href'].startswith(spliturl.scheme+'://www.'+spliturl.netloc):
				extracted_urls.append(str(''+tag['href']+''))

def end():
	print "extracted"
	mylist = (list(set(extracted_urls)))
	for aUrl in mylist:
		x = aUrl[0:len(aUrl)]
		elinks.append(''+x+'')
	elinks.sort()
	thefile = open('thelist.txt', 'a')
	for a in elinks:
		print a
		thefile.write("%s\n" % a)
	thefile.close()

def main():
	if len(sys.argv) == 1:
		print "Jon's Link Extractor v0.1"
		print "Usage: %s URL [URL]..." % sys.argv[0]
		sys.exit(1)
	# else, if at least one parameter was passed
	for url in sys.argv[1:]:
		process(url)
	for p in extracted_urls:
		process(p)
	# Need to do this better
	##### RTMP
	rtmpfile = open('rtmps.txt', 'a')
	for r in rtmps:
		print r
		rtmpfile.write("%s\n" % r)
	rtmpfile.close()
	#### JPGS
	jpg_file = open('jpgs.txt', 'a')
	for j in jpg:
		print j
		jpg_file.write("%s\n" % j)
	jpg_file.close()
	#### WMV
	wmv_file = open('wmvs.txt', 'a')
	for w in wmv:
		print w
		wmv_file.write("%s\n" % w)
	wmv_file.close()
	#### MP4
	mp4_file = open('mp4s.txt', 'a')
	for me in wmv:
		print me
		mp4_file.write("%s\n" % me)
	mp4_file.close()
# main()

#############################################################################

if __name__ == "__main__":
	main()
	end()

