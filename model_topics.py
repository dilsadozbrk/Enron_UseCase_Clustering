import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import joblib

import gensim
import gensim.corpora as corpora
from gensim.models import CoherenceModel
from gensim.test.utils import datapath
from gensim import  models
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis
import pickle


with open('preprocessing/keywords.pkl', 'rb') as file:
    data = pickle.load(file)


# create dictionary and corpus both are needed for (LDA) topic modeling
# Create Dictionary
id2word = corpora.Dictionary(data)

# Create Corpus
texts = data

# Term Document Frequency
corpus = [id2word.doc2bow(text) for text in texts]


def lda_model(corpus, id2word, num_topics):

    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                            id2word=id2word,
                                            num_topics=num_topics,
                                            random_state=100,
                                            update_every=1,
                                            chunksize=2000,
                                            alpha='auto',
                                            per_word_topics=True)

    joblib.dump(lda_model, "model.pkl")


def model_score(ldamodel, corpus, texts, dictionary):

    perplexity = ldamodel.log_perplexity(corpus)
    print(f'Perplexity: {perplexity}')

    coherence_model_lda = CoherenceModel(model=ldamodel, texts=texts, dictionary=dictionary, coherence='c_v')
    coherence_lda = coherence_model_lda.get_coherence()
    print(f'\nCoherence Score: {coherence_lda}')


def visualization(ldamodel, corpus, id2word):
    pyLDAvis.enable_notebook(sort=True)
    vis = gensimvis.prepare(ldamodel, corpus, id2word, mds='mmds', R = 20)
    pyLDAvis.display(vis)


def topic_words_dic(ldamodel, num_topics, id2word):

    topic_token_dict = {}
    topic_words = []
    for i in range(num_topics):
        tt = ldamodel.get_topic_terms(i,topn=20)
        topic_words.append([id2word[pair[0]] for pair in tt])
        topic_token_dict[i] = topic_words[i] 
    print(topic_token_dict)
    with open('topic_dict.pkl', 'wb') as f:
        pickle.dump(topic_token_dict, f)

    
#lda_model(corpus, id2word, 8)
lda = joblib.load("model.pkl")
#model_score(lda, corpus, data, id2word)    
#visualization(lda, corpus, id2word)
topic_words_dic(lda, 8, id2word)



