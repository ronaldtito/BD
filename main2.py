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

for i in range(31,32): 
    Archive = open('StopWords/2gm-00'+str(i),'r')
    Lematizacion = open('Final/2gm-00'+str(i),'a')
    for line in Archive:
        word = line.split()
       # word1 = word[0].lower()
        #word2 = word[1].lower()
        word_tag1 = nltk.pos_tag(nltk.word_tokenize(word[0]))
        word_tag11 = (word_tag1[0][0],get_wordnet_pos(word_tag1[0][1]))
        word_tag2 = nltk.pos_tag(nltk.word_tokenize(word[1]))
        word_tag21 = (word_tag2[0][0],get_wordnet_pos(word_tag2[0][1]))
        if word_tag11[1] != None and word_tag21[1] != None:
            Word = (word_tag11[0]+'\t'+word_tag21[0]+'\t'+word[2]+'\n')
            Lematizacion.write(Word)#



    #    if(word_tag11[1] is None):
    #        lema1 = wordnet_lemmatizer.lemmatize(word_tag11[0])
    #    else:
    #        lema1 = wordnet_lemmatizer.lemmatize(word_tag11[0],word_tag11[1])
    #    if(word_tag21[1] is None):
    #        lema2 = wordnet_lemmatizer.lemmatize(word_tag21[0])
    #    else:
    #        lema2 = wordnet_lemmatizer.lemmatize(word_tag21[0],word_tag21[1])
    #    weight = word[2]
    #    Word = (lema1 +'\t'+lema2+'\t'+weight+'\n')#

    Archive.close()
    Lematizacion.close()