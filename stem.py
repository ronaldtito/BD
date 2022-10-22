from nltk.corpus import words
from english_words import english_words_set
from nltk.stem.snowball import SnowballStemmer
import os

def is_english(word):
    word1 = word.lower()
    if word1 in english_words_set:
        return True
    return False

Archive = open('DataFin','r')
Filter = open('DataFin1','a')

noword = ["e'er","o'er","abc"]#d'oeuvre l'oeil
clock = "o'clock"
for line in Archive:
    word = line.split()
    if word[0] not in noword and word[1] not in noword:
        if word[0] == clock:
            word[0] = 'oclock'
        if word[1] == clock:
            word[1] = 'oclock'
        Word = (word[0]+'\t'+word[1]+'\t'+word[2]+'\n')
        Filter.write(Word)
    #if len(word[0]) > 2 and len(word[1])>2 :
    #    Word = (word[0]+'\t'+word[1]+'\t'+word[2]+'\n')
    #    Filter.write(Word)

print ('a')
Archive.close()
Filter.close()


