'''
Membaca isi berkas dari korpus Tempo di folder yang diberikan.
Anung Ariwibowo
Versioning
20120118 Membaca korpus Tempo, memasukkannya ke nltk.Text.
20120116 v1.0
'''

import networkx as nx
import os
import nltk
import pprint

def grab_files(directory):
    for name in os.listdir(directory):
        full_path = os.path.join(directory, name)
        if os.path.isdir(full_path):
            for entry in grab_files(full_path):
                yield entry
        elif os.path.isfile(full_path):
            yield full_path
        else:
            print('Unidentified name %s. It could be a symbolic link' % full_path)

def main():
    G = nx.Graph()

    folderKorpus = os.path.abspath('.') + '\\tempo-txt'
    #folderKorpus = 'tempo-txt'
    '''
    for root, files, dirs in os.walk(folderKorpus):
        for name in files:
            print(os.path.join(root, name))
    '''

    ctrBerkas = 0
    sentTokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    daftarBerkas = grab_files(folderKorpus)
    for berkas in daftarBerkas:
        data = open(berkas)
        for baris in data:
            sents = sentTokenizer.tokenize(baris)
            for sent in sents:
                kalimat = sent.replace('\n', ' ').strip()
                tokens = nltk.word_tokenize(kalimat)
                text = nltk.Text(tokens)
        data.close()
        ctrBerkas += 1
    pprint.pprint(text)
    print("%d berkas diolah" % ctrBerkas)


if __name__ == '__main__':
    main()
else:
    print "Modul Analisis Graf Bahasa."
    print __doc__
