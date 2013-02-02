
import os
import nltk.data

from nltk.corpus import PlaintextCorpusReader


def main():
  print nltk.data.path

  corpus_dir = '../corpus-local/tempo-txt'
  corpus_root = os.getcwd() + '/' + corpus_dir
  wordlists = PlaintextCorpusReader(corpus_root, '.*\.txt')

  len(wordlists.fileids())

  f1 = wordlists.fileids()[0]
  f2 = wordlists.fileids()[1]
  f3 = wordlists.fileids()[2]

  wordlists.raw(fileids=[f1,f2,f3])

  for sent in wordlists.sents(fileids=[f1]):
    for word in sent:
      print word,
    print


if __name__ == '__main__':
  main()

