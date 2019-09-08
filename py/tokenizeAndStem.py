import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3

stopwords = nltk.corpus.stopwords.words('english')


xDIR = 'C:/Users/V574361/Documents/bigdata/files'
synopses=[open(os.path.join(xDIR,os.listdir(xDIR)[1]), encoding="utf8").read()]

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")


def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
            # print(filtered_tokens[len(filtered_tokens)-1])
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems

def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens


#not super pythonic, no, not at all.
#use extend so it's a big flat list of vocab
def test1(synopses):
    totalvocab_stemmed = []
    totalvocab_tokenized = []
    for i in synopses:
        allwords_stemmed = tokenize_and_stem(i) #for each item in 'synopses', tokenize/stem
        totalvocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list
        
        allwords_tokenized = tokenize_only(i)
        totalvocab_tokenized.extend(allwords_tokenized)
        
    vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
    print('there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame')
    return [totalvocab_stemmed,totalvocab_tokenized]



def test(synopses):
    totalvocab_stemmed = []
    totalvocab_tokenized = []
    allwords_stemmed = tokenize_and_stem(synopses) #for each item in 'synopses', tokenize/stem
    totalvocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list
        
    allwords_tokenized = tokenize_only(synopses)
    totalvocab_tokenized.extend(allwords_tokenized)
        
    vocab_frame = pd.DataFrame({'words': totalvocab_tokenized}, index = totalvocab_stemmed)
    print('there are ' + str(vocab_frame.shape[0]) + ' items in vocab_frame')
    return vocab_frame
    #[totalvocab_stemmed,totalvocab_tokenized]
    

vocab_frame=test(synopses[0])


from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                 min_df=0.2, stop_words='english',
                                 use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))

#%time 
tfidf_matrix = tfidf_vectorizer.fit_transform(synopses) #fit the vectorizer to synopses

#print(tfidf_matrix.shape)