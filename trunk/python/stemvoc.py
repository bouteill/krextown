#!/usr/bin/env python
#
# stemvoc.py
# 
# Stemming using vocal and consonant patterns in Bahasa Indonesia.
# Anung B. Ariwibowo
# May 2012.
# 
# Outline ide
# Ada berapa jenis prefix dalam bahasa Indonesia? Masing-masing prefix
# itu diawali dengan huruf-huruf apa saja?
# Menurut situs wikipedia Indonesia
# http://id.wikipedia.org/wiki/Prefiks_dalam_bahasa_Indonesia
# ber-, ter-, me-, di-, ke-, ku-, kau-, pe-, per-, se-

def main():
    vocal = ['a', 'i', 'u', 'e', 'o']
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
        'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    kata = raw_input("Masukkan sebuah kata: ")
    kata = kata.lower()
    kata = kata.strip()

    for huruf in kata:
        if huruf in vocal:
            print 'V',
        elif huruf in consonant:
            print 'K',
        else:
            print '-',



if __name__ == '__main__':
    main()

