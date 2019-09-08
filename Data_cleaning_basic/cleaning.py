
# coding: utf-8

# In[ ]:


import re
import os 
import string
import contractions
import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
import unicodedata
import pandas as pd
import numpy 
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer


porter = PorterStemmer()
lancaster=LancasterStemmer()


def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        word = unicode(word)
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def to_lowercase(words):
    """Convert all characters to lowercase from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = word.lower()
        new_words.append(new_word)
    return new_words

def remove_stopwords(words):
    """Remove stop words from list of tokenized words"""
    new_words = []
    #print (words)
    #print "stopwords"
    for word in words:
        if word not in stopwords.words('english'):
            new_words.append(word)
    return new_words


'''def stem_and_lemmatize(words):
    stems =[]
    lemmas =[]
    for word in words:
        stems.append(stem_words(word))
        lemmas.append(lemmatize_verbs(word))
    return stems, lemmas'''

def normalize(words):
    words = remove_non_ascii(words)
    words = to_lowercase(words)
   
    
    words = remove_stopwords(words)
    return words



dirpath = os.getcwd()
os.chdir('C:\Users\PratikParekh\Downloads\Project_bda\Text')
dirpath = os.getcwd()
#table = string.maketrans("","")
f = open("a94amj.txt", 'r')
word = []
tokens=[]
#text = f.read()
new_tokens=[]
for line in f:
    #print(line)
    
    line=line.strip()
    #freq = pd.Series(' '.join(text).split()).value_counts()[:10]
    #print (freq)
    p=re.compile(r'([a-z]\s([a-z]\s)+[a-z])')        #combine words in which 
    m=p.findall(line)
    #print(m)
 
    
    #print (mlist)
    type(m)
    
        

    if p.findall(line):
        #print "yes"
        mlist = str(m[0][0]).replace(" ","")        #mlist=m[0][0]
        #print (mlist)
        words=nltk.word_tokenize(mlist)
        for word in words :
            tokens.append(word)

    else :
        #print "no"
        #print line
        #print "Ojk"
        line = re.sub('[^\w\s]',"",line)
        line = re.sub ('_',"",line)
        line = re.sub(r'\d+', "", line)
        #print line
        line  = contractions.fix(line)
        #print line
        exclude = set(string.punctuation)
        line = ''.join(ch for ch in line if ch not in exclude)
        words=nltk.word_tokenize(line)
        for word in words :
            tokens.append(word)
        
    
    #print line
#print(tokens)
#tokens =unicode(tokens)
new_tokens = normalize(tokens)
print (new_tokens)
#print (new_tokens[1])
#stem_words=[]
stems=[]
lemmas = []
print("\n\n\n\n{0:20}{1:20}{2:20}".format("Word","Porter Stemmer","lancaster Stemmer"))
for word in new_tokens:
    stems.append(porter.stem(word))
    lemmas.append(lancaster.stem(word))
    print("{0:20}{1:20}{2:20}".format(word,porter.stem(word),lancaster.stem(word)))

print(stems)

print("\n\n\n\n" +str(lemmas))
#stems, lemmas = stem_and_lemmatize(new_tokens)
#print('Stemmed:\n', stems)
#print('\nLemmatized:\n', lemmas)

