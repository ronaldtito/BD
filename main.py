from nltk.corpus import words
from english_words import english_words_set
from nltk.stem.snowball import SnowballStemmer
import os

def is_english(word):
    word1 = word.lower()
    if word1 in english_words_set:
        return True
    return False

Archive = open('Lemas1','r')
Filter = open('Lemas2','a')
lemas = []
for line in Archive:
    word = line.split()
    lemas.append(word[0])

lemas.sort()

for line in lemas:
    word = (line + '\n')
    Filter.write(word)

Archive.close()
Filter.close()


