import pickle
import pyLDAvis
import pyLDAvis.gensim_models
import nltk
import gensim
import gensim.corpora as corpora
import pyLDAvis.gensim_models as gensimvis
nltk.download('stopwords')


def get_all_tokens_from_mails():
    with open('data/word_list.pkl', 'rb') as file:
        data = pickle.load(file)
    return data



def create_dictionary_and_corpus(data):
    """
    create dictionary and corpus both are needed 
    for (LDA) topic modeling
    """
    # Create Dictionary
    id2word = corpora.Dictionary(data)
    # Create Corpus
    texts = data
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]
    return id2word,texts,corpus



def train_model(id2word,corpus):
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                            id2word=id2word,
                                            num_topics=14,
                                            random_state=100,
                                            update_every=1,
                                            chunksize=100,
                                            passes=10,
                                            alpha='auto',
                                            per_word_topics=True)
    return lda_model


def prepare_model(id2word,corpus,lda_model):
    #pyLDAvis.enable_notebook(sort=True)
    vis = gensimvis.prepare(lda_model, corpus, id2word, mds='mmds', R = 30)
    return vis


def get_topic(vis):

    return list(vis.topic_info["Term"].iloc[0:10].values)


def get_tokens_by_topic(vis,topic_number):
    topic_group = vis.token_table.groupby("Topic")
    df_term = topic_group.get_group(topic_number).sort_values("Freq",ascending=False).head(10)
    return list(df_term["Term"].values)

def show_graph(vis):
    html_string = pyLDAvis.prepared_data_to_html(vis)
    from streamlit import components
    components.v1.html(html_string, width=1300, height=800)

def run() -> None:
    data = get_all_tokens_from_mails()
    id2word,texts,corpus = create_dictionary_and_corpus(data)
    lda_model = train_model(id2word,corpus)
    vis = prepare_model(id2word,corpus,lda_model)
    return vis