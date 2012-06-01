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
    kata = raw_input("Masukkan sebuah kata: ")
    kata = kata.lower()
    kata = kata.strip()
    pola = vocalize(kata)
    print pola
    

def vocalize(word):
    '''
    >>> vocalize('apa')
    VKV
    >>> vocalize('sungguh')
    KVKKVK
    '''

    vocal = ['a', 'i', 'u', 'e', 'o']
    consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
        'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

    NORMAL, PREDIFTONG, PREMIXED = range(3)

    pola = ''

    state = NORMAL

    for huruf in word:
        if huruf in vocal:
            if huruf in ['a', 'o']:
                prev_letter = huruf
                continue
            if huruf in ['u'] and prev_letter == 'a':
                pola = pola + 'V'
                continue
            if huruf in ['i'] and prev_letter in ['a', 'o']:
                pola = pola + 'V'
                continue
            if prev_letter in consonant:
                pola = pola + 'KV'
                continue
            pola = pola+'V'
            continue
        if huruf in consonant:
            if huruf in ['k', 'n', 's']:
                prev_letter = huruf
                continue
            if huruf == 'y' and prev_letter in ['n', 's']:
                pola = pola + 'K'
                continue
            if huruf == 'g' and prev_letter == 'n':
                pola = pola + 'K'
                continue
            if huruf == 'h' and prev_letter == 'k':
                pola = pola + 'K'
                continue
            if prev_letter in vocal:
                pola = pola + 'VK'
                continue
            pola = pola+'K'
            continue
        pola = pola+'-'

    return pola


if __name__ == '__main__':
    main()

