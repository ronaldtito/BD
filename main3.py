from nltk.corpus import words
from english_words import english_words_set
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk.stem import LancasterStemmer
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


wordnet_lemmatizer = WordNetLemmatizer()
lancaster=LancasterStemmer()
import os
import nltk

stop_words = set(stopwords.words('english'))


#Archive = open('Filter/2gm-0000','r')
#Lematizacion = open('Lema/2gm-0000','a')
#
#for line in Archive:
#    word = line.split()
#    word1 = word[0].lower()
#    word2 = word[1].lower()
#
#    
#    weight = word[2]
#    Word = (word1 +'\t'+word2+'\t'+weight+'\n')
#    Lematizacion.write(Word)
#
#Archive.close()
#Lematizacion.close()

#determinar el tipo de word
#pos for better lemmma no stem 

#print(is_english("potatoes"))
#print(stem('dogs'))

def get_wordnet_pos(treebank_tag):
        """ Converts a Penn Tree-Bank part of speech tag into a corresponding WordNet-friendly tag. 
        Borrowed from: http://stackoverflow.com/questions/15586721/wordnet-lemmatization-and-pos-tagging-in-python. """
        if treebank_tag.startswith('J') or treebank_tag.startswith('A'):
            return wordnet.ADJ
        elif treebank_tag.startswith('V'):
            return wordnet.VERB
        elif treebank_tag.startswith('N'):
            return wordnet.NOUN
        elif treebank_tag.startswith('R'):
            return wordnet.ADV
        else:
            return None 

for i in range(10,32):
    Archive = open('Lema/2gm-00'+str(i),'r')
    Lematizacion = open('StopWords/2gm-00'+str(i),'a')
    for line in Archive:
        word = line.split()
        word1 = word[0].lower()
        word2 = word[1].lower()
        weight = word[2]
        if word1 not in stop_words and word2 not in stop_words:
            Word = (word1+'\t'+word2+'\t'+weight+'\n')
            Lematizacion.write(Word)

    Archive.close()
    Lematizacion.close()
