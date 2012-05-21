#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      user
#
# Created:     17/05/2012
# Copyright:   (c) user 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import nltk
from nltk.book import *
import nltk.book as buku
from nltk.corpus import wordnet as wn


'''
text1: Moby Dick
text2: Sense and Sensibility
text3: The Book of Genesis
text4: Inaugural Address Corpus
text5: Chat Corpus
text6: Monty Python and the Holy Grail
text7: Wall Street Journal
text8: Personals Corpus
text9: The Man Who Was Thursday
'''

def main():
    text1.concordance("monstrous")
    text1.similar("monstrous")
    text1.common_contexts(['monstrous', 'subtly'])
    len(text1)
    len(set(text1))
    sorted(set(text1))

    df = FreqDist(text5)
    vocabulary = df.keys()
    vocabulary[:10]
    df.plot(50)
    df.plot(50, cumulative=True)

    kalimat = ['After', 'all', 'is', 'said', 'and', 'done', 'more', 'is', 'said', 'than', 'done']
    tokens = set(kalimat)
    tokens = sorted(tokens)
    tokens[-2:]
    bigrams(kalimat)

    H = df.hapaxes()
    longHapaxes = [w for w in V if len(w) > 15]

    #from nltk.book import *
    fdist1 = FreqDist(text1)
    vocabulary = fdist.keys()
    vocabulary[:50]
    vocabulary['whale']


def lexicalDiversity(text):
    return len(text) / len(set(text))

def percentage(count, total):
    return 100 * count / total

def latihan_wordnet():
    wn.synsets('motorcar')
    wn.synset('car.n.01').lemma_names
    wn.synset('car.n.01').lemmas
    wn.synset('car.n.01').definition
    wn.synset('car.n.01').examples
    wn.synset('car.n.01').definition
    #'a motor vehicle with four wheels; usually propelled by an internal combustion engine'
    wn.synset('car.n.01').examples
    #['he needs a car to get to work']
    #atau
    wn.lemmas('car')
    #[Lemma('car.n.01.car'), Lemma('car.n.02.car'), Lemma('car.n.03.car'),
    #Lemma('car.n.04.car'), Lemma('cable_car.n.01.car')]
    wn.synsets('car')
    #[Synset('car.n.01'), Synset('car.n.02'), Synset('car.n.03'), Synset('car.n.04'),
    #Synset('cable_car.n.01')]
    for synset in wn.synsets('car'):
       print synset.lemma_names
    #['car', 'auto', 'automobile', 'machine', 'motorcar']
    #['car', 'railcar', 'railway_car', 'railroad_car']
    #['car', 'gondola']
    #['car', 'elevator_car']
    #['cable_car', 'car']
    motorcar = wn.synset('car.n.01')
    types_of_motorcar = motorcar.hyponyms()
    len(types_of_motorcar)
    #31
    types_of_motorcar[26]
    #Synset('ambulance.n.01')
    sorted([lemma.name for synset in types_of_motorcar for lemma in synset.lemmas])
    #['Model_T', 'S.U.V.', 'SUV', 'Stanley_Steamer', 'ambulance', 'beach_waggon',
    #...]
    motorcar.hypernyms()
    #[Synset('motor_vehicle.n.01')]
    paths = motorcar.hypernym_paths()
    len(paths)
    #2
    [synset.name for synset in paths[0]]
    #['entity.n.01', 'physical_entity.n.01', 'object.n.01', 'whole.n.02', 'artifact.n.01',
    #'instrumentality.n.03', 'container.n.01', 'wheeled_vehicle.n.01',
    #'self-propelled_vehicle.n.01', 'motor_vehicle.n.01', 'car.n.01']
    [synset.name for synset in paths[1]]
    #['entity.n.01', 'physical_entity.n.01', 'object.n.01', 'whole.n.02', 'artifact.n.01',
    #'instrumentality.n.03', 'conveyance.n.03', 'vehicle.n.01', 'wheeled_vehicle.n.01',
    #'self-propelled_vehicle.n.01', 'motor_vehicle.n.01', 'car.n.01']
    motorcar.root_hypernyms()
    #[Synset('entity.n.01')]
    wn.synset('tree.n.01').part_meronyms()
    #[Synset('burl.n.02'), Synset('crown.n.07'), Synset('stump.n.01'),
    #Synset('trunk.n.01'), Synset('limb.n.02')]
    wn.synset('tree.n.01').substance_meronyms()
    #[Synset('heartwood.n.01'), Synset('sapwood.n.01')]
    wn.synset('tree.n.01').member_holonyms()
    #[Synset('forest.n.01')]
    for synset in wn.synsets('mint', wn.NOUN):
        print synset.name + ':', synset.definition
    #batch.n.02: (often followed by `of') a large number or amount or extent
    #mint.n.02: any north temperate plant of the genus Mentha with aromatic leaves and
    #small mauve flowers
    #mint.n.03: any member of the mint family of plants
    #mint.n.04: the leaves of a mint plant used fresh or candied
    #mint.n.05: a candy that is flavored with a mint oil
    #mint.n.06: a plant where money is coined by authority of the government
    wn.synset('mint.n.04').part_holonyms()
    #[Synset('mint.n.02')]
    wn.synset('mint.n.04').substance_holonyms()
    #[Synset('mint.n.05')]
    wn.synset('walk.v.01').entailments()
    #[Synset('step.v.01')]
    wn.synset('eat.v.01').entailments()
    #[Synset('swallow.v.01'), Synset('chew.v.01')]
    wn.synset('tease.v.03').entailments()
    #[Synset('arouse.v.07'), Synset('disappoint.v.01')]
    #Antonym
    wn.lemma('supply.n.02.supply').antonyms()
    #[Lemma('demand.n.02.demand')]
    wn.lemma('rush.v.01.rush').antonyms()
    #[Lemma('linger.v.04.linger')]
    wn.lemma('horizontal.a.01.horizontal').antonyms()
    #[Lemma('vertical.a.01.vertical'), Lemma('inclined.a.02.inclined')]
    wn.lemma('staccato.r.01.staccato').antonyms()
    #[Lemma('legato.r.01.legato')]

    #Semantic Similarity
    #Semakin dekat path antara dua lemma, semakin mirip makna semantik kedua lemma tersebut
    right = wn.synset('right_whale.n.01')
    orca = wn.synset('orca.n.01')
    minke = wn.synset('minke_whale.n.01')
    tortoise = wn.synset('tortoise.n.01')
    novel = wn.synset('novel.n.01')
    print right.lowest_common_hypernyms(minke)
    #[Synset('baleen_whale.n.01')]
    print right.lowest_common_hypernyms(orca)
    #[Synset('whale.n.02')]
    print right.lowest_common_hypernyms(tortoise)
    #[Synset('vertebrate.n.01')]
    print right.lowest_common_hypernyms(novel)
    #[Synset('entity.n.01')]
    print wn.synset('baleen_whale.n.01').min_depth()
    #14
    print wn.synset('whale.n.02').min_depth()
    #13
    print wn.synset('vertebrate.n.01').min_depth()
    #8
    print wn.synset('entity.n.01').min_depth()
    #0
    print right.path_similarity(minke)
    #0.25
    print right.path_similarity(orca)
    #0.16666666666666666
    print right.path_similarity(tortoise)
    #0.076923076923076927
    print right.path_similarity(novel)
    #0.043478260869565216

    ##nltk web
    #from __future__ import division
    import nltk, re, pprint

    #from urllib import urlopen
    url = "http://www.gutenberg.org/files/2554/2554.txt"
    raw = urlopen(url).read()
    len(raw)
    raw[:75]

    #from __future__ import division
    #import nltk, re, pprint
    #from urllib import urlopen
    url = "http://www.gutenberg.org/files/2554/2554.txt"
    print "Accessing gutenberg #2554..."
    raw = urlopen(url).read()
    tokens = nltk.word_tokenize(raw)
    text = nltk.Text(tokens)
    text.concorddance("Gutenberg")
    text.collocations()
    text.similarity()

    #Mengakses data dengan tag HTML
    url = 'http://news.bbc.co.uk/2/hi/health/2284783.stm'
    htmlsite = urlopen(url)
    htmldata = htmlsite.read()
    htmlraw = nltk.clean_html(htmldata)
    htmltokens = nltk.word_tokenize(htmlraw)
    htmltexts = nltk.Text(htmltokens)
    htmltexts.concordance('gene')

    #Mengakses Berkas Lokal
    f = open('document.txt', 'r')
    data = f.read()
    tokens = nltk.word_tokenize(data)
    texts = nltk.Text(tokens)
    texts.concordance('gene')

    #Menulis Berkas Lokal
    f = open('document.txt', 'w')
    for word in sorted(htmltexts):
        f.write(word + '\n')

    #Mengakses RSS Feed
    import feedparser
    url = 'http://news.bbc.co.uk/2/hi/health/2284783.stm'
    htmlsite = urlopen(url)
    htmldata = htmlsite.read()
    htmlraw = nltk.clean_html(htmldata)
    htmltokens = nltk.word_tokenize(htmlraw)
    htmltexts = nltk.Text(htmltokens)
    htmltexts.concordance('gene')

    #Python dan PyScripter
    import os
    os.chdir('path\to\tugas')
    import  tugas
    reload(tugas)
    #NLTK dan Teks
    import nltk
    data = 'Sebuah contoh kalimat yang ingin dianalisis menggunakan NLTK'
    tokens = nltk.word_tokenize(data)
    text = nltk.Text(tokens)




if __name__ == '__main__':
    main()
