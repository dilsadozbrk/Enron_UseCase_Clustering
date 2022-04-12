# Goal: Email content to be cleaned & identify unique keywords

import json
import pandas as pd
import nltk
from gensim.utils import simple_preprocess
from gensim.models.phrases import Phrases, Phraser
import spacy


def sent_to_words(sentences):
    """
    Function to tokenize sentences in each email body into a list of words
    """
    for sentence in sentences:
        yield (simple_preprocess(str(sentence), deacc=True))


def remove_stopwords(text):
    """
    Function to remove stopwords.
    """
    stop_words = nltk.corpus.stopwords.words('english')
    stop_words.extend(['from', 'subject', 're', 'edu', 'use'])
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
    nlp = spacy.load('en_core_web_trf', disable=['parser', 'ner'])
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
    df = pd.read_csv("data/lay_k_emails.csv")

    data = df['Body'].values.tolist()
    #print(data[:2])

    # Convert sentences to words --> Try to optimize this!!
    data_words = list(sent_to_words(data[:2]))
    #print(data_words[:2])

    # Remove stop words
    data_words_nostops = remove_stopwords(data_words)
    #print(data_words_nostops[:2])

    # Form bigrams
    data_words_bigram = bigram(data_words_nostops)
    #print(data_words_bigram[:2])

    # Lemmatize --> Try to optimize this!!
    data_lemmatized = lemmatize(
        data_words_bigram, allowed_postages=['NOUN', 'ADJ', 'VERB', 'ADV'])

    print(data_lemmatized[:2])

    #jsonString = {"data": data_lemmatized}

    #with open('data/clean_body.json', 'w') as file:
    #    json.dump(jsonString, file)


preprocess_emails()
"""
def normalize_document(doc):
    
    # Remove stop words
    tokens = nltk.word_tokenize(doc)
    filtered_tokens = [token for token in tokens if token not in stopwords]
    doc = " ".join(filtered_tokens)
    #print(f"Doc: {doc}")
    return doc


normalize_corpus = np.vectorize(normalize_document)
#print(f"Normalize Corpus: {normalize_corpus}")

norm_corpus = normalize_corpus(df['Body'][0:5])
#print(f"Norm Corpus: {norm_corpus}")

"""
