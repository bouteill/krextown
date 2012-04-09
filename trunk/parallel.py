#!/usr/bin/env python
r'''
Script Python untuk membaca dua berkas paralel dan membentuk graf
sintaktikal dari terms yang ditemukan di masing-masing berkas. Graf
yang terbentuk disimpan ke dalam berkas dengan format graphml.

@author Anung Ariwibowo
@date 20120406
@versioning
20120408. path corpus with os package.
20120406. Initial experiment: Mencoba menuliskan format graphml
dari data berkas parallel.
'''

import networkx as nx
import os


#G_ID = nx.Graph()
#G_EN = nx.Graph()


class Parallel:

    def __init__(self):
        self.tandaBaca = '''!'",;)(/.#&=@+:'''
        ''' path to the corpus
        '''
        self.corpus_path = os.getcwd() + "\\plain\\"
        ''' the corpus
        '''
        self.file_ID = self.corpus_path + "PANL-BPPT-SPO-ID-100Kw.txt"
        self.file_EN = self.corpus_path + "PANL-BPPT-SPO-EN-100Kw.txt"
        self.G_ID = nx.Graph()
        self.G_EN = nx.Graph()
        self.g_file_ID = self.corpus_path + "PANL-BPPT-SPO-ID-100Kw.graphml"
        self.g_file_EN = self.corpus_path + "PANL-BPPT-SPO-EN-100Kw.graphml"


    def load_ID(self):
        f_ID = open(self.file_ID)
        for lines in f_ID:
            lines = lines.lower()
            words = lines.split()
            for idx in range(1, len(words)):
                for mark in self.tandaBaca:
                    words[idx] = words[idx].replace(mark, "")
                self.G_ID.add_edge(words[idx-1], words[idx])
        f_ID.close()


    def load_EN(self):
        f_EN = open(self.file_EN)
        for lines in f_EN:
            lines = lines.lower()
            words = lines.split()
            for idx in range(1, len(words)):
                for mark in self.tandaBaca:
                    words[idx] = words[idx].replace(mark, "")
                self.G_EN.add_edge(words[idx-1], words[idx])
        f_EN.close()


    def read(self):
        self.load_ID()
        self.load_EN()


    def write(self):
        nx.write_graphml(self.G_ID, self.g_file_ID)
        nx.write_graphml(self.G_EN, self.g_file_EN)


    def get_G_ID(self):
        return(self.G_ID)


    def get_G_EN(self):
        return(self.G_EN)


def main():
    parallel_graph = Parallel()
    parallel_graph.read()
    #parallel_graph.write()
    G_ID = parallel_graph.get_G_ID()
    G_EN = parallel_graph.get_G_EN()
    print G_ID.nodes()


if __name__ == '__main__':
    main()

