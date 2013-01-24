
import nltk.data

print nltk.data.path

from nltk.corpus import PlaintextCorpusReader

corpus_root = 'C:/Users/user/Documents/02254/krextown/corpus-local/tempo-txt'
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

