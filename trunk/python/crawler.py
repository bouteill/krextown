#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-

# For processing HTML
from BeautifulSoup import BeautifulSoup

#for file-like opening and reading urls 
import urllib2

#for operating system functions like creating directories
import os

#to handle encodings (the way characters are stored/represented)
import codecs
#regular expressions
import re
#provides standard error message values
import errno
#library providing functions on strings
import string


#url of the website listing the speech documents
BASE_URL = "http://2008election.procon.org/"
WEBSITE = BASE_URL + "view.resource.php?resourceID=001568"
DATA_DIR = "downloads"
WEBSITE_FILE = DATA_DIR + os.sep + "procon.html"

def mkdir_p(path):
    try:
        os.makedirs(path)
    #if something went wrong
    except OSError as exc:
        #if the directory already exists we don't have to create it
        if exc.errno == errno.EEXIST:
            pass
        #something else went wrong, so raise the error to show it to the user
        else: raise


def download_file(url, filename):
    """
    Takes an url to download into the given filename.
    """
    #file already downloaded?
    if not os.path.exists(filename):
        #os.path.dirname("/path/to/file") => "/path/to/"
        directory_name = os.path.dirname(filename)
        #if directory_name is empty ("") skip the creation
        if directory_name:
            mkdir_p(directory_name)

        opened_url = urllib2.urlopen(url) #like open(file) we can open a url
        with open(filename, "w") as outputfile:
            outputfile.write(opened_url.read())


def parse_file(filename):
    """
    Takes html file and returns a BeautifulSoup object with the parsed content
    """
    #open file
    with codecs.open(filename,"r","utf-8") as htmlfile:
        html_content = " ".join(htmlfile.readlines())
        #parse the file to create a BeautifulSoup object
        soup = BeautifulSoup(html_content, fromEncoding="utf-8")
    return soup


def clean_filename(ugly_filename):
    """
    Removes or replaces all ugly characters to return a nice filename.
    """
    #define allowed chars
    valid_chars = "-_.(){0}{1}".format(string.ascii_letters, string.digits)
    #replace spaces with underscores
    cleaner_filename = ugly_filename.replace(" ","_")
    #only take character in account that are valid. the rest is thrown away
    clean_fname = ''.join(c for c in cleaner_filename if c in valid_chars)
    #s=(x for x in y if z) is an iteration over y with character x. Only those
    #characters that match condition z are added to the resulting list s.
    #''.join creates a string from of the list

    return clean_fname


if __name__ == "__main__":
    #Did we already download the search page?
    if not os.path.exists(WEBSITE_FILE):
        download_file(WEBSITE, WEBSITE_FILE)

    soup = parse_file(WEBSITE_FILE)

    #find all tags <a href=..> where the regular expression (anything
    #ending in .pdf) matches the value of the href attribute
    pdfsoup = soup.findAll("a",href=re.compile(r'.*\.pdf'))

    #To learn about the r before the regular expressions read
    #https://pythonconquerstheuniverse.wordpress.com/2008/06/04/gotcha-—-backslashes-are-escape-characters/

    #match an uppercase letter at the beginning of a string followed by an
    #arbitray number > 0 of lowercase letters
    dir_regex = re.compile(r"^[A-Z][a-z]+")
    #match any sequence of digits in a string
    date_regex = re.compile(r"\d+")

    #iterate over the pdf links to download them
    for pdfs in pdfsoup:
        try:
            #relative url looks like "sourcefiles/Obama20081104.pdf"
            rel_url = pdfs["href"]
            pdfurl = BASE_URL + rel_url #complete url with the base
            title = clean_filename(pdfs.getText()) #name of the actual file

            #split rel_url at "/" => ["sourcefile", "Obama20081104.pdf"] take
            #last element with [-1] => Obama20081104.pdf
            filename_on_server = rel_url.split("/")[-1]

            #create complete local directory name with help of the dir_regex
            dir_name = dir_regex.search(filename_on_server).group()
            dir_name = DATA_DIR + os.sep + dir_name

            #extract speech date
            speech_date = date_regex.search(filename_on_server).group()

            #put together the complete path and filename
            filename = dir_name + os.sep + speech_date + "-" + title + ".pdf"

            #download the file and store it in our nicely formatted filename
            download_file(pdfurl, filename)
            print("downloaded {0}".format(filename))
        except Exception, e:
            #if something went wrong print the error and continue with the next
            #link. The program is not aborted on an error here!
            print(e)
            continue
