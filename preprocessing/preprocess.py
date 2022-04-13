# Goal: Email content to be cleaned & identify unique keywords

import json
import pandas as pd
import nltk
import spacy
from gensim.utils import simple_preprocess
from gensim.models.phrases import Phrases, Phraser
from functools import lru_cache
from tqdm import tqdm
import pickle

nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])


def sent_to_words(bodies):
    """
    Function to tokenize sentences in each email body into a list of words
    """
    for sentence in bodies:
        yield (simple_preprocess(str(sentence), deacc=True))
    """
    # Method 2
    raw_words = []
    for line in bodies:
        index = []
        for token in nlp(line):
            index.append(token.text)
        raw_words.append(index)
    return raw_words
    """


def remove_stopwords(text):
    """
    Function to remove stopwords.
    """

    print
    stop_words = nltk.corpus.stopwords.words('english')
    stop_words.extend(['from', 'subject', 're', 'edu', 'use', 'www'])
    return [[word for word in doc if word not in stop_words] for doc in text]


def bigram(words):
    """
    Function to form bigrams.
    """
    bigram = Phrases(words, min_count=5, threshold=100)
    bigram_mod = Phraser(bigram)
    return [bigram_mod[doc] for doc in words]


def lemmatize(texts,
              allowed_postages=['NOUN', 'ADJ', 'VERB',
                                'ADV']):  # Optimize this as well!
    """
    Funtion to lemmatize words.
    """
    texts_out = []
    for sent in texts:
        doc = nlp(" ".join(sent))
        texts_out.append(
            [token.lemma_ for token in doc if token.pos_ in allowed_postages])
    return texts_out


def preprocess_emails():
    """
    Main function in preprocess script to clean emails message body
    """
    df = pd.read_csv("emails.csv")

    data_bodies = df['Body'].values.tolist()
    #print(data[:2])

    # Convert sentences to words --> Try to optimize this!!
    data_words = list(tqdm(sent_to_words(data_bodies[:10000])))
    #print(data_words[:2])
    
    with open('data/data_word_list.pkl', 'wb') as f:
        pickle.dump(data_words, f)

    print("Sentences converted to words")
    # Remove stop words
    data_words_nostops = list(tqdm(remove_stopwords(data_words)))
    #print(data_words_nostops)
    print("Stop words removed")

    # Form bigrams
    data_words_bigram = list(tqdm(bigram(data_words_nostops)))
    #print(data_words_bigram[:2])
    print("Bigrams added")

    # Lemmatize --> Try to optimize this!!
    data_lemmatized = list(
        tqdm(
            lemmatize(data_words_bigram,
                      allowed_postages=['NOUN', 'ADJ', 'VERB', 'ADV'])))

    #print(data_lemmatized[:2])
    print("Lemmatization done")

    with open('data/lemmatized_word_list.pkl', 'wb') as f:
        pickle.dump(data_lemmatized, f)


preprocess_emails()
