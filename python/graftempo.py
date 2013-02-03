
import os
import nltk.data
import networkx as nx

from nltk.corpus import PlaintextCorpusReader
from nltk import tokenize


def main():
  tempo_dir = '../corpus-local/tempo-txt'
  file_regex = '.*\.txt'

  G = build_graph(tempo_dir, file_regex)
  print tempo_dir
  print "\tAda " + str(len(G.nodes())) + " node."
  print "\tAda " + str(len(G.edges())) + " edge."
  print "\tClustering coefficient      : " + str(nx.clustering(G))
  print "\tAverage shortest path length: " + str(nx.clustering(G))

  kompas_dir = '../corpus-local/kompas-txt'
  G = build_graph(kompas_dir, file_regex)
  print kompas_dir
  print "\tAda " + str(len(G.nodes())) + " node."
  print "\tAda " + str(len(G.edges())) + " edge."
  print "\tClustering coefficient      : " + str(nx.clustering(G))
  print "\tAverage shortest path length: " + str(nx.clustering(G))



def build_graph(folder, file_pattern):
  corpus_root = os.getcwd() + '/' + folder
  print "Membuka korpus " + folder + " ..."
  word_lists = PlaintextCorpusReader(corpus_root, file_pattern)

  naskah = word_lists.sents()
  filelists = tempo_word_lists.fileids()
  teks = tokenize.sent_tokenize(tempo_word_lists.raw(fileids=filelists))

  print folder + " memiliki " + str(len(teks)) + ", " + str(len(naskah)) + " kalimat."

  G_result = nx.Graph()
  print "Membangun graf " + folder + " ..."
  for kalimat in naskah:
    kata = kalimat[0]
    prevToken = kata.lower()
    for idx in range(1, len(kalimat)):
      kata = kalimat[idx]
      token = kata.lower()
      if containsLetter(token) and containsLetter(prevToken):
        G_result.add_edge(prevToken, token)
        prevToken = token

  return G_result


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
  
