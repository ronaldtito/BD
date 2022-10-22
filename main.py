from nltk.corpus import words
from english_words import english_words_set
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()
import os

def is_english(word):
    word1 = word.lower()
    if word1 in english_words_set:
    #if word1 in words.words():
        return True
    return False


for i in range():
    text1 = 'corpus1/2gm-003'+str(i)
    text2 = 'Filter/2gm-003'+str(i)
    Archive = open(text1,'r')
    Filter = open(text2,'a')
 
    for line in Archive:
        word = line.split()
        if is_english(word[0]) and is_english(word[1]):
            Filter.write(line)

    Archive.close()
    Filter.close()


#Archive = open('Filter/2gm-0015','r')
#Lematizacion = open('Lema/2gm-0015','a')#

#for line in Archive:
#    word = line.split()
#    word1 = stem(word[0])
#    word2 = stem(word[1])
#    weight = word[2]
#    Word = (word1 +'\t'+word2+'\t'+weight+'\n')
#    Lematizacion.write(Word)#

#Archive.close()
#Lematizacion.close()#



def stem(word):
    st = SnowballStemmer("english").stem(word)
    return st

#print(is_english("potatoes"))
#print(stem('dogs'))