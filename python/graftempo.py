
import os
import nltk.data
import networkx as nx

from nltk.corpus import PlaintextCorpusReader
from nltk import tokenize


def main():
  #print nltk.data.path

  sent_tknzr = nltk.data.load('tokenizers/punkt/english.pickle')
  corpus_dir = '../corpus-local/tempo-txt'
  corpus_root = os.getcwd() + '/' + corpus_dir
  wordlists = PlaintextCorpusReader(corpus_root, '.*\.txt')

  len(wordlists.fileids())

  '''
  f1 = wordlists.fileids()[0]
  f2 = wordlists.fileids()[1]
  f3 = wordlists.fileids()[2]

  print wordlists.raw(fileids=[f1,f2,f3])
  '''

  filelists = wordlists.fileids()
  teks = tokenize.sent_tokenize(wordlists.raw(fileids=filelists))
  ctrKalimat = 0
  '''
  for kalimat in teks:
    #print kalimat
    ctrKalimat = ctrKalimat + 1
  print "\tAda " + str(ctrKalimat) + " kalimat."
  '''
  print "\tAda " + str(len(teks)) + " kalimat."

  G = nx.Graph()
  print "Membangun graf ..."
  for kalimat in teks:
    kata = kalimat[0]
    prevToken = kata.lower()
    for idx in range(1, len(kalimat)):
      kata = kalimat[idx]
      token = kata.lower()
      if containsLetter(token) and containsLetter(prevToken):
        G.add_edge(prevToken, token)
        prevToken = token
  print "Ada " + len(G.nodes()) + " node."
  print "Ada " + len(G.edges()) + " edge."

  '''
  for sent in wordlists.sents(fileids=filelists[0]):
    print type(sent)
    for word in sent:
      print word,
    print
  '''


def containsLetter(token):
  flag = False
  letter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
      'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
      'y', 'z']
  for symbol in token:
    if symbol in letter:
      flag = True
  return flag


if __name__ == '__main__':
  main()
  
