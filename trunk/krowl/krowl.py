import urllib2
from BeautifulSoup import BeautifulSoup

def main():
    c = urllib2.urlopen('http://www.tempo.co')
    soup = BeautifulSoup(c.read())
    links = soup('a')
    for link in links:
        print link['href']


if __name__ == '__main__':
    main()

