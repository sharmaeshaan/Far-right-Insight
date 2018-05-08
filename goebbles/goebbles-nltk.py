import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import sqlite3

conn = sqlite3.connect('goebbles.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS wordcount (word, count INTEGER)')

def getfiles():
    # list all files in working dir
    dirlist = os.listdir(path='./')
    # place all content in list
    files = list()
    for f in dirlist:
        if f.endswith('.txt'):
            fhand = open(f, mode='r')
            files.append(fhand.read())
    return files

def allwords():
    stpwrds = stopwords.words('english')
    custom_stpwrds = ('’', ',', '.', 'would', 'way', 'year',
                      'make', 'rather', 'able', 'yet', 'meet', '“', '”', 'even', 'could', 'know', 'always', 'like', ' ', '', 'saw', 'says', 'got')
    stpwrds.extend(custom_stpwrds)
    filteredwords = list()
    for f in getfiles():
        words = word_tokenize(f)
        for w in words:
            w_lower = w.lower()
            if w_lower not in stpwrds:
                filteredwords.append(w_lower)
    return filteredwords

def countwords():
    freq = dict()
    for i in allwords():
        if i not in freq:
            count = 1
            freq[i] = count
        else:
            count = int(freq.get(i)) + 1
            freq[i] = count
    for key, val in list(freq.items()):
        if val < 5:
            del freq[key]
    return freq

def placewords():
    for w, c in countwords().items():
        # count = countwords().get(w)
        # if count < 5:
        #     pass
        # else:
        cur.execute('INSERT OR IGNORE INTO wordcount (word, count) VALUES (?, ?)', (w, c, ))
        print('inserted')
    conn.commit()

getfiles()
print('got content')
allwords()
print('got words')
countwords()
print('counted words')
placewords()
print('placed words')
